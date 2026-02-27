"""
Course Report Generator

Generates markdown change reports for course editorial review.
Maps editorial issues to Kim's 4 categories and formats for easy review.

Categories:
- Cisco Style Guide: Headings, terminology, GUI formatting, Cisco-specific punctuation
- Acronyms: First-use expansion, redundant expansion, product acronyms
- Technical Terms: Product naming, code style
- Chicago Manual: Structure, general punctuation, grammar

Fix Types:
- SAFE: Auto-fixable, high confidence
- REVIEW: Applied but needs verification
- QUERY: Not applied, author decision required
"""
import os
from datetime import datetime
from typing import Dict, List, Optional

# Add tools directory to path for imports
import sys
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

from editorial_models import ValidationResult, EditorialIssue, QualityScore
from course_models import CourseModule, CATEGORY_MAPPING, CISCO_PUNCTUATION_RULES, map_category


# =============================================================================
# Category Mapping
# =============================================================================

def get_category_from_rule_id(rule_id: str) -> str:
    """
    Extract Kim's category from a rule ID.

    Rule IDs follow pattern: CATEGORY_RULE_NAME (e.g., PUNCT_DOUBLE_SPACE)

    Args:
        rule_id: Editorial rule ID

    Returns:
        One of Kim's 4 categories
    """
    # Map rule prefixes to existing categories
    prefix_to_category = {
        'PUNCT': 'punctuation',
        'TERM': 'terminology',
        'HEADING': 'heading',
        'GUI': 'gui_format',
        'CODE': 'code_style',
        'STRUCT': 'structure',
        'PRODUCT': 'product_naming',
        'ACRONYM': 'acronym',
        'AI': 'structure',  # AI-enhanced rules are usually structural
    }

    # Get prefix from rule_id
    prefix = rule_id.split('_')[0] if '_' in rule_id else rule_id
    existing_category = prefix_to_category.get(prefix, 'other')

    return map_category(existing_category, rule_id)


def group_issues_by_kim_category(issues: List[EditorialIssue]) -> Dict[str, List[EditorialIssue]]:
    """
    Group issues by Kim's 4 categories.

    Args:
        issues: List of EditorialIssue objects

    Returns:
        Dict mapping category names to issue lists
    """
    categories = {
        'Cisco Style Guide': [],
        'Acronyms': [],
        'Technical Terms': [],
        'Chicago Manual': []
    }

    for issue in issues:
        category = get_category_from_rule_id(issue.rule_id)
        categories[category].append(issue)

    return categories


# =============================================================================
# Report Generation
# =============================================================================

def generate_report(
    result: ValidationResult,
    course_name: str,
    course_module: Optional[CourseModule] = None
) -> str:
    """
    Generate a markdown change report from validation results.

    Args:
        result: ValidationResult from editorial validation
        course_name: Name of the course module
        course_module: Optional CourseModule for additional metadata

    Returns:
        Markdown formatted report string
    """
    lines = []

    # Header
    lines.extend(generate_header(result, course_name, course_module))

    # Summary
    lines.extend(generate_summary(result))

    # Changes by Category
    lines.extend(generate_category_sections(result))

    # Detailed Changes (sorted by line number)
    lines.extend(generate_detailed_changes(result))

    # Footer
    lines.extend(generate_footer(result))

    return '\n'.join(lines)


def generate_header(
    result: ValidationResult,
    course_name: str,
    course_module: Optional[CourseModule]
) -> List[str]:
    """Generate report header section."""
    lines = []
    score = result.quality_score

    lines.append(f"# Editorial Review Report: {course_name}")
    lines.append("")

    # Quality Score Badge
    score_emoji = get_score_emoji(score.score)
    lines.append(f"**Quality Score**: {score_emoji} {score.score}/10 ({score.interpretation})")
    lines.append("")

    # Document Info
    if course_module:
        lines.append("| Property | Value |")
        lines.append("|----------|-------|")
        lines.append(f"| Word Count | {course_module.total_word_count:,} |")
        lines.append(f"| Sections | {len(course_module.sections)} |")
        lines.append(f"| Estimated Duration | {course_module.estimated_duration} |")
        lines.append(f"| Processing Time | {result.processing_time_ms/1000:.1f}s |")
        lines.append("")

    return lines


