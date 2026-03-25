#!/usr/bin/env python3
"""
LWC Editorial - AI Copy Editing for LWC Module Content

Processes Content/*.md files through the editorial validation pipeline,
preserving custom components and formatting results for PR comments.

Usage:
    python lwc_editorial.py --content-path /path/to/Content [OPTIONS]

Options:
    --content-path PATH    Path to Content/ directory
    --format FORMAT        Output format: markdown, json, pr-comment (default: markdown)
    --output PATH          Output file path (default: stdout)
    --results PATH         Load existing results JSON (for pr-comment format)
    --linting PATH         Load linting results JSON (for pr-comment format)
    --no-ai                Disable AI enhancement (regex rules only)
    --verbose              Show detailed processing information
"""

import argparse
import json
import os
import sys
import re
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

# Add tools directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from component_skipper import extract_components, restore_components, strip_markers, map_line_number
from lwc_models import (
    TopicFile, EditorialResult, EditorialIssue, EditorialCategory, FixSeverity,
    PRComment, LintingResult
)
from lwc_constants import TOPIC_FILE_PATTERN


def load_topic_files(content_path: str) -> List[TopicFile]:
    """
    Load all Topic-*.md files from the Content directory.

    Args:
        content_path: Path to Content/ directory

    Returns:
        List of TopicFile objects
    """
    content_dir = Path(content_path)
    topic_files = []

    if not content_dir.exists():
        return topic_files

    # Find all Topic-*.md files
    pattern = re.compile(TOPIC_FILE_PATTERN)
    for file_path in sorted(content_dir.iterdir()):
        if file_path.is_file() and pattern.match(file_path.name):
            try:
                raw_content = file_path.read_text(encoding='utf-8')
                topic_files.append(TopicFile(
                    path=file_path,
                    filename=file_path.name,
                    raw_content=raw_content
                ))
            except Exception as e:
                print(f"Warning: Could not read {file_path}: {e}", file=sys.stderr)

    return topic_files


def preprocess_for_editorial(topic_file: TopicFile) -> TopicFile:
    """
    Preprocess a topic file for editorial validation.

    Extracts custom components and strips markers, storing results
    in the TopicFile object.

    Args:
        topic_file: TopicFile to preprocess

    Returns:
        Updated TopicFile with clean_content and components populated
    """
    clean_text, components = extract_components(topic_file.raw_content)
    clean_text = strip_markers(clean_text)

    topic_file.clean_content = clean_text
    topic_file.components = components
    topic_file.word_count = len(clean_text.split())

    return topic_file


def validate_with_rules(topic_file: TopicFile, use_ai: bool = True) -> EditorialResult:
    """
    Run editorial validation on preprocessed topic file content.

    Args:
        topic_file: TopicFile with clean_content populated
        use_ai: Whether to use AI enhancement (default: True)

    Returns:
        EditorialResult with detected issues
    """
    issues = []

    # Try to use existing editorial_validation module
    try:
        from editorial_validation import validate_content, load_rules
        rules = load_rules()
        validation_results = validate_content(topic_file.clean_content, rules, use_ai=use_ai)

        # Convert to our issue format
        for i, result in enumerate(validation_results):
            # Map line number back to original file
            original_line = map_line_number(result.get('line', 1), topic_file.components)

            issue = EditorialIssue(
                id=f"{topic_file.filename}-{i+1:03d}",
                category=_map_category(result.get('category', 'grammar')),
                severity=_map_severity(result.get('severity', 'REVIEW')),
                line=original_line,
                original=result.get('original', ''),
                suggested=result.get('suggested', ''),
                rule_id=result.get('rule_id', 'UNKNOWN'),
                rationale=result.get('rationale', '')
            )
            issues.append(issue)

    except ImportError:
        # Fallback: basic validation without full rules engine
        issues = _basic_validation(topic_file)

    return EditorialResult(file=topic_file, issues=issues)


def _map_category(category_str: str) -> EditorialCategory:
    """Map category string to EditorialCategory enum."""
    mapping = {
        'cisco_style': EditorialCategory.CISCO_STYLE,
        'acronym': EditorialCategory.ACRONYM,
        'grammar': EditorialCategory.GRAMMAR,
        'terminology': EditorialCategory.TERMINOLOGY,
    }
    return mapping.get(category_str.lower(), EditorialCategory.GRAMMAR)


