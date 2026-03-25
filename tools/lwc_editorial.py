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
import yaml
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

# Add tools directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from component_skipper import extract_components, restore_components, strip_markers, map_line_number
from lwc_models import (
    TopicFile, EditorialResult, EditorialIssue, EditorialCategory, FixSeverity,
    PRComment, LintingResult, EditorialRule, AcronymEntry
)
from lwc_constants import TOPIC_FILE_PATTERN

# Global caches for rules and acronyms
_EDITORIAL_RULES: List[EditorialRule] = []
_ACRONYM_DATABASE: Dict[str, AcronymEntry] = {}


def load_editorial_rules(rules_file: Optional[str] = None) -> List[EditorialRule]:
    """
    Load editorial rules from YAML file.

    Args:
        rules_file: Path to editorial_rules.yaml (default: same directory as this script)

    Returns:
        List of EditorialRule objects
    """
    global _EDITORIAL_RULES
    if _EDITORIAL_RULES and not rules_file:
        return _EDITORIAL_RULES

    if rules_file is None:
        rules_file = os.path.join(os.path.dirname(__file__), 'editorial_rules.yaml')

    rules = []
    try:
        with open(rules_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        for rule_data in data.get('rules', []):
            if not rule_data.get('enabled', True):
                continue

            rule = EditorialRule(
                id=rule_data.get('id', ''),
                name=rule_data.get('name', ''),
                category=rule_data.get('category', 'grammar'),
                severity=rule_data.get('severity', 'medium'),
                fix_type=rule_data.get('fix_type', 'REVIEW'),
                pattern=rule_data.get('pattern', ''),
                pattern_type=rule_data.get('pattern_type', 'regex'),
                message=rule_data.get('message', ''),
                suggestion_template=rule_data.get('suggestion_template', ''),
                enabled=rule_data.get('enabled', True),
                priority=rule_data.get('priority', 50),
                context_skip=rule_data.get('context_skip', []),
            )
            rules.append(rule)

        # Sort by priority (lower = higher priority)
        rules.sort(key=lambda r: r.priority)
        _EDITORIAL_RULES = rules

    except Exception as e:
        print(f"Warning: Could not load editorial rules from {rules_file}: {e}", file=sys.stderr)

    return rules


def load_acronym_database(db_file: Optional[str] = None) -> Dict[str, AcronymEntry]:
    """
    Load acronym database from JSON file.

    Args:
        db_file: Path to acronym-database.json (default: .claude/references/)

    Returns:
        Dictionary mapping acronyms to AcronymEntry objects
    """
    global _ACRONYM_DATABASE
    if _ACRONYM_DATABASE and not db_file:
        return _ACRONYM_DATABASE

    if db_file is None:
        # Default path relative to tools directory
        db_file = os.path.join(
            os.path.dirname(__file__), '..', '.claude', 'references', 'acronym-database.json'
        )

    acronyms = {}
    try:
        with open(db_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Process each category in the database
        for category, entries in data.items():
            if category.startswith('_'):  # Skip metadata
                continue

            if isinstance(entries, dict):
                for acronym, entry_data in entries.items():
                    if isinstance(entry_data, dict):
                        entry = AcronymEntry(
                            acronym=acronym,
                            expansion=entry_data.get('expansion', ''),
                            category=category,
                            full_name=entry_data.get('full_name'),
                            first_use=entry_data.get('first_use'),
                            subsequent=entry_data.get('subsequent', []),
                            deprecated=entry_data.get('deprecated', False),
                            well_known=entry_data.get('well_known', False),
                            skip_expansion=entry_data.get('skip_expansion', False),
                            notes=entry_data.get('notes'),
                        )
                        acronyms[acronym] = entry
                    elif isinstance(entry_data, str):
                        # Simple string entry (just expansion)
                        entry = AcronymEntry(
                            acronym=acronym,
                            expansion=entry_data,
                            category=category,
                        )
                        acronyms[acronym] = entry

        _ACRONYM_DATABASE = acronyms

    except Exception as e:
        print(f"Warning: Could not load acronym database from {db_file}: {e}", file=sys.stderr)

    return acronyms


def apply_rule(rule: EditorialRule, content: str, filename: str, issue_counter: int) -> Tuple[List[EditorialIssue], int]:
    """
    Apply a single editorial rule to content.

    Args:
        rule: EditorialRule to apply
        content: Text content to validate
        filename: Source filename for issue IDs
        issue_counter: Starting counter for issue IDs

    Returns:
        Tuple of (list of issues found, updated counter)
    """
    issues = []

    if rule.pattern_type != 'regex' or not rule.pattern:
        return issues, issue_counter

    try:
        pattern = re.compile(rule.pattern, re.IGNORECASE)
    except re.error:
        return issues, issue_counter

    lines = content.split('\n')
    for line_num, line in enumerate(lines, 1):
        # Skip code blocks (simple heuristic)
        if 'code_block' in rule.context_skip and line.strip().startswith('```'):
            continue

        # Skip inline code if needed
        if 'inline_code' in rule.context_skip:
            # Remove inline code for checking
            check_line = re.sub(r'`[^`]+`', '', line)
        else:
            check_line = line

        for match in pattern.finditer(check_line):
            issue_counter += 1

            # Generate suggestion based on rule
            original = match.group(0)
            suggested = _generate_suggestion(rule, original)

            issue = EditorialIssue(
                id=f"{filename}-{issue_counter:03d}",
                category=rule.get_category_enum(),
                severity=rule.get_fix_severity(),
                line=line_num,
                original=original,
                suggested=suggested,
                rule_id=rule.id,
                rationale=rule.message
            )
            issues.append(issue)

    return issues, issue_counter


def _generate_suggestion(rule: EditorialRule, original: str) -> str:
    """Generate a fix suggestion based on rule and matched text."""
    # Common replacements based on rule ID patterns
    replacements = {
        'TERM_CLICK_ON': lambda m: re.sub(r'\bclick on\b', 'click', m, flags=re.I),
        'TERM_IN_ORDER_TO': lambda m: re.sub(r'\bin order to\b', 'to', m, flags=re.I),
        'TERM_UTILIZE': lambda m: re.sub(r'\butilize[sd]?\b', 'use', m, flags=re.I),
        'TERM_ALLOWS_YOU_TO': lambda m: re.sub(r'\ballows you to\b', 'lets you', m, flags=re.I),
        'TERM_MAKE_SURE': lambda m: re.sub(r'\b[Mm]ake sure\b', 'ensure', m),
        'TERM_BLACKLIST': lambda m: re.sub(r'\bblacklist(?:ed|ing|s)?\b', 'blocked list', m, flags=re.I),
        'TERM_WHITELIST': lambda m: re.sub(r'\bwhitelist(?:ed|ing|s)?\b', 'allowed list', m, flags=re.I),
        'TERM_CISCO_SYSTEMS': lambda m: re.sub(r'\bCisco Systems\b', 'Cisco', m),
        'TERM_REFER_TO': lambda m: re.sub(r'\b[Rr]efer to\b', 'see', m),
        'PUNCT_DOUBLE_SPACE': lambda m: re.sub(r'  +', ' ', m),
        'GRAMMAR_COMPOUND_WELL_KNOWN': lambda m: 'well-known',
        'GRAMMAR_COMPOUND_REAL_TIME': lambda m: 'real-time',
        'GRAMMAR_COMPOUND_END_TO_END': lambda m: 'end-to-end',
    }

    if rule.id in replacements:
        return replacements[rule.id](original)

    # Default: return original with suggestion note
    return f"{original} -> [see suggestion]"


def validate_acronyms(content: str, acronym_db: Dict[str, AcronymEntry], filename: str, issue_counter: int) -> Tuple[List[EditorialIssue], int]:
    """
    Validate acronyms in content against the database.

    Checks for:
    - Deprecated acronyms (FTD, FMC, DNA Center, etc.)
    - Unknown acronyms not in database
    - First-use expansion (REVIEW severity)

    Args:
        content: Text content to validate
        acronym_db: Loaded acronym database
        filename: Source filename for issue IDs
        issue_counter: Starting counter for issue IDs

    Returns:
        Tuple of (list of issues found, updated counter)
    """
    issues = []

    # Deprecated product names (multi-word)
    DEPRECATED_PRODUCTS = {
        "DNA Center": ("Cisco Catalyst Center", "DNA Center was rebranded to Cisco Catalyst Center"),
        "Webex Teams": ("Webex", "Webex Teams was rebranded to simply 'Webex'"),
        "Azure AD": ("Microsoft Entra ID", "Azure AD was rebranded to Microsoft Entra ID"),
    }

    lines = content.split('\n')

    # Check deprecated product names
    for line_num, line in enumerate(lines, 1):
        for product, (replacement, notes) in DEPRECATED_PRODUCTS.items():
            if product in line:
                issue_counter += 1
                issues.append(EditorialIssue(
                    id=f"{filename}-{issue_counter:03d}",
                    category=EditorialCategory.PRODUCT_NAMING,
                    severity=FixSeverity.REVIEW,
                    line=line_num,
                    original=product,
                    suggested=replacement,
                    rule_id="PROD_DEPRECATED_NAME",
                    rationale=notes
                ))

    # Acronym pattern: 2-6 uppercase letters
    acronym_pattern = re.compile(r'\b([A-Z][A-Z0-9-]{1,5})\b')
    seen_acronyms: set = set()

    # Skip common terms that don't need expansion
    SKIP_ACRONYMS = {
        'OK', 'AM', 'PM', 'US', 'UK', 'TV', 'PC', 'ID', 'IP',
        'GB', 'MB', 'KB', 'TB', 'CPU', 'RAM', 'ROM', 'USB', 'HTTP',
        'HTTPS', 'HTML', 'CSS', 'JSON', 'XML', 'PDF', 'YAML', 'PNG',
        'JPG', 'JPEG', 'GIF', 'SVG', 'MD', 'API', 'SDK', 'CLI', 'GUI',
        'OS', 'VM', 'AWS', 'GCP', 'UI', 'UX', 'FAQ', 'TBD', 'TODO',
        'NOTE', 'SD', 'WAN', 'LAN', 'GET', 'POST', 'PUT', 'DELETE',
    }

    in_code_block = False
    for line_num, line in enumerate(lines, 1):
        # Track code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        # Remove inline code before scanning
        check_line = re.sub(r'`[^`]+`', '', line)

        for match in acronym_pattern.finditer(check_line):
            acronym = match.group(1)

            # Skip if already seen or in skip list
            if acronym in seen_acronyms or acronym in SKIP_ACRONYMS:
                continue

            seen_acronyms.add(acronym)

            # Look up in database
            entry = acronym_db.get(acronym)

            if entry:
                # Check if deprecated
                if entry.deprecated:
                    issue_counter += 1
                    suggested = entry.full_name or entry.first_use or f"[use full name instead of {acronym}]"
                    issues.append(EditorialIssue(
                        id=f"{filename}-{issue_counter:03d}",
                        category=EditorialCategory.ACRONYM,
                        severity=FixSeverity.REVIEW,
                        line=line_num,
                        original=acronym,
                        suggested=suggested,
                        rule_id="ACRONYM_DEPRECATED",
                        rationale=entry.notes or f"'{acronym}' is deprecated"
                    ))
                elif not entry.well_known and not entry.skip_expansion:
                    # Check if expanded on this line
                    if f"({acronym})" not in line:
                        issue_counter += 1
                        suggested = entry.first_use or f"{entry.expansion} ({acronym})"
                        issues.append(EditorialIssue(
                            id=f"{filename}-{issue_counter:03d}",
                            category=EditorialCategory.ACRONYM,
                            severity=FixSeverity.REVIEW,
                            line=line_num,
                            original=acronym,
                            suggested=suggested,
                            rule_id="ACRONYM_FIRST_USE",
                            rationale=f"Expand '{acronym}' on first use"
                        ))
            else:
                # Unknown acronym - QUERY severity
                issue_counter += 1
                issues.append(EditorialIssue(
                    id=f"{filename}-{issue_counter:03d}",
                    category=EditorialCategory.ACRONYM,
                    severity=FixSeverity.QUERY,
                    line=line_num,
                    original=acronym,
                    suggested=f"[Please define '{acronym}']",
                    rule_id="ACRONYM_UNKNOWN",
                    rationale=f"Unknown acronym '{acronym}'. Please provide expansion."
                ))

    return issues, issue_counter


def validate_product_naming(content: str, filename: str, issue_counter: int) -> Tuple[List[EditorialIssue], int]:
    """
    Validate Cisco product naming compliance.

    Checks for:
    - Possessive forms of Cisco products (Cisco ASA's -> the Cisco ASA)
    - Deprecated product names

    Args:
        content: Text content to validate
        filename: Source filename for issue IDs
        issue_counter: Starting counter for issue IDs

    Returns:
        Tuple of (list of issues found, updated counter)
    """
    issues = []

    # Cisco product possessive pattern
    possessive_pattern = re.compile(r"Cisco\s+(\w+)'s\b")

    lines = content.split('\n')
    for line_num, line in enumerate(lines, 1):
        for match in possessive_pattern.finditer(line):
            issue_counter += 1
            original = match.group(0)
            product = match.group(1)
            issues.append(EditorialIssue(
                id=f"{filename}-{issue_counter:03d}",
                category=EditorialCategory.PRODUCT_NAMING,
                severity=FixSeverity.REVIEW,
                line=line_num,
                original=original,
                suggested=f"the Cisco {product}",
                rule_id="PROD_CISCO_POSSESSIVE",
                rationale="Avoid possessive forms of Cisco product names; rephrase instead"
            ))

    return issues, issue_counter


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


def validate_with_rules(
    topic_file: TopicFile,
    use_ai: bool = True,
    rules: Optional[List[EditorialRule]] = None,
    acronym_db: Optional[Dict[str, AcronymEntry]] = None
) -> EditorialResult:
    """
    Run editorial validation on preprocessed topic file content.

    Args:
        topic_file: TopicFile with clean_content populated
        use_ai: Whether to use AI enhancement (default: True)
        rules: Optional list of EditorialRule objects (loads from YAML if not provided)
        acronym_db: Optional acronym database (loads from JSON if not provided)

    Returns:
        EditorialResult with detected issues
    """
    issues = []
    issue_counter = 0

    # Load rules if not provided
    if rules is None:
        rules = load_editorial_rules()

    # Load acronym database if not provided
    if acronym_db is None:
        acronym_db = load_acronym_database()

    if rules:
        # Apply all loaded rules from editorial_rules.yaml
        for rule in rules:
            new_issues, issue_counter = apply_rule(
                rule,
                topic_file.clean_content,
                topic_file.filename,
                issue_counter
            )
            # Map line numbers back to original file
            for issue in new_issues:
                issue.line = map_line_number(issue.line, topic_file.components)
            issues.extend(new_issues)
    else:
        # Fallback: basic validation without full rules engine
        issues = _basic_validation(topic_file)

    # Run acronym validation (separate from YAML rules)
    if acronym_db:
        acronym_issues, issue_counter = validate_acronyms(
            topic_file.clean_content,
            acronym_db,
            topic_file.filename,
            issue_counter
        )
        # Map line numbers back to original file
        for issue in acronym_issues:
            issue.line = map_line_number(issue.line, topic_file.components)
        issues.extend(acronym_issues)

    # Run product naming validation
    product_issues, issue_counter = validate_product_naming(
        topic_file.clean_content,
        topic_file.filename,
        issue_counter
    )
    # Map line numbers back to original file
    for issue in product_issues:
        issue.line = map_line_number(issue.line, topic_file.components)
    issues.extend(product_issues)

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

    Preserves content inside LWC custom components - only fixes content in regular markdown.

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

    # Extract components to preserve them
    from component_skipper import extract_components, restore_components
    clean_content, components = extract_components(content)

    # Apply fixes to clean content only (components are protected)
    modified_content = clean_content

    # Group issues by rule_id to avoid duplicate fixes
    applied_rules = set()

    for issue in safe_issues:
        if issue.rule_id in applied_rules:
            continue

        original_modified = modified_content

        # Apply fix based on rule type
        if issue.rule_id == 'DOUBLE_SPACE' or issue.rule_id == 'PUNCT_DOUBLE_SPACE':
            # Replace multiple consecutive spaces with single space (not in code)
            modified_content = re.sub(r'(?<!`)  +(?!`)', ' ', modified_content)
        elif issue.rule_id == 'TRAILING_WHITESPACE' or issue.rule_id == 'PUNCT_TRAILING_SPACE':
            # Remove trailing whitespace from all lines
            lines = modified_content.split('\n')
            modified_content = '\n'.join(line.rstrip() for line in lines)
        elif issue.rule_id == 'TERM_CLICK_ON':
            modified_content = re.sub(r'\bclick on\b', 'click', modified_content, flags=re.I)
        elif issue.rule_id == 'TERM_IN_ORDER_TO':
            modified_content = re.sub(r'\bin order to\b', 'to', modified_content, flags=re.I)
        elif issue.rule_id == 'TERM_UTILIZE':
            modified_content = re.sub(r'\butilize[sd]?\b', 'use', modified_content, flags=re.I)
        elif issue.rule_id == 'TERM_ALLOWS_YOU_TO':
            modified_content = re.sub(r'\ballows you to\b', 'lets you', modified_content, flags=re.I)
        elif issue.rule_id == 'TERM_MAKE_SURE':
            modified_content = re.sub(r'\b[Mm]ake sure\b', 'ensure', modified_content)
        elif issue.rule_id == 'TERM_BLACKLIST':
            modified_content = re.sub(r'\bblacklist(?:ed|ing|s)?\b', 'blocked list', modified_content, flags=re.I)
        elif issue.rule_id == 'TERM_WHITELIST':
            modified_content = re.sub(r'\bwhitelist(?:ed|ing|s)?\b', 'allowed list', modified_content, flags=re.I)
        elif issue.rule_id == 'TERM_CISCO_SYSTEMS':
            modified_content = re.sub(r'\bCisco Systems\b', 'Cisco', modified_content)
        elif issue.rule_id == 'TERM_REFER_TO':
            modified_content = re.sub(r'\b[Rr]efer to\b', 'see', modified_content)
        elif issue.rule_id == 'TERM_DATACENTER':
            modified_content = re.sub(r'\bdata center\b', 'datacenter', modified_content, flags=re.I)
        elif issue.rule_id.startswith('GRAMMAR_COMPOUND_'):
            # Handle compound word hyphenation
            if 'WELL_KNOWN' in issue.rule_id:
                modified_content = re.sub(r'\bwell known\b', 'well-known', modified_content, flags=re.I)
            elif 'REAL_TIME' in issue.rule_id:
                modified_content = re.sub(r'\breal time\b', 'real-time', modified_content, flags=re.I)
            elif 'END_TO_END' in issue.rule_id:
                modified_content = re.sub(r'\bend to end\b', 'end-to-end', modified_content, flags=re.I)

        if modified_content != original_modified:
            fixes_applied += 1
            applied_rules.add(issue.rule_id)

    # Restore components back into the modified content
    final_content = restore_components(modified_content, components)

    # Write back to file if changes were made
    if final_content != topic_file.raw_content:
        topic_file.path.write_text(final_content, encoding='utf-8')
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