def get_score_emoji(score: float) -> str:
    """Get emoji indicator for quality score."""
    if score >= 9:
        return "🟢"  # Green - excellent
    elif score >= 7:
        return "🟡"  # Yellow - good
    elif score >= 5:
        return "🟠"  # Orange - moderate
    else:
        return "🔴"  # Red - needs work


def generate_summary(result: ValidationResult) -> List[str]:
    """Generate summary section with issue counts."""
    lines = []
    score = result.quality_score

    lines.append("## Summary")
    lines.append("")
    lines.append(f"**Total Issues**: {score.total_issues}")
    lines.append("")
    lines.append("| Fix Type | Count | Description |")
    lines.append("|----------|-------|-------------|")
    lines.append(f"| SAFE | {score.safe_count} | Auto-fixable with high confidence |")
    lines.append(f"| REVIEW | {score.review_count} | Applied but needs human verification |")
    lines.append(f"| QUERY | {score.query_count} | Questions for author - not auto-fixed |")
    lines.append("")

    # Category breakdown
    by_category = group_issues_by_kim_category(result.issues)
    category_counts = {cat: len(issues) for cat, issues in by_category.items() if issues}

    if category_counts:
        lines.append("### Issues by Category")
        lines.append("")
        lines.append("| Category | Count |")
        lines.append("|----------|-------|")
        for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
            lines.append(f"| {cat} | {count} |")
        lines.append("")

    return lines


def generate_category_sections(result: ValidationResult) -> List[str]:
    """Generate Changes by Category sections with tables."""
    lines = []

    lines.append("## Changes by Category")
    lines.append("")

    by_category = group_issues_by_kim_category(result.issues)

    for category in ['Cisco Style Guide', 'Acronyms', 'Technical Terms', 'Chicago Manual']:
        issues = by_category[category]
        if not issues:
            continue

        lines.append(f"### {category} ({len(issues)} issues)")
        lines.append("")

        # Group by fix type
        by_type = {'SAFE': [], 'REVIEW': [], 'QUERY': []}
        for issue in issues:
            if issue.fix_type in by_type:
                by_type[issue.fix_type].append(issue)

        # SAFE issues table
        safe_issues = by_type['SAFE']
        if safe_issues:
            lines.append("**Auto-fixable (SAFE)**:")
            lines.append("")
            lines.append("| Line | Original | Suggested | Rationale |")
            lines.append("|------|----------|-----------|-----------|")
            for issue in sorted(safe_issues, key=lambda x: x.line_number)[:15]:
                orig = escape_table_cell(truncate(issue.original_text, 30))
                sugg = escape_table_cell(truncate(issue.suggested_fix or '', 30))
                rationale = get_rationale(issue)
                lines.append(f"| {issue.line_number} | `{orig}` | `{sugg}` | {rationale} |")
            if len(safe_issues) > 15:
                lines.append(f"| ... | *{len(safe_issues) - 15} more* | | |")
            lines.append("")

        # REVIEW issues table
        review_issues = by_type['REVIEW']
        if review_issues:
            lines.append("**Needs Review (REVIEW)**:")
            lines.append("")
            lines.append("| Line | Original | Suggested | Rationale |")
            lines.append("|------|----------|-----------|-----------|")
            for issue in sorted(review_issues, key=lambda x: x.line_number)[:10]:
                orig = escape_table_cell(truncate(issue.original_text, 30))
                sugg = escape_table_cell(truncate(issue.suggested_fix or '', 30))
                rationale = get_rationale(issue)
                lines.append(f"| {issue.line_number} | `{orig}` | `{sugg}` | {rationale} |")
            if len(review_issues) > 10:
                lines.append(f"| ... | *{len(review_issues) - 10} more* | | |")
            lines.append("")

        # QUERY issues list
        query_issues = by_type['QUERY']
        if query_issues:
            lines.append("**Questions for Author (QUERY)**:")
            lines.append("")
            for issue in sorted(query_issues, key=lambda x: x.line_number)[:8]:
                lines.append(f"- **Line {issue.line_number}**: {issue.message}")
            if len(query_issues) > 8:
                lines.append(f"- *...and {len(query_issues) - 8} more questions*")
            lines.append("")

    return lines


