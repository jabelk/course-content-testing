#!/usr/bin/env python3
"""
Course AI Editing - Main CLI Entry Point

Processes DOCX course modules through the editorial validation pipeline.
Converts DOCX to markdown, validates against editorial rules, and generates
categorized change reports.

Usage:
    python course_editor.py <docx_path> [OPTIONS]

Options:
    --output OUTPUT    Output path for report (default: <input>-report.md)
    --json             Output as JSON instead of markdown
    --verbose          Show detailed processing information
    --no-ai            Disable AI enhancement (regex rules only)
    --progress         Show progress indicator for large documents

Examples:
    # Basic usage - generates markdown report
    python course_editor.py "Course Module.docx"

    # Specify output location
    python course_editor.py "Course.docx" --output report.md

    # JSON output for automation
    python course_editor.py "Course.docx" --json
"""
import os
import sys
import json
import argparse
import tempfile
import shutil
import time
from typing import Optional
from datetime import datetime

# Add tools directory to path for imports
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

from docx_converter import (
    convert_docx_to_markdown,
    create_temp_tutorial_structure,
    cleanup_temp_structure,
    check_pandoc_installed,
    ConversionResult
)
from course_models import CourseModule, ChangeReport
from editorial_models import ValidationResult, QualityScore


# =============================================================================
# Configuration
# =============================================================================

# Word count thresholds for progress indicator
LARGE_DOCUMENT_THRESHOLD = 5000  # words
PROGRESS_INTERVAL = 1000  # words between progress updates


# =============================================================================
# Core Functions
# =============================================================================

def convert_and_validate(
    docx_path: str,
    use_ai: bool = True,
    verbose: bool = False,
    show_progress: bool = False
) -> tuple[Optional[ValidationResult], Optional[CourseModule], str, str]:
    """
    Convert a DOCX file to markdown and validate it through editorial rules.

    This function:
    1. Converts DOCX to markdown using pandoc
    2. Creates a temp folder mimicking tutorial structure
    3. Calls existing editorial_validation.validate_tutorial()
    4. Returns ValidationResult

    Args:
        docx_path: Path to the DOCX file
        use_ai: Whether to use AI enhancement for rules
        verbose: Show detailed processing information
        show_progress: Show progress indicator for large documents

    Returns:
        Tuple of (ValidationResult, CourseModule, error_message, markdown_content)
        On success: (result, course_module, '', markdown_content)
        On failure: (None, None, error_message, '')
    """
    start_time = time.time()

    # Check pandoc is installed
    pandoc_ok, pandoc_msg = check_pandoc_installed()
    if not pandoc_ok:
        return None, None, f"Pandoc not available: {pandoc_msg}", ""

    # Validate input file
    if not os.path.exists(docx_path):
        return None, None, f"File not found: {docx_path}", ""

    if not docx_path.lower().endswith('.docx'):
        return None, None, f"Not a DOCX file: {docx_path}", ""

    # Get file size for progress estimation
    file_size = os.path.getsize(docx_path)
    if verbose:
        print(f"Processing: {docx_path} ({file_size / 1024:.1f} KB)")

    # Convert DOCX to markdown
    if show_progress:
        print("Converting DOCX to markdown...", end=" ", flush=True)

    conversion_result = convert_docx_to_markdown(docx_path, timeout=300)

    if not conversion_result.success:
        return None, None, f"Conversion failed: {conversion_result.error_message}", ""

    # Store markdown content for inline diff generation
    markdown_content = conversion_result.markdown_content

    if show_progress:
        print(f"done ({conversion_result.word_count} words)")

    # Check for large document
    is_large = conversion_result.word_count >= LARGE_DOCUMENT_THRESHOLD
    if is_large and not show_progress and verbose:
        print(f"Note: Large document ({conversion_result.word_count} words)")

    # Create CourseModule
    course_module = CourseModule.from_docx(docx_path, conversion_result.markdown_content)
    course_name = course_module.name

    if verbose:
        print(f"Course: {course_name}")
        print(f"Sections: {len(course_module.sections)}")
        print(f"Estimated duration: {course_module.estimated_duration}")

    # Create temp tutorial structure
    if show_progress:
        print("Creating temporary tutorial structure...", end=" ", flush=True)

    temp_folder, step_file = create_temp_tutorial_structure(
        conversion_result.markdown_content,
        course_name
    )

    if show_progress:
        print("done")

    try:
        # Load editorial rules and validate
        if show_progress:
            print("Running editorial validation...", end=" ", flush=True)
        elif verbose:
            print("Loading editorial rules...")

        from editorial_validation import load_rules, validate_tutorial, RULES_FILE

        rules_path = os.path.join(script_dir, RULES_FILE)
        rules = load_rules(rules_path)

        if verbose:
            print(f"Loaded {len(rules)} editorial rules")

        # Run validation
        result = validate_tutorial(
            folder_path=temp_folder,
            rules=rules,
            apply_fixes_flag=False,  # Never modify content for course editing
            use_ai=use_ai,
            verbose=verbose
        )

        if show_progress:
            print(f"done ({len(result.issues)} issues found)")

        # Update result with course-specific info
        result.tutorial_folder = course_name
        elapsed_time = int((time.time() - start_time) * 1000)
        result.processing_time_ms = elapsed_time

        return result, course_module, '', markdown_content

    finally:
        # Always cleanup temp folder
        cleanup_temp_structure(temp_folder)


