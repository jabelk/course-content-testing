"""
Editorial Rules Engine - Fix Type Handlers

Implements the fix application logic for SAFE and REVIEW type issues.
QUERY type issues are never auto-fixed - they create author queries instead.

Fix Types:
    SAFE: Deterministic fix, auto-apply without review
          - High confidence (>95%)
          - Single valid replacement
          - No context dependency

    REVIEW: Apply fix but flag for human verification
          - Moderate confidence (70-95%)
          - May have multiple valid replacements
          - Requires context awareness

    QUERY: Don't fix, ask author for clarification
          - Low confidence (<70%)
          - Unknown terms or ambiguous situations
          - Requires author domain knowledge
"""
import re
from typing import List, Tuple, Optional
from editorial_models import EditorialIssue, EditorialRule


# =============================================================================
# SAFE Fix Handlers
# =============================================================================

def apply_safe_fix(issue: EditorialIssue, content: str) -> Tuple[str, bool]:
    """
    Apply a SAFE fix to content.

    SAFE fixes are deterministic and have high confidence.
    They are applied automatically without review.

    Args:
        issue: The EditorialIssue with the fix to apply
        content: The content to modify

    Returns:
        Tuple of (modified_content, was_applied)
    """
    if issue.fix_type != 'SAFE':
        return content, False

    if not issue.suggested_fix:
        return content, False

    # Handle specific rule IDs
    if issue.rule_id == 'PUNCT_EM_DASH_SPACE':
        return apply_em_dash_fix(issue, content)
    elif issue.rule_id == 'TERM_CLICK_ON':
        return apply_click_on_fix(issue, content)
    elif issue.rule_id == 'TERM_IN_ORDER_TO':
        return apply_in_order_to_fix(issue, content)
    elif issue.rule_id == 'TERM_UTILIZE':
        return apply_utilize_fix(issue, content)
    elif issue.rule_id == 'PUNCT_DOUBLE_EXCLAMATION':
        return apply_double_exclamation_fix(issue, content)
    elif issue.rule_id == 'PUNCT_DOUBLE_SPACE':
        return apply_double_space_fix(issue, content)
    elif issue.rule_id == 'TERM_ALLOWS_YOU_TO':
        return apply_allows_you_to_fix(issue, content)
    elif issue.rule_id == 'TERM_MAKE_SURE':
        return apply_make_sure_fix(issue, content)

    # Generic replacement
    return apply_generic_fix(issue, content)


def apply_em_dash_fix(issue: EditorialIssue, content: str) -> Tuple[str, bool]:
    """Remove spaces around em dashes."""
    lines = content.split('\n')
    line_idx = issue.line_number - 1

    if 0 <= line_idx < len(lines):
        line = lines[line_idx]
        # Replace various em dash spacing patterns
        new_line = re.sub(r'\s+—\s+', '—', line)
        new_line = re.sub(r'\s+—', '—', new_line)
        new_line = re.sub(r'—\s+', '—', new_line)

        if new_line != line:
            lines[line_idx] = new_line
            return '\n'.join(lines), True

    return content, False


def apply_click_on_fix(issue: EditorialIssue, content: str) -> Tuple[str, bool]:
    """Replace 'click on' with 'click'."""
    lines = content.split('\n')
    line_idx = issue.line_number - 1

    if 0 <= line_idx < len(lines):
        line = lines[line_idx]
        new_line = re.sub(r'\bclick on\b', 'click', line, flags=re.IGNORECASE)

        if new_line != line:
            lines[line_idx] = new_line
            return '\n'.join(lines), True

    return content, False


def apply_in_order_to_fix(issue: EditorialIssue, content: str) -> Tuple[str, bool]:
    """Replace 'in order to' with 'to'."""
    lines = content.split('\n')
    line_idx = issue.line_number - 1

    if 0 <= line_idx < len(lines):
        line = lines[line_idx]
        new_line = re.sub(r'\bin order to\b', 'to', line, flags=re.IGNORECASE)

        if new_line != line:
            lines[line_idx] = new_line
            return '\n'.join(lines), True

    return content, False


def apply_utilize_fix(issue: EditorialIssue, content: str) -> Tuple[str, bool]:
    """Replace 'utilize' with 'use'."""
    lines = content.split('\n')
    line_idx = issue.line_number - 1

    if 0 <= line_idx < len(lines):
        line = lines[line_idx]
        # Handle different forms: utilize, utilized, utilizes
        new_line = re.sub(r'\butilizes\b', 'uses', line)
        new_line = re.sub(r'\butilized\b', 'used', new_line)
        new_line = re.sub(r'\butilize\b', 'use', new_line)

        if new_line != line:
            lines[line_idx] = new_line
            return '\n'.join(lines), True

    return content, False