def generate_detailed_changes(result: ValidationResult) -> List[str]:
    """Generate Detailed Changes section sorted by line number."""
    lines = []

    lines.append("## Detailed Changes")
    lines.append("")
    lines.append("*All issues sorted by line number for easy review:*")
    lines.append("")

    sorted_issues = sorted(result.issues, key=lambda x: x.line_number)

    # Group into chunks of 50 for readability
    chunk_size = 50
    total = len(sorted_issues)

    if total == 0:
        lines.append("*No issues found.*")
        lines.append("")
        return lines

    lines.append("<details>")
    lines.append(f"<summary>Click to expand all {total} issues</summary>")
    lines.append("")

    lines.append("| Line | Type | Rule | Message |")
    lines.append("|------|------|------|---------|")

    for issue in sorted_issues:
        type_badge = get_type_badge(issue.fix_type)
        msg = escape_table_cell(truncate(issue.message, 50))
        lines.append(f"| {issue.line_number} | {type_badge} | {issue.rule_id} | {msg} |")

    lines.append("")
    lines.append("</details>")
    lines.append("")

    return lines


def generate_footer(result: ValidationResult) -> List[str]:
    """Generate report footer."""
    lines = []

    lines.append("---")
    lines.append("")
    lines.append(f"*Generated by Course AI Editor on {datetime.now().strftime('%Y-%m-%d %H:%M')}*")
    lines.append("")
    lines.append("**Fix Type Legend**:")
    lines.append("- 🟢 **SAFE**: High-confidence fix, can be auto-applied")
    lines.append("- 🟡 **REVIEW**: Applied fix, please verify")
    lines.append("- 🔴 **QUERY**: Question for author, not auto-fixed")

    return lines


# =============================================================================
# Helper Functions
# =============================================================================

def truncate(text: str, max_length: int) -> str:
    """Truncate text to max length with ellipsis."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + '...'


def escape_table_cell(text: str) -> str:
    """Escape special characters for markdown table cells."""
    # Replace pipe characters which break tables
    text = text.replace('|', '\\|')
    # Replace newlines
    text = text.replace('\n', ' ')
    text = text.replace('\r', '')
    return text


def get_type_badge(fix_type: str) -> str:
    """Get emoji badge for fix type."""
    badges = {
        'SAFE': '🟢',
        'REVIEW': '🟡',
        'QUERY': '🔴'
    }
    return badges.get(fix_type, '⚪')


def get_rationale(issue: EditorialIssue) -> str:
    """Extract a short rationale from issue message."""
    # The message often contains the rationale
    msg = issue.message

    # Remove redundant text patterns
    patterns_to_remove = [
        "Consider ",
        "Found: ",
        "Detected: ",
    ]

    for pattern in patterns_to_remove:
        if msg.startswith(pattern):
            msg = msg[len(pattern):]

    return truncate(msg, 40)


# =============================================================================
# CLI Interface
# =============================================================================

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Generate markdown report from validation JSON'
    )
    parser.add_argument('json_file', help='Path to validation JSON file')
    parser.add_argument('--output', '-o', help='Output markdown file')

    args = parser.parse_args()

    # Load validation result from JSON
    import json
    with open(args.json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Reconstruct ValidationResult
    from editorial_models import ValidationResult, EditorialIssue, QualityScore

    result = ValidationResult(tutorial_folder=data.get('tutorial_folder', 'Unknown'))
    result.files_processed = data.get('files_processed', [])
    result.processing_time_ms = data.get('processing_time_ms', 0)

    # Reconstruct issues
    for issue_data in data.get('issues', []):
        issue = EditorialIssue(
            rule_id=issue_data['rule_id'],
            file_path=issue_data['file_path'],
            line_number=issue_data['line_number'],
            original_text=issue_data['original_text'],
            fix_type=issue_data['fix_type'],
            message=issue_data['message'],
            confidence=issue_data['confidence'],
            suggested_fix=issue_data.get('suggested_fix')
        )
        result.add_issue(issue)

    result.calculate_score()

    # Generate report
    report = generate_report(result, result.tutorial_folder)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Report written to: {args.output}")
    else:
        print(report)