def _map_severity(severity_str: str) -> FixSeverity:
    """Map severity string to FixSeverity enum."""
    mapping = {
        'SAFE': FixSeverity.SAFE,
        'REVIEW': FixSeverity.REVIEW,
        'QUERY': FixSeverity.QUERY,
    }
    return mapping.get(severity_str.upper(), FixSeverity.REVIEW)


def _basic_validation(topic_file: TopicFile) -> List[EditorialIssue]:
    """
    Basic validation fallback when full rules engine unavailable.

    Checks for common issues like:
    - Double spaces
    - Trailing whitespace
    - Missing period at end of sentences
    """
    issues = []
    lines = topic_file.clean_content.split('\n')

    for line_num, line in enumerate(lines, 1):
        original_line = map_line_number(line_num, topic_file.components)

        # Double space check
        if '  ' in line and not line.strip().startswith('#'):
            issues.append(EditorialIssue(
                id=f"{topic_file.filename}-{len(issues)+1:03d}",
                category=EditorialCategory.GRAMMAR,
                severity=FixSeverity.SAFE,
                line=original_line,
                original='  ',
                suggested=' ',
                rule_id='DOUBLE_SPACE',
                rationale='Multiple consecutive spaces should be reduced to single space'
            ))

        # Trailing whitespace check
        if line.rstrip() != line:
            issues.append(EditorialIssue(
                id=f"{topic_file.filename}-{len(issues)+1:03d}",
                category=EditorialCategory.GRAMMAR,
                severity=FixSeverity.SAFE,
                line=original_line,
                original=line,
                suggested=line.rstrip(),
                rule_id='TRAILING_WHITESPACE',
                rationale='Lines should not have trailing whitespace'
            ))

    return issues


def apply_safe_fixes(topic_file: TopicFile, issues: List[EditorialIssue], verbose: bool = False) -> int:
    """
    Apply SAFE severity fixes to the original file.

    Args:
        topic_file: The TopicFile object with path to original file
        issues: List of editorial issues found
        verbose: Whether to print verbose output

    Returns:
        Number of fixes applied
    """
    safe_issues = [i for i in issues if i.severity == FixSeverity.SAFE]
    if not safe_issues:
        return 0

    # Read the original file content
    content = topic_file.raw_content
    fixes_applied = 0

    # Apply fixes by rule type
    for issue in safe_issues:
        if issue.rule_id == 'DOUBLE_SPACE':
            # Replace multiple consecutive spaces with single space (not in code blocks)
            new_content = re.sub(r'(?<!`)  +(?!`)', ' ', content)
            if new_content != content:
                content = new_content
                fixes_applied += 1
        elif issue.rule_id == 'TRAILING_WHITESPACE':
            # Remove trailing whitespace from all lines
            lines = content.split('\n')
            new_lines = [line.rstrip() for line in lines]
            new_content = '\n'.join(new_lines)
            if new_content != content:
                content = new_content
                fixes_applied += 1

    # Write back to file if changes were made
    if content != topic_file.raw_content:
        topic_file.path.write_text(content, encoding='utf-8')
        if verbose:
            print(f"  - Applied {fixes_applied} fixes to {topic_file.filename}", file=sys.stderr)

    return fixes_applied


def _get_severity_badge(severity: FixSeverity) -> str:
    """Get visual badge for severity level."""
    badges = {
        FixSeverity.SAFE: "![SAFE](https://img.shields.io/badge/SAFE-green)",
        FixSeverity.REVIEW: "![REVIEW](https://img.shields.io/badge/REVIEW-yellow)",
        FixSeverity.QUERY: "![QUERY](https://img.shields.io/badge/QUERY-orange)",
    }
    return badges.get(severity, "")


def _get_severity_emoji(severity: FixSeverity) -> str:
    """Get emoji indicator for severity level."""
    emojis = {
        FixSeverity.SAFE: ":white_check_mark:",
        FixSeverity.REVIEW: ":warning:",
        FixSeverity.QUERY: ":question:",
    }
    return emojis.get(severity, "")