def validate_docx_file(docx_path: str) -> tuple[bool, str]:
    """
    Validate that a DOCX file is readable and not malformed.

    Args:
        docx_path: Path to the DOCX file

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not os.path.exists(docx_path):
        return False, f"File not found: {docx_path}"

    if not docx_path.lower().endswith('.docx'):
        return False, f"Not a DOCX file (must end with .docx): {docx_path}"

    # Check file is not empty
    file_size = os.path.getsize(docx_path)
    if file_size == 0:
        return False, f"DOCX file is empty: {docx_path}"

    # Check file is not too large (over 100MB likely a problem)
    if file_size > 100 * 1024 * 1024:
        return False, f"DOCX file too large ({file_size / 1024 / 1024:.1f} MB): {docx_path}"

    # Try to read as ZIP (DOCX is a ZIP file)
    import zipfile
    try:
        with zipfile.ZipFile(docx_path, 'r') as z:
            # Check for required DOCX files
            required = ['[Content_Types].xml', 'word/document.xml']
            namelist = z.namelist()
            for req in required:
                if req not in namelist:
                    return False, f"Malformed DOCX: missing {req}"
    except zipfile.BadZipFile:
        return False, f"Malformed DOCX: not a valid ZIP archive"
    except Exception as e:
        return False, f"Error reading DOCX: {str(e)}"

    return True, ""


# =============================================================================
# Output Formatting
# =============================================================================

def format_json_output(
    result: ValidationResult,
    course_module: CourseModule
) -> str:
    """
    Format validation result as JSON.

    Args:
        result: ValidationResult from editorial validation
        course_module: CourseModule with document metadata

    Returns:
        JSON string
    """
    output = {
        'course': course_module.to_dict(),
        'validation': result.to_dict(),
        'generated_at': datetime.now().isoformat()
    }
    return json.dumps(output, indent=2)


def format_progress(word_count: int, total_words: int) -> str:
    """Format progress indicator string."""
    percent = (word_count / total_words) * 100 if total_words > 0 else 0
    bar_length = 30
    filled = int(bar_length * percent / 100)
    bar = '█' * filled + '░' * (bar_length - filled)
    return f"[{bar}] {percent:.0f}% ({word_count}/{total_words} words)"


# =============================================================================
# CLI Entry Point
# =============================================================================

def main():
    """Main entry point for course editor CLI."""
    parser = argparse.ArgumentParser(
        description='Process a DOCX course module through editorial validation.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    parser.add_argument(
        'docx_path',
        help='Path to DOCX file to process'
    )
    parser.add_argument(
        '--output', '-o',
        help='Output path for report (default: <input>-report.md)'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output as JSON instead of markdown'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show detailed processing information'
    )
    parser.add_argument(
        '--no-ai',
        action='store_true',
        help='Disable AI enhancement (regex rules only)'
    )
    parser.add_argument(
        '--progress',
        action='store_true',
        help='Show progress indicator for large documents'
    )
    parser.add_argument(
        '--docx-output',
        action='store_true',
        help='Generate DOCX with track changes instead of markdown report'
    )
    parser.add_argument(
        '--inline-diff',
        action='store_true',
        help='Generate inline diff with track-changes style markup (~~deleted~~ **added**)'
    )
    parser.add_argument(
        '--change-list',
        action='store_true',
        help='Generate change list with context preview (alternative to inline-diff)'
    )

    args = parser.parse_args()

    # Validate DOCX file first
    is_valid, error_msg = validate_docx_file(args.docx_path)
    if not is_valid:
        print(f"Error: {error_msg}", file=sys.stderr)
        return 1

    # Run conversion and validation
    result, course_module, error, markdown_content = convert_and_validate(
        docx_path=args.docx_path,
        use_ai=not args.no_ai,
        verbose=args.verbose,
        show_progress=args.progress
    )

    if error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    # Generate output
    if args.docx_output:
        # Generate DOCX with track changes
        from docx_track_changes import generate_track_changes_docx

        # Determine output path
        if args.output:
            docx_output_path = args.output
        else:
            base = os.path.splitext(args.docx_path)[0]
            docx_output_path = f"{base}_edited.docx"

        # Convert ValidationResult to dict format expected by track changes generator
        validation_dict = {
            'issues': [
                {
                    'original': issue.original_text,
                    'suggestion': issue.suggested_fix,
                    'line': issue.line_number,
                    'rule_id': issue.rule_id,
                    'category': getattr(issue, 'category', 'general'),
                    'fix_type': issue.fix_type.name if hasattr(issue.fix_type, 'name') else str(issue.fix_type),
                    'message': issue.message
                }
                for issue in result.issues
            ]
        }

        stats = generate_track_changes_docx(
            args.docx_path,
            docx_output_path,
            validation_dict,
            author="Editorial AI"
        )

        print(f"\nDOCX with track changes written to: {docx_output_path}")
        print(f"  Changes applied: {stats['changes_applied']}")
        print(f"  Comments added: {stats['comments_added']}")
        output = None  # No text output for DOCX mode

    elif args.inline_diff:
        # Generate inline diff with track-changes style markup
        from inline_diff_generator import generate_inline_diff
        output = generate_inline_diff(markdown_content, result, course_module.name)
    elif args.change_list:
        # Generate change list with context preview
        from inline_diff_generator import generate_change_list_with_context
        output = generate_change_list_with_context(result, course_module.name)
    elif args.json:
        output = format_json_output(result, course_module)
    else:
        # Generate full markdown report using report generator
        from course_report_generator import generate_report
        output = generate_report(result, course_module.name, course_module)

    # Write output (only for non-DOCX modes)
    if output and args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"Report written to: {args.output}")
    else:
        print(output)

    # Report summary to stderr for CLI feedback
    if args.output or args.json:
        score = result.quality_score
        print(f"\nProcessing complete:", file=sys.stderr)
        print(f"  Quality Score: {score.score}/10 ({score.interpretation})", file=sys.stderr)
        print(f"  Total Issues: {score.total_issues}", file=sys.stderr)
        print(f"  Processing Time: {result.processing_time_ms/1000:.1f}s", file=sys.stderr)

    return 0


def generate_basic_report(result: ValidationResult, course_module: CourseModule) -> str:
    """
    Generate a basic markdown report (temporary until T012-T018 implement full report).

    Args:
        result: ValidationResult from editorial validation
        course_module: CourseModule with document metadata

    Returns:
        Markdown report string
    """
    lines = []
    score = result.quality_score

    lines.append(f"# Editorial Review Report: {course_module.name}")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- **Quality Score**: {score.score}/10 ({score.interpretation})")
    lines.append(f"- **Total Issues**: {score.total_issues}")
    lines.append(f"  - Auto-fixable (SAFE): {score.safe_count}")
    lines.append(f"  - Needs Review (REVIEW): {score.review_count}")
    lines.append(f"  - Questions for Author (QUERY): {score.query_count}")
    lines.append("")
    lines.append("## Document Info")
    lines.append("")
    lines.append(f"- **Word Count**: {course_module.total_word_count}")
    lines.append(f"- **Sections**: {len(course_module.sections)}")
    lines.append(f"- **Estimated Duration**: {course_module.estimated_duration}")
    lines.append(f"- **Processing Time**: {result.processing_time_ms/1000:.1f}s")
    lines.append("")

    # Group issues by fix type
    by_type = result.get_issues_by_type()

    if by_type['SAFE']:
        lines.append("## Auto-fixable Issues (SAFE)")
        lines.append("")
        lines.append("| Line | Rule | Original | Suggested |")
        lines.append("|------|------|----------|-----------|")
        for issue in sorted(by_type['SAFE'], key=lambda x: x.line_number)[:20]:
            orig = issue.original_text[:30] + '...' if len(issue.original_text) > 30 else issue.original_text
            sugg = issue.suggested_fix[:30] + '...' if issue.suggested_fix and len(issue.suggested_fix) > 30 else (issue.suggested_fix or '')
            lines.append(f"| {issue.line_number} | {issue.rule_id} | `{orig}` | `{sugg}` |")
        if len(by_type['SAFE']) > 20:
            lines.append(f"\n*...and {len(by_type['SAFE']) - 20} more*")
        lines.append("")

    if by_type['REVIEW']:
        lines.append("## Items Needing Review (REVIEW)")
        lines.append("")
        for issue in sorted(by_type['REVIEW'], key=lambda x: x.line_number)[:15]:
            lines.append(f"- **Line {issue.line_number}**: {issue.message}")
            if issue.suggested_fix:
                lines.append(f"  - Suggestion: `{issue.original_text}` → `{issue.suggested_fix}`")
        if len(by_type['REVIEW']) > 15:
            lines.append(f"\n*...and {len(by_type['REVIEW']) - 15} more*")
        lines.append("")

    if by_type['QUERY']:
        lines.append("## Questions for Author (QUERY)")
        lines.append("")
        for issue in sorted(by_type['QUERY'], key=lambda x: x.line_number)[:10]:
            lines.append(f"- **Line {issue.line_number}**: {issue.message}")
        if len(by_type['QUERY']) > 10:
            lines.append(f"\n*...and {len(by_type['QUERY']) - 10} more*")
        lines.append("")

    lines.append("---")
    lines.append(f"*Generated by Course AI Editor on {datetime.now().strftime('%Y-%m-%d %H:%M')}*")

    return '\n'.join(lines)


if __name__ == '__main__':
    sys.exit(main())