def apply_double_exclamation_fix(issue: EditorialIssue, content: str) -> Tuple[str, bool]:
    """Replace multiple exclamation points with single."""
    lines = content.split('\n')
    line_idx = issue.line_number - 1

    if 0 <= line_idx < len(lines):
        line = lines[line_idx]
        new_line = re.sub(r'!{2,}', '!', line)

        if new_line != line:
            lines[line_idx] = new_line
            return '\n'.join(lines), True

    return content, False


def apply_double_space_fix(issue: EditorialIssue, content: str) -> Tuple[str, bool]:
    """Replace double space after period with single space."""
    lines = content.split('\n')
    line_idx = issue.line_number - 1

    if 0 <= line_idx < len(lines):
        line = lines[line_idx]
        new_line = re.sub(r'\.  +', '. ', line)

        if new_line != line:
            lines[line_idx] = new_line
            return '\n'.join(lines), True

    return content, False


def apply_allows_you_to_fix(issue: EditorialIssue, content: str) -> Tuple[str, bool]:
    """Replace 'allows you to' with 'lets you'."""
    lines = content.split('\n')
    line_idx = issue.line_number - 1

    if 0 <= line_idx < len(lines):
        line = lines[line_idx]
        new_line = re.sub(r'\ballows you to\b', 'lets you', line, flags=re.IGNORECASE)

        if new_line != line:
            lines[line_idx] = new_line
            return '\n'.join(lines), True

    return content, False


def apply_make_sure_fix(issue: EditorialIssue, content: str) -> Tuple[str, bool]:
    """Replace 'make sure' with 'ensure'."""
    lines = content.split('\n')
    line_idx = issue.line_number - 1

    if 0 <= line_idx < len(lines):
        line = lines[line_idx]
        # Preserve case
        new_line = re.sub(r'\bMake sure\b', 'Ensure', line)
        new_line = re.sub(r'\bmake sure\b', 'ensure', new_line)

        if new_line != line:
            lines[line_idx] = new_line
            return '\n'.join(lines), True

    return content, False


def apply_generic_fix(issue: EditorialIssue, content: str) -> Tuple[str, bool]:
    """Apply a generic fix by replacing original text with suggested fix."""
    if not issue.suggested_fix or not issue.original_text:
        return content, False

    lines = content.split('\n')
    line_idx = issue.line_number - 1

    if 0 <= line_idx < len(lines):
        line = lines[line_idx]
        new_line = line.replace(issue.original_text, issue.suggested_fix, 1)

        if new_line != line:
            lines[line_idx] = new_line
            return '\n'.join(lines), True

    return content, False


# =============================================================================
# REVIEW Fix Handlers
# =============================================================================

def apply_review_fix(issue: EditorialIssue, content: str) -> Tuple[str, bool]:
    """
    Apply a REVIEW fix to content.

    REVIEW fixes have moderate confidence and are applied with
    a flag for human verification. The reviewer can revert if needed.

    Args:
        issue: The EditorialIssue with the fix to apply
        content: The content to modify

    Returns:
        Tuple of (modified_content, was_applied)
    """
    if issue.fix_type != 'REVIEW':
        return content, False

    if not issue.suggested_fix:
        return content, False

    # Handle specific rule IDs
    if issue.rule_id == 'HEADING_GERUND':
        return apply_gerund_heading_fix(issue, content)
    elif issue.rule_id == 'HEADING_HOW_TO':
        return apply_how_to_heading_fix(issue, content)
    elif issue.rule_id == 'PROD_CISCO_POSSESSIVE':
        return apply_cisco_possessive_fix(issue, content)
    elif issue.rule_id == 'ACRONYM_FIRST_USE':
        return apply_acronym_expansion_fix(issue, content)

    # Generic replacement for REVIEW items
    return apply_generic_fix(issue, content)


def apply_gerund_heading_fix(issue: EditorialIssue, content: str) -> Tuple[str, bool]:
    """
    Convert gerund heading to imperative form.

    Examples:
        "## Configuring VLANs" -> "## Configure VLANs"
        "## Installing the Agent" -> "## Install the Agent"
    """
    lines = content.split('\n')
    line_idx = issue.line_number - 1

    if 0 <= line_idx < len(lines):
        line = lines[line_idx]

        # Extract heading level and text
        match = re.match(r'^(#+\s+)(\w+ing)\b(.*)$', line)
        if match:
            prefix = match.group(1)
            gerund = match.group(2)
            suffix = match.group(3)

            # Convert gerund to imperative
            imperative = gerund_to_imperative(gerund)
            new_line = f"{prefix}{imperative}{suffix}"

            if new_line != line:
                lines[line_idx] = new_line
                return '\n'.join(lines), True

    return content, False