def format_pr_comment(
    editorial_results: List[EditorialResult],
    linting_result: Optional[LintingResult] = None,
    repo_url: Optional[str] = None,
    branch: Optional[str] = None,
    content_path: str = "Content"
) -> str:
    """
    Format editorial results as a GitHub PR comment.

    Args:
        editorial_results: List of EditorialResult objects
        linting_result: Optional LintingResult object
        repo_url: Optional GitHub repository URL for "View in file" links
        branch: Optional branch name for file links
        content_path: Path to Content/ directory (default: Content)

    Returns:
        Formatted markdown string for PR comment
    """
    sections = ['## Editorial Review Results\n']

    # Summary statistics
    total_issues = sum(len(r.issues) for r in editorial_results)
    total_fixed = sum(r.auto_fixed for r in editorial_results)
    total_review = sum(r.needs_review for r in editorial_results)
    total_query = sum(1 for r in editorial_results for i in r.issues if i.severity == FixSeverity.QUERY)
    total_components = sum(r.skipped_components for r in editorial_results)

    # Status indicator
    if total_issues == 0:
        sections.append(':white_check_mark: **All checks passed!** No editorial issues found.\n')
    elif total_review == 0 and total_query == 0:
        sections.append(':white_check_mark: **All issues auto-fixed.** No manual review needed.\n')
    else:
        sections.append(f':warning: **{total_review + total_query} items need review.**\n')

    # Summary table with severity legend
    sections.append('### Summary\n')
    sections.append('| Metric | Count | Legend |')
    sections.append('|--------|-------|--------|')
    sections.append(f'| Total Issues | {total_issues} | |')
    sections.append(f'| :white_check_mark: Auto-Fixed (SAFE) | {total_fixed} | No action needed |')
    sections.append(f'| :warning: Needs Review (REVIEW) | {total_review - total_query} | Suggested change |')
    sections.append(f'| :question: Flagged (QUERY) | {total_query} | Needs discussion |')
    sections.append(f'| Components Skipped | {total_components} | Custom LWC components |')
    sections.append('')

    # Category breakdown
    if total_issues > 0:
        sections.append('### Issues by Category\n')
        sections.append('| Category | Issues | Fixed | Review |')
        sections.append('|----------|--------|-------|--------|')

        # Group by category
        by_category: Dict[str, List[EditorialIssue]] = {}
        for result in editorial_results:
            for issue in result.issues:
                cat = issue.category.value
                if cat not in by_category:
                    by_category[cat] = []
                by_category[cat].append(issue)

        for cat, issues in sorted(by_category.items()):
            fixed = sum(1 for i in issues if i.severity == FixSeverity.SAFE)
            review = len(issues) - fixed
            cat_display = cat.replace('_', ' ').title()
            sections.append(f'| {cat_display} | {len(issues)} | {fixed} | {review} |')

        sections.append('')

    # Linting results
    if linting_result:
        if linting_result.passed:
            sections.append('### Module Structure\n')
            sections.append('✓ All structure checks passed\n')
        else:
            sections.append('### Module Structure ⚠️\n')
            for error in linting_result.errors:
                sections.append(f'- **{error.rule_id}**: {error.message}')
            sections.append('')

    # Helper function to generate file link
    def _file_link(filename: str, line: int) -> str:
        """Generate GitHub file link or plain line reference."""
        if repo_url and branch:
            # Generate GitHub permalink
            file_path = f"{content_path}/{filename}"
            return f"[{filename}:{line}]({repo_url}/blob/{branch}/{file_path}#L{line})"
        return f"{filename}:{line}"

    # Detailed issues (expandable)
    review_count = total_review + total_query
    if review_count > 0:
        sections.append('### Issues Requiring Review\n')
        sections.append('<details>')
        sections.append(f'<summary>:warning: {review_count} items need review (click to expand)</summary>\n')
        sections.append('| Severity | Location | Category | Issue | Suggestion |')
        sections.append('|----------|----------|----------|-------|------------|')

        for result in editorial_results:
            for issue in result.issues:
                if issue.severity != FixSeverity.SAFE:
                    original_truncated = issue.original[:30] + '...' if len(issue.original) > 30 else issue.original
                    suggested_truncated = issue.suggested[:30] + '...' if len(issue.suggested) > 30 else issue.suggested
                    severity_icon = _get_severity_emoji(issue.severity)
                    location = _file_link(result.file.filename, issue.line)
                    sections.append(
                        f'| {severity_icon} | {location} | '
                        f'{issue.category.value} | `{original_truncated}` | `{suggested_truncated}` |'
                    )

        sections.append('\n</details>\n')

    # Auto-fixed summary
    if total_fixed > 0:
        sections.append(f'### Auto-Fixed ({total_fixed} items)\n')
        sections.append('These issues were automatically corrected:\n')
        sections.append('<details>')
        sections.append('<summary>View auto-fixed items</summary>\n')

        for result in editorial_results:
            for issue in result.issues:
                if issue.severity == FixSeverity.SAFE:
                    sections.append(f'- **{result.file.filename}:{issue.line}** - {issue.rule_id}')

        sections.append('\n</details>\n')

    return '\n'.join(sections)


