#!/usr/bin/env python3
"""
LWC Linter - Module Structure Validation

Validates that LWC module repositories have the required files and structure
before running editorial checks.

Usage:
    python lwc_linter.py --content-path /path/to/module [OPTIONS]

Options:
    --content-path PATH    Path to module root (parent of Content/)
    --output PATH          Output file path for JSON results
    --changed-files FILE   File containing list of changed files (for PR checks)
    --verbose              Show detailed validation information
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import List, Optional, Set

# Add tools directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lwc_models import LintingResult, LintingError, LintingWarning
from lwc_constants import (
    REQUIRED_FILES, REQUIRED_DIRS, TOPIC_FILE_PATTERN, LintingRules
)


def validate_structure(module_path: str, changed_files: Optional[Set[str]] = None) -> LintingResult:
    """
    Validate module repository structure.

    Args:
        module_path: Path to module root directory
        changed_files: Optional set of changed file paths (for PR checks)

    Returns:
        LintingResult with errors and warnings
    """
    result = LintingResult()
    module_dir = Path(module_path)

    if not module_dir.exists():
        result.add_error(
            LintingRules.CONTENT_FOLDER_MISSING,
            f"Module path does not exist: {module_path}",
            str(module_path)
        )
        return result

    # Check required directories
    _check_required_dirs(module_dir, result)

    # Check required files
    _check_required_files(module_dir, result)

    # Check topic files exist
    _check_topic_files(module_dir, result)

    # Check for unexpected file changes (if changed_files provided)
    if changed_files:
        _check_unexpected_changes(module_dir, changed_files, result)

    # Validate topic files match ModuleStructure.json
    _check_topic_structure_match(module_dir, result)

    return result


def _check_required_dirs(module_dir: Path, result: LintingResult) -> None:
    """Check that required directories exist."""
    for dir_name in REQUIRED_DIRS:
        dir_path = module_dir / dir_name
        if not dir_path.exists():
            result.add_error(
                LintingRules.CONTENT_FOLDER_MISSING,
                f"Required directory missing: {dir_name}/",
                str(dir_path)
            )
        elif not dir_path.is_dir():
            result.add_error(
                LintingRules.CONTENT_FOLDER_MISSING,
                f"'{dir_name}' exists but is not a directory",
                str(dir_path)
            )


def _check_required_files(module_dir: Path, result: LintingResult) -> None:
    """Check that required files exist."""
    for file_name in REQUIRED_FILES:
        file_path = module_dir / file_name
        if not file_path.exists():
            if file_name == 'ModuleStructure.json':
                result.add_error(
                    LintingRules.MODULE_STRUCTURE_MISSING,
                    f"Required file missing: {file_name}",
                    str(file_path)
                )
            elif file_name == 'Metadata.json':
                result.add_error(
                    LintingRules.METADATA_MISSING,
                    f"Required file missing: {file_name}",
                    str(file_path)
                )


def _check_topic_files(module_dir: Path, result: LintingResult) -> None:
    """Check that at least one Topic-*.md file exists."""
    content_dir = module_dir / 'Content'
    if not content_dir.exists():
        return  # Already reported in _check_required_dirs

    pattern = re.compile(TOPIC_FILE_PATTERN)
    topic_files = [f for f in content_dir.iterdir() if f.is_file() and pattern.match(f.name)]

    if not topic_files:
        result.add_error(
            LintingRules.NO_TOPIC_FILES,
            "No Topic-*.md files found in Content/ directory",
            str(content_dir)
        )


def _check_unexpected_changes(
    module_dir: Path,
    changed_files: Set[str],
    result: LintingResult
) -> None:
    """
    Check for unexpected file changes outside Content/ directory.

    Warns if authors modified files they shouldn't typically touch.
    """
    expected_paths = {
        'Content/',
        'Images/',
        'Videos/',
        'Resources/',
    }

    unexpected = []
    for changed_file in changed_files:
        # Normalize path
        rel_path = changed_file.lstrip('./')

        # Check if file is in an expected location
        is_expected = False
        for expected in expected_paths:
            if rel_path.startswith(expected):
                is_expected = True
                break

        # Also allow specific root files
        if rel_path in ['Metadata.json', 'ModuleStructure.json', '.gitignore']:
            is_expected = True

        if not is_expected:
            unexpected.append(rel_path)

    if unexpected:
        result.add_warning(
            LintingRules.UNEXPECTED_FILE_CHANGES,
            f"Unexpected file changes outside Content/: {', '.join(unexpected[:5])}" +
            (f" (+{len(unexpected)-5} more)" if len(unexpected) > 5 else ""),
            str(module_dir)
        )


def _check_topic_structure_match(module_dir: Path, result: LintingResult) -> None:
    """
    Check that Topic files in Content/ match ModuleStructure.json.
    """
    structure_path = module_dir / 'ModuleStructure.json'
    content_dir = module_dir / 'Content'

    if not structure_path.exists() or not content_dir.exists():
        return  # Already reported elsewhere

    try:
        with open(structure_path) as f:
            structure = json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        result.add_warning(
            LintingRules.TOPIC_MISMATCH,
            f"Could not parse ModuleStructure.json: {e}",
            str(structure_path)
        )
        return

    # Get expected files from structure
    expected_files = set()
    for topic in structure.get('topics', []):
        if 'file' in topic:
            expected_files.add(topic['file'])
    for lab in structure.get('labs', []):
        if 'file' in lab:
            expected_files.add(lab['file'])

    # Get actual files
    pattern = re.compile(TOPIC_FILE_PATTERN)
    actual_files = {f.name for f in content_dir.iterdir() if f.is_file() and pattern.match(f.name)}

    # Check for mismatches
    missing_in_content = expected_files - actual_files
    extra_in_content = actual_files - expected_files

    if missing_in_content:
        result.add_warning(
            LintingRules.TOPIC_MISMATCH,
            f"Files in ModuleStructure.json but missing in Content/: {', '.join(sorted(missing_in_content))}",
            str(content_dir)
        )

    if extra_in_content:
        result.add_warning(
            LintingRules.TOPIC_MISMATCH,
            f"Files in Content/ but not in ModuleStructure.json: {', '.join(sorted(extra_in_content))}",
            str(content_dir)
        )


def format_json_output(result: LintingResult) -> str:
    """Format linting result as JSON."""
    return json.dumps(result.to_dict(), indent=2)


def format_text_output(result: LintingResult) -> str:
    """Format linting result as human-readable text."""
    lines = []

    if result.passed:
        lines.append("✓ Module structure validation passed")
    else:
        lines.append("✗ Module structure validation failed")

    if result.errors:
        lines.append(f"\nErrors ({len(result.errors)}):")
        for error in result.errors:
            lines.append(f"  [{error.rule_id}] {error.message}")
            if error.path:
                lines.append(f"           Path: {error.path}")

    if result.warnings:
        lines.append(f"\nWarnings ({len(result.warnings)}):")
        for warning in result.warnings:
            lines.append(f"  [{warning.rule_id}] {warning.message}")

    return '\n'.join(lines)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='LWC Module Structure Linting',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        '--content-path',
        required=True,
        help='Path to module root directory (parent of Content/)'
    )
    parser.add_argument(
        '--output',
        help='Output file path for JSON results'
    )
    parser.add_argument(
        '--changed-files',
        help='File containing list of changed files (one per line)'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed validation information'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output as JSON (default if --output specified)'
    )

    args = parser.parse_args()

    # Load changed files if provided
    changed_files = None
    if args.changed_files and os.path.exists(args.changed_files):
        with open(args.changed_files) as f:
            changed_files = {line.strip() for line in f if line.strip()}

    # Run validation
    if args.verbose:
        print(f"Validating module structure: {args.content_path}", file=sys.stderr)

    result = validate_structure(args.content_path, changed_files)

    # Format output
    if args.output or args.json:
        output = format_json_output(result)
    else:
        output = format_text_output(result)

    # Write output
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        if args.verbose:
            print(f"Results written to: {args.output}", file=sys.stderr)
    else:
        print(output)

    # Exit with appropriate code
    sys.exit(0 if result.passed else 1)


if __name__ == '__main__':
    main()