def gerund_to_imperative(gerund: str) -> str:
    """
    Convert a gerund verb to imperative form.

    Args:
        gerund: Word ending in -ing (e.g., "Configuring")

    Returns:
        Imperative form (e.g., "Configure")
    """
    if not gerund.endswith('ing'):
        return gerund

    # Preserve original case
    is_capitalized = gerund[0].isupper()
    base = gerund[:-3].lower()  # Remove 'ing'

    # Handle common patterns
    # Doubling: running -> run, stopping -> stop
    if len(base) >= 2 and base[-1] == base[-2] and base[-1] in 'bdfgklmnprstv':
        imperative = base[:-1]
    # e-ending: configuring -> configure, creating -> create
    elif base.endswith('at') or base.endswith('ur') or base.endswith('iz'):
        imperative = base + 'e'
    # y-ending: copying -> copy
    elif base.endswith('y'):
        imperative = base
    # Standard: installing -> install
    else:
        imperative = base

    # Restore capitalization
    if is_capitalized:
        imperative = imperative.capitalize()

    return imperative


def apply_how_to_heading_fix(issue: EditorialIssue, content: str) -> Tuple[str, bool]:
    """
    Remove "How to" from heading and use imperative form.

    Examples:
        "## How to Configure VLANs" -> "## Configure VLANs"
        "## How To Install the Agent" -> "## Install the Agent"
    """
    lines = content.split('\n')
    line_idx = issue.line_number - 1

    if 0 <= line_idx < len(lines):
        line = lines[line_idx]
        new_line = re.sub(r'^(#+\s+)[Hh]ow [Tt]o\s+', r'\1', line)

        if new_line != line:
            lines[line_idx] = new_line
            return '\n'.join(lines), True

    return content, False


def apply_cisco_possessive_fix(issue: EditorialIssue, content: str) -> Tuple[str, bool]:
    """
    Convert Cisco product possessive to "the [product]" form.

    Examples:
        "Cisco Hypershield's features" -> "the Cisco Hypershield features"
    """
    lines = content.split('\n')
    line_idx = issue.line_number - 1

    if 0 <= line_idx < len(lines):
        line = lines[line_idx]

        # Replace "Cisco Product's" with "the Cisco Product"
        def replace_possessive(match):
            product = match.group(1)
            return f"the Cisco {product}"

        new_line = re.sub(r"Cisco\s+(\w+)'s\b", replace_possessive, line)

        if new_line != line:
            lines[line_idx] = new_line
            return '\n'.join(lines), True

    return content, False


def apply_acronym_expansion_fix(issue: EditorialIssue, content: str) -> Tuple[str, bool]:
    """
    Add expansion for acronym on first use.

    Example:
        "VLAN" -> "virtual LAN (VLAN)"
    """
    if not issue.suggested_fix:
        return content, False

    lines = content.split('\n')
    line_idx = issue.line_number - 1

    if 0 <= line_idx < len(lines):
        line = lines[line_idx]

        # Replace first occurrence of the acronym with expanded form
        # Be careful not to replace inside code or already expanded
        acronym = issue.original_text
        expansion = issue.suggested_fix

        # Only replace if not already expanded
        if f"({acronym})" not in line:
            # Replace only if word boundary
            pattern = rf'\b{re.escape(acronym)}\b'
            new_line = re.sub(pattern, expansion, line, count=1)

            if new_line != line:
                lines[line_idx] = new_line
                return '\n'.join(lines), True

    return content, False


# =============================================================================
# Batch Fix Application
# =============================================================================

def apply_all_fixes(
    content: str,
    issues: List[EditorialIssue],
    apply_safe: bool = True,
    apply_review: bool = True
) -> Tuple[str, int]:
    """
    Apply all applicable fixes to content.

    Args:
        content: Original file content
        issues: List of issues to potentially fix
        apply_safe: Whether to apply SAFE fixes
        apply_review: Whether to apply REVIEW fixes

    Returns:
        Tuple of (modified_content, fixes_applied_count)
    """
    if not issues:
        return content, 0

    # Sort by line number descending to apply from bottom to top
    # This prevents line number shifts from affecting subsequent fixes
    sorted_issues = sorted(issues, key=lambda i: i.line_number, reverse=True)

    fixes_applied = 0
    modified_content = content

    for issue in sorted_issues:
        if issue.fix_type == 'SAFE' and apply_safe:
            modified_content, applied = apply_safe_fix(issue, modified_content)
            if applied:
                issue.applied = True
                fixes_applied += 1
        elif issue.fix_type == 'REVIEW' and apply_review:
            modified_content, applied = apply_review_fix(issue, modified_content)
            if applied:
                issue.applied = True
                fixes_applied += 1
        # QUERY fixes are never auto-applied

    return modified_content, fixes_applied