def format_json_output(
    editorial_results: List[EditorialResult],
    linting_result: Optional[LintingResult] = None
) -> str:
    """Format results as JSON."""
    output = {
        'total_issues': sum(len(r.issues) for r in editorial_results),
        'auto_fixed': sum(r.auto_fixed for r in editorial_results),
        'needs_review': sum(r.needs_review for r in editorial_results),
        'skipped_components': sum(r.skipped_components for r in editorial_results),
        'files': [r.to_dict() for r in editorial_results],
    }
    if linting_result:
        output['linting'] = linting_result.to_dict()

    return json.dumps(output, indent=2)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='LWC Module AI Editorial Validation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        '--content-path',
        required=True,
        help='Path to Content/ directory'
    )
    parser.add_argument(
        '--format',
        choices=['markdown', 'json', 'pr-comment'],
        default='markdown',
        help='Output format (default: markdown)'
    )
    parser.add_argument(
        '--output',
        help='Output file path (default: stdout)'
    )
    parser.add_argument(
        '--results',
        help='Load existing results JSON (for pr-comment format)'
    )
    parser.add_argument(
        '--linting',
        help='Load linting results JSON (for pr-comment format)'
    )
    parser.add_argument(
        '--no-ai',
        action='store_true',
        help='Disable AI enhancement (regex rules only)'
    )
    parser.add_argument(
        '--repo-url',
        help='GitHub repository URL for "View in file" links'
    )
    parser.add_argument(
        '--branch',
        help='Branch name for file links'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed processing information'
    )
    parser.add_argument(
        '--apply-fixes',
        action='store_true',
        help='Apply SAFE fixes to files (writes changes back to disk)'
    )

    args = parser.parse_args()

    # Load linting results if provided
    linting_result = None
    if args.linting and os.path.exists(args.linting):
        with open(args.linting) as f:
            linting_data = json.load(f)
            linting_result = LintingResult(
                passed=linting_data.get('passed', True),
                errors=[],
                warnings=[]
            )

    # If loading existing results for PR comment formatting
    if args.results and os.path.exists(args.results):
        with open(args.results) as f:
            results_data = json.load(f)
        # Format as PR comment from existing data
        # (simplified - full implementation would reconstruct EditorialResult objects)
        output = format_pr_comment([], linting_result)
    else:
        # Load and process topic files
        if args.verbose:
            print(f"Loading topic files from: {args.content_path}", file=sys.stderr)

        topic_files = load_topic_files(args.content_path)

        if args.verbose:
            print(f"Found {len(topic_files)} topic files", file=sys.stderr)

        # Preprocess and validate each file
        editorial_results = []
        for topic_file in topic_files:
            if args.verbose:
                print(f"Processing: {topic_file.filename}", file=sys.stderr)

            preprocess_for_editorial(topic_file)
            result = validate_with_rules(topic_file, use_ai=not args.no_ai)
            editorial_results.append(result)

            if args.verbose:
                print(f"  - {len(result.issues)} issues found", file=sys.stderr)
                print(f"  - {len(topic_file.components)} components skipped", file=sys.stderr)

            # Apply fixes if requested
            if args.apply_fixes and result.issues:
                fixes_count = apply_safe_fixes(topic_file, result.issues, args.verbose)
                if fixes_count > 0 and args.verbose:
                    print(f"  - Applied {fixes_count} auto-fixes", file=sys.stderr)

        # Format output
        if args.format == 'json':
            output = format_json_output(editorial_results, linting_result)
        else:
            output = format_pr_comment(
                editorial_results,
                linting_result,
                repo_url=args.repo_url,
                branch=args.branch,
                content_path=args.content_path
            )

    # Write output
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        if args.verbose:
            print(f"Output written to: {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == '__main__':
    main()
