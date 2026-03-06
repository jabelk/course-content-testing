#!/usr/bin/env python3
"""
Editorial Rules Engine - Main Validation Tool

A pluggable editorial validation system for Cisco U. tutorials that:
- Loads rules from YAML configuration
- Detects editorial issues using regex, stateful, and AI-enhanced patterns
- Classifies fixes as SAFE (auto-fix), REVIEW (flag for verification), or QUERY (ask author)
- Generates structured PR comments with quality scores

Usage:
    python editorial_validation.py <folder_path> [OPTIONS]

Options:
    --apply-fixes    Apply SAFE and REVIEW fixes to files
    --json-output    Output results as JSON
    --pr-comment     Output as PR comment markdown
    --no-ai          Disable AI enhancement
    --list-rules     List available rules and exit
    --verbose        Show detailed processing information
    --debug-rules    Show rule matching details

Examples:
    # Validate a tutorial (report only)
    python editorial_validation.py tutorials/tc-configure-vlans

    # Validate and apply fixes
    python editorial_validation.py tutorials/tc-configure-vlans --apply-fixes

    # Output as JSON for CI
    python editorial_validation.py tutorials/tc-configure-vlans --json-output
"""
import os
import re
import sys
import json
import time
import argparse
from pathlib import Path
from typing import List, Dict, Optional, Tuple

import yaml

from editorial_models import (
    EditorialRule,
    EditorialIssue,
    ValidationResult,
    QualityScore,
    AcronymState,
    PRCommentPayload,
    FixType,
    PatternType
)
from acronym_detector import AcronymDetector
from ai_editorial_client import get_ai_client, is_ai_available


# =============================================================================
# Configuration
# =============================================================================

RULES_FILE = 'editorial_rules.yaml'
ACRONYM_DB_FILE = '../.claude/references/acronym-database.json'
STYLE_RULES_FILE = 'cisco-style-rules.json'

# Contexts to skip for certain rules
CODE_BLOCK_PATTERN = re.compile(r'```[\s\S]*?```', re.MULTILINE)
INLINE_CODE_PATTERN = re.compile(r'`[^`]+`')
URL_PATTERN = re.compile(r'https?://[^\s\)]+')
FILE_PATH_PATTERN = re.compile(r'\./[^\s\)]+|\b[\w/-]+\.\w+')
# Quiz question pattern: line starting with number followed by period (e.g., "1. Which of the following...")
QUIZ_QUESTION_PATTERN = re.compile(r'^\s*\d+\.\s+', re.MULTILINE)
# Answer choice pattern: A. B. C. D. etc.
ANSWER_CHOICE_PATTERN = re.compile(r'^[A-F]\.\s+', re.MULTILINE)


# =============================================================================
# Rule Loading
# =============================================================================

def load_rules(rules_path: str) -> List[EditorialRule]:
    """
    Load editorial rules from YAML configuration file.

    Args:
        rules_path: Path to editorial_rules.yaml

    Returns:
        List of EditorialRule objects sorted by priority
    """
    if not os.path.exists(rules_path):
        print(f"Warning: Rules file not found: {rules_path}", file=sys.stderr)
        return []

    with open(rules_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    if not data or 'rules' not in data:
        print(f"Warning: No rules found in {rules_path}", file=sys.stderr)
        return []

    rules = []
    for rule_data in data['rules']:
        if rule_data.get('enabled', True):
            try:
                rule = EditorialRule.from_dict(rule_data)
                rules.append(rule)
            except (KeyError, TypeError) as e:
                print(f"Warning: Invalid rule definition: {e}", file=sys.stderr)

    # Sort by priority (lower = higher priority)
    rules.sort(key=lambda r: r.priority)
    return rules


def load_acronym_database(db_path: str) -> Dict[str, dict]:
    """
    Load acronym database from JSON file.

    Args:
        db_path: Path to acronym-database.json

    Returns:
        Dictionary mapping acronyms to their entries
    """
    if not os.path.exists(db_path):
        print(f"Warning: Acronym database not found: {db_path}", file=sys.stderr)
        return {}

    with open(db_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Handle both list and dict formats
    if isinstance(data, list):
        return {entry['acronym']: entry for entry in data if 'acronym' in entry}
    elif isinstance(data, dict):
        if 'acronyms' in data:
            return {entry['acronym']: entry for entry in data['acronyms'] if 'acronym' in entry}
        return data
    return {}


# =============================================================================
# Content Parsing
# =============================================================================

def extract_text_regions(content: str) -> List[Tuple[int, int, str]]:
    """
    Extract text regions that should be validated, excluding code blocks.

    Args:
        content: Full file content

    Returns:
        List of (start_offset, end_offset, text) tuples for non-code regions
    """
    regions = []
    last_end = 0

    # Find all code blocks and exclude them
    for match in CODE_BLOCK_PATTERN.finditer(content):
        if match.start() > last_end:
            text = content[last_end:match.start()]
            regions.append((last_end, match.start(), text))
        last_end = match.end()

    # Add remaining content after last code block
    if last_end < len(content):
        regions.append((last_end, len(content), content[last_end:]))

    return regions


def get_line_number(content: str, offset: int) -> int:
    """Get 1-indexed line number for a given offset in content."""
    return content[:offset].count('\n') + 1


def should_skip_context(match_text: str, line: str, skip_contexts: List[str]) -> bool:
    """
    Check if match should be skipped based on context.

    Args:
        match_text: The matched text
        line: The full line containing the match
        skip_contexts: List of contexts to skip ('code_block', 'inline_code', 'url', 'file_path', 'quiz_question')

    Returns:
        True if match should be skipped
    """
    if 'inline_code' in skip_contexts:
        # Check if match is inside inline code
        for code_match in INLINE_CODE_PATTERN.finditer(line):
            if match_text in code_match.group():
                return True

    if 'url' in skip_contexts:
        # Check if match is inside a URL
        for url_match in URL_PATTERN.finditer(line):
            if match_text in url_match.group():
                return True

    if 'file_path' in skip_contexts:
        # Check if match is inside a file path
        for path_match in FILE_PATH_PATTERN.finditer(line):
            if match_text in path_match.group():
                return True

    if 'quiz_question' in skip_contexts:
        # Check if line is a quiz question (starts with number.) or answer choice (starts with A. B. etc.)
        if QUIZ_QUESTION_PATTERN.match(line) or ANSWER_CHOICE_PATTERN.match(line.strip()):
            return True

    return False


# =============================================================================
# Duplicate Detection
# =============================================================================

def detect_duplicate_paragraphs(content: str, file_path: str, min_words: int = 15) -> List[EditorialIssue]:
    """
    Detect duplicate or near-duplicate paragraphs in content.

    Args:
        content: File content to analyze
        file_path: Relative path to the file
        min_words: Minimum word count to consider for duplication

    Returns:
        List of EditorialIssue objects for duplicate content found
    """
    issues = []

    # Split into paragraphs (blank line separated)
    paragraphs = re.split(r'\n\s*\n', content)

    # Normalize paragraphs for comparison
    def normalize(text: str) -> str:
        """Normalize text for comparison (lowercase, single spaces, strip)."""
        text = re.sub(r'\s+', ' ', text.lower().strip())
        # Remove markdown formatting for comparison
        text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)  # bold
        text = re.sub(r'\*([^*]+)\*', r'\1', text)      # italic
        text = re.sub(r'`([^`]+)`', r'\1', text)        # inline code
        return text

    # Track seen paragraphs with their first occurrence line
    seen_paragraphs = {}  # normalized_text -> (original_text, first_line_num)

    current_line = 1
    for para in paragraphs:
        if not para.strip():
            current_line += 1
            continue

        # Skip code blocks
        if para.strip().startswith('```'):
            current_line += para.count('\n') + 2
            continue

        # Skip very short paragraphs
        word_count = len(para.split())
        if word_count < min_words:
            current_line += para.count('\n') + 2
            continue

        normalized = normalize(para)

        if normalized in seen_paragraphs:
            first_text, first_line = seen_paragraphs[normalized]

            # Create issue for duplicate
            issue = EditorialIssue(
                rule_id='CONTENT_DUPLICATE_PARAGRAPH',
                file_path=file_path,
                line_number=current_line,
                original_text=para[:100] + ('...' if len(para) > 100 else ''),
                fix_type='REVIEW',
                message=f"Duplicate paragraph (first appears at line {first_line})",
                confidence=0.95,
                suggested_fix="Consider removing this duplicate paragraph",
                context_before="",
                context_after="",
                absolute_offset=0
            )
            issues.append(issue)
        else:
            seen_paragraphs[normalized] = (para, current_line)

        current_line += para.count('\n') + 2

    return issues


# =============================================================================
# Rule Execution
# =============================================================================

def get_context(content: str, start: int, end: int, context_chars: int = 25) -> tuple:
    """
    Extract context before and after a match position.

    Args:
        content: Full content
        start: Start offset of match
        end: End offset of match
        context_chars: Number of characters of context to capture

    Returns:
        Tuple of (context_before, context_after)
    """
    # Get context before (up to context_chars, but stop at newline)
    ctx_start = max(0, start - context_chars)
    before = content[ctx_start:start]
    # Find last newline in before and trim
    last_nl = before.rfind('\n')
    if last_nl != -1:
        before = before[last_nl + 1:]

    # Get context after (up to context_chars, but stop at newline)
    ctx_end = min(len(content), end + context_chars)
    after = content[end:ctx_end]
    # Find first newline in after and trim
    first_nl = after.find('\n')
    if first_nl != -1:
        after = after[:first_nl]

    return before.strip(), after.strip()


def apply_regex_rule(
    rule: EditorialRule,
    content: str,
    file_path: str,
    verbose: bool = False
) -> List[EditorialIssue]:
    """
    Apply a regex-based rule to content.

    Args:
        rule: The EditorialRule to apply
        content: File content to validate
        file_path: Relative path to the file
        verbose: Show detailed matching info

    Returns:
        List of EditorialIssue objects for matches found
    """
    if not rule.pattern:
        return []

    issues = []
    try:
        pattern = re.compile(rule.pattern, re.MULTILINE)
    except re.error as e:
        print(f"Warning: Invalid regex pattern in rule {rule.id}: {e}", file=sys.stderr)
        return []

    # Extract non-code regions
    regions = extract_text_regions(content)
    lines = content.split('\n')

    for start_offset, end_offset, region_text in regions:
        for match in pattern.finditer(region_text):
            absolute_offset = start_offset + match.start()
            absolute_end = start_offset + match.end()
            line_num = get_line_number(content, absolute_offset)
            line = lines[line_num - 1] if line_num <= len(lines) else ''
            match_text = match.group()

            # Check context skip conditions
            if should_skip_context(match_text, line, rule.context_skip):
                if verbose:
                    print(f"  Skipping {rule.id} match at line {line_num}: context skip")
                continue

            # Generate suggested fix
            suggested_fix = generate_suggestion(rule, match_text)

            # Calculate confidence based on fix type
            confidence = 0.99 if rule.fix_type == 'SAFE' else 0.85 if rule.fix_type == 'REVIEW' else 0.5

            # Get surrounding context for locating in original document
            context_before, context_after = get_context(content, absolute_offset, absolute_end)

            issue = EditorialIssue(
                rule_id=rule.id,
                file_path=file_path,
                line_number=line_num,
                original_text=match_text,
                fix_type=rule.fix_type,
                message=rule.message.replace('{match}', match_text),
                confidence=confidence,
                suggested_fix=suggested_fix,
                column_start=match.start(),
                column_end=match.end(),
                context_before=context_before,
                context_after=context_after,
                absolute_offset=absolute_offset
            )
            issues.append(issue)

            if verbose:
                print(f"  Found {rule.id} at line {line_num}: '{match_text}'")

    return issues


def generate_suggestion(rule: EditorialRule, match_text: str) -> Optional[str]:
    """
    Generate a suggested fix based on the rule and matched text.

    For simple replacements, applies the pattern's replacement.
    For complex rules, returns a template suggestion.
    """
    # Handle specific rule patterns
    if rule.id == 'PUNCT_EM_DASH_SPACE':
        return match_text.replace(' — ', '—').replace(' —', '—').replace('— ', '—')
    elif rule.id == 'PUNCT_DOUBLE_HYPHEN':
        return match_text.replace('--', '—')
    elif rule.id == 'PUNCT_DOUBLE_EXCLAMATION':
        return '!'
    elif rule.id == 'PUNCT_MULTIPLE_QUESTION':
        return '?'
    elif rule.id == 'PUNCT_TRAILING_SPACE':
        return ''
    elif rule.id == 'PUNCT_DOUBLE_SPACE':
        return '. '
    elif rule.id == 'TERM_CLICK_ON':
        return re.sub(r'\bclick on\b', 'click', match_text, flags=re.IGNORECASE)
    elif rule.id == 'TERM_IN_ORDER_TO':
        return re.sub(r'\bin order to\b', 'to', match_text, flags=re.IGNORECASE)
    elif rule.id == 'TERM_UTILIZE':
        result = re.sub(r'\butilizes\b', 'uses', match_text)
        result = re.sub(r'\butilized\b', 'used', result)
        result = re.sub(r'\butilize\b', 'use', result)
        return result
    elif rule.id == 'TERM_MAKE_SURE':
        result = re.sub(r'\bMake sure\b', 'Ensure', match_text)
        result = re.sub(r'\bmake sure\b', 'ensure', result)
        return result
    elif rule.id == 'TERM_ALLOWS_YOU_TO':
        return re.sub(r'\ballows you to\b', 'lets you', match_text, flags=re.IGNORECASE)
    elif rule.id == 'TERM_BLACKLIST':
        result = re.sub(r'\bblacklisted\b', 'blocked', match_text, flags=re.IGNORECASE)
        result = re.sub(r'\bblacklisting\b', 'blocking', result, flags=re.IGNORECASE)
        result = re.sub(r'\bblacklists\b', 'blocked lists', result, flags=re.IGNORECASE)
        result = re.sub(r'\bblacklist\b', 'blocked list', result, flags=re.IGNORECASE)
        return result
    elif rule.id == 'TERM_WHITELIST':
        result = re.sub(r'\bwhitelisted\b', 'allowed', match_text, flags=re.IGNORECASE)
        result = re.sub(r'\bwhitelisting\b', 'allowing', result, flags=re.IGNORECASE)
        result = re.sub(r'\bwhitelists\b', 'allowed lists', result, flags=re.IGNORECASE)
        result = re.sub(r'\bwhitelist\b', 'allowed list', result, flags=re.IGNORECASE)
        return result
    elif rule.id == 'TERM_EG':
        return re.sub(r'\be\.g\.\s', 'for example, ', match_text)
    elif rule.id == 'TERM_IE':
        return re.sub(r'\bi\.e\.\s', 'that is, ', match_text)
    elif rule.id == 'TERM_ETC':
        return re.sub(r'\betc\.', 'and so on', match_text)
    elif rule.id == 'TERM_PRIOR_TO':
        return re.sub(r'\bprior to\b', 'before', match_text, flags=re.IGNORECASE)
    elif rule.id == 'TERM_LEVERAGE':
        result = re.sub(r'\bleverages\b', 'uses', match_text)
        result = re.sub(r'\bleveraged\b', 'used', result)
        result = re.sub(r'\bleverage\b', 'use', result)
        return result
    elif rule.id == 'TERM_INITIATE':
        result = re.sub(r'\binitiates\b', 'starts', match_text)
        result = re.sub(r'\binitiated\b', 'started', result)
        result = re.sub(r'\binitiate\b', 'start', result)
        return result
    elif rule.id == 'TERM_DATACENTER':
        return re.sub(r'\bdatacenter\b', 'data center', match_text, flags=re.IGNORECASE)
    elif rule.id == 'TERM_HOTSPOT':
        return re.sub(r'\bhot spot\b', 'hotspot', match_text, flags=re.IGNORECASE)
    elif rule.id == 'TERM_GRAYED_OUT':
        return re.sub(r'\bgrayed out\b', 'dimmed', match_text, flags=re.IGNORECASE)
    elif rule.id == 'TERM_LEFT_HAND':
        return re.sub(r'\bleft-hand\b', 'left', match_text, flags=re.IGNORECASE)
    elif rule.id == 'TERM_RIGHT_HAND':
        return re.sub(r'\bright-hand\b', 'right', match_text, flags=re.IGNORECASE)
    elif rule.id == 'TERM_BOOT_UP':
        return re.sub(r'\bboot up\b', 'start', match_text, flags=re.IGNORECASE)
    elif rule.id == 'TERM_CISCO_SYSTEMS':
        return re.sub(r'\bCisco Systems\b', 'Cisco', match_text)
    elif rule.id == 'TERM_DESIRE':
        result = re.sub(r'\bdesires\b', 'wants', match_text)
        result = re.sub(r'\bdesired\b', 'wanted', result)
        result = re.sub(r'\bdesire\b', 'want', result)
        return result
    # New rules from Kim's Circuit comparison
    elif rule.id == 'TERM_DIFFERENT_THAN':
        return re.sub(r'\bdifferent than\b', 'different from', match_text, flags=re.IGNORECASE)
    elif rule.id == 'TERM_REFER_TO':
        result = re.sub(r'\bRefer to\b', 'See', match_text)
        result = re.sub(r'\brefer to\b', 'see', result)
        return result
    elif rule.id == 'TERM_DROPDOWN_MENU':
        return re.sub(r'\bdrop-?down menu\b', 'drop-down list', match_text, flags=re.IGNORECASE)
    elif rule.id == 'TERM_TABLE_BELOW':
        # Transform "table below" to "following table"
        result = re.sub(r'\b(table|figure|diagram|image|screenshot)\s+below\b',
                       r'following \1', match_text, flags=re.IGNORECASE)
        return result
    elif rule.id == 'TERM_DUE_TO':
        return re.sub(r'\bdue to\b', 'because of', match_text, flags=re.IGNORECASE)
    elif rule.id == 'TERM_WISH_TO':
        return re.sub(r'\bwish to\b', 'want to', match_text, flags=re.IGNORECASE)
    elif rule.id == 'TERM_RUNTIME':
        return re.sub(r'\brun time\b', 'runtime', match_text, flags=re.IGNORECASE)
    elif rule.id == 'TERM_CHECKBOX':
        return re.sub(r'\bcheckbox\b', 'check box', match_text, flags=re.IGNORECASE)
    elif rule.id == 'TERM_USERID':
        result = re.sub(r'\buserid\b', 'user ID', match_text, flags=re.IGNORECASE)
        result = re.sub(r'\buser-id\b', 'user ID', result, flags=re.IGNORECASE)
        return result
    elif rule.id == 'HEADING_GERUND':
        # Try to convert gerund to imperative (remove -ing, add appropriate ending)
        words = match_text.split()
        if len(words) >= 2 and words[1].endswith('ing'):
            gerund = words[1]
            # Common transformations
            if gerund.endswith('ting'):
                imperative = gerund[:-4] + 't'
            elif gerund.endswith('ning'):
                imperative = gerund[:-4] + 'n'
            elif gerund.endswith('ring'):
                imperative = gerund[:-4] + 'r'
            elif gerund.endswith('ling'):
                imperative = gerund[:-4] + 'l'
            elif gerund.endswith('ying'):
                imperative = gerund[:-4] + 'y'
            elif gerund.endswith('ing'):
                imperative = gerund[:-3] + 'e' if gerund[-4] not in 'aeiou' else gerund[:-3]
            else:
                imperative = gerund[:-3]
            words[1] = imperative.capitalize() if words[1][0].isupper() else imperative
            return ' '.join(words)

    # Default: return the suggestion template with placeholder replaced
    return rule.suggestion_template.replace('{original}', match_text)


# =============================================================================
# Fix Application
# =============================================================================

def apply_fixes(
    content: str,
    issues: List[EditorialIssue],
    apply_safe: bool = True,
    apply_review: bool = True
) -> Tuple[str, int]:
    """
    Apply fixes to content based on issues.

    Args:
        content: Original file content
        issues: List of issues to potentially fix
        apply_safe: Apply SAFE fixes
        apply_review: Apply REVIEW fixes

    Returns:
        Tuple of (modified_content, fixes_applied_count)
    """
    if not issues:
        return content, 0

    # Sort issues by position (reverse order to apply from end to start)
    # This prevents offset issues when applying multiple fixes
    sorted_issues = sorted(
        issues,
        key=lambda i: (i.line_number, i.column_start),
        reverse=True
    )

    lines = content.split('\n')
    fixes_applied = 0

    for issue in sorted_issues:
        # Check if we should apply this fix
        if issue.fix_type == 'SAFE' and not apply_safe:
            continue
        if issue.fix_type == 'REVIEW' and not apply_review:
            continue
        if issue.fix_type == 'QUERY':
            continue  # Never auto-fix QUERY issues
        if not issue.suggested_fix:
            continue

        line_idx = issue.line_number - 1
        if 0 <= line_idx < len(lines):
            line = lines[line_idx]
            # Replace the matched text with the suggested fix
            new_line = line.replace(issue.original_text, issue.suggested_fix, 1)
            if new_line != line:
                lines[line_idx] = new_line
                issue.applied = True
                fixes_applied += 1

    return '\n'.join(lines), fixes_applied


# =============================================================================
# File Processing
# =============================================================================

def get_step_files(folder_path: str) -> List[str]:
    """
    Get list of step-*.md files in a tutorial folder, sorted by step number.

    Args:
        folder_path: Path to tutorial folder (tc-*)

    Returns:
        List of file paths sorted by step number
    """
    step_files = []
    for filename in os.listdir(folder_path):
        if filename.startswith('step-') and filename.endswith('.md'):
            step_files.append(os.path.join(folder_path, filename))

    # Sort by step number
    def get_step_number(path):
        filename = os.path.basename(path)
        try:
            return int(filename.replace('step-', '').replace('.md', ''))
        except ValueError:
            return 999

    step_files.sort(key=get_step_number)
    return step_files


def validate_file(
    file_path: str,
    rules: List[EditorialRule],
    acronym_state: Dict[str, AcronymState],
    verbose: bool = False,
    use_ai: bool = True
) -> List[EditorialIssue]:
    """
    Validate a single markdown file against editorial rules.

    Args:
        file_path: Path to the markdown file
        rules: List of EditorialRule objects to apply
        acronym_state: Shared acronym state across files
        verbose: Show detailed processing info
        use_ai: Whether to use AI enhancement

    Returns:
        List of EditorialIssue objects found
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    relative_path = os.path.basename(file_path)
    all_issues = []

    for rule in rules:
        if rule.pattern_type == 'regex':
            issues = apply_regex_rule(rule, content, relative_path, verbose)
            all_issues.extend(issues)
        elif rule.pattern_type == 'stateful':
            # Stateful rules (like acronyms) handled separately
            pass
        elif rule.pattern_type == 'ai_enhanced':
            # AI-enhanced rules with graceful fallback
            issues = apply_ai_rule(rule, content, relative_path, use_ai, verbose)
            all_issues.extend(issues)

    return all_issues


def apply_ai_rule(
    rule: EditorialRule,
    content: str,
    file_path: str,
    use_ai: bool = True,
    verbose: bool = False
) -> List[EditorialIssue]:
    """
    Apply an AI-enhanced rule to content.

    Falls back to QUERY fix type if AI is unavailable.

    Args:
        rule: The EditorialRule to apply
        content: File content to validate
        file_path: Relative path to the file
        use_ai: Whether to use AI enhancement
        verbose: Show detailed matching info

    Returns:
        List of EditorialIssue objects for matches found
    """
    issues = []

    # First, find potential matches using the pattern (if any)
    if not rule.pattern:
        return issues

    try:
        pattern = re.compile(rule.pattern, re.MULTILINE)
    except re.error as e:
        print(f"Warning: Invalid regex pattern in rule {rule.id}: {e}", file=sys.stderr)
        return issues

    # Extract non-code regions
    regions = extract_text_regions(content)
    lines = content.split('\n')

    # Check if AI is available and enabled
    ai_available = use_ai and is_ai_available()

    for start_offset, end_offset, region_text in regions:
        for match in pattern.finditer(region_text):
            absolute_offset = start_offset + match.start()
            absolute_end = start_offset + match.end()
            line_num = get_line_number(content, absolute_offset)
            line = lines[line_num - 1] if line_num <= len(lines) else ''
            match_text = match.group()

            # Check context skip conditions
            if should_skip_context(match_text, line, rule.context_skip):
                if verbose:
                    print(f"  Skipping {rule.id} match at line {line_num}: context skip")
                continue

            # Get surrounding context for locating in original document
            context_before, context_after = get_context(content, absolute_offset, absolute_end)

            if ai_available:
                # Use AI for intelligent suggestion
                ai_response = _get_ai_suggestion(rule, content, line_num, match_text, verbose)
                if ai_response:
                    issue = EditorialIssue(
                        rule_id=rule.id,
                        file_path=file_path,
                        line_number=line_num,
                        original_text=match_text,
                        fix_type='REVIEW',
                        message=rule.message.replace('{match}', match_text),
                        confidence=ai_response.confidence,
                        suggested_fix=ai_response.suggestion,
                        context_before=context_before,
                        context_after=context_after,
                        absolute_offset=absolute_offset
                    )
                    issues.append(issue)
                    if verbose:
                        cached_str = " (cached)" if ai_response.cached else ""
                        print(f"  AI suggestion for {rule.id} at line {line_num}{cached_str}: {ai_response.suggestion}")
            else:
                # Fall back to QUERY - ask author
                issue = EditorialIssue(
                    rule_id=rule.id,
                    file_path=file_path,
                    line_number=line_num,
                    original_text=match_text,
                    fix_type='QUERY',  # Downgrade to QUERY when AI unavailable
                    message=f"{rule.message.replace('{match}', match_text)} (AI unavailable - manual review needed)",
                    confidence=0.5,
                    suggested_fix=None,
                    context_before=context_before,
                    context_after=context_after,
                    absolute_offset=absolute_offset
                )
                issues.append(issue)
                if verbose:
                    print(f"  {rule.id} at line {line_num}: AI unavailable, created QUERY")

    return issues


def _get_ai_suggestion(
    rule: EditorialRule,
    content: str,
    line_num: int,
    match_text: str,
    verbose: bool
):
    """
    Get AI suggestion for a specific rule and match.

    Returns AIResponse or None.
    """
    from ai_editorial_client import AIResponse

    ai_client = get_ai_client()

    # Get context around the match (5 lines before and after)
    lines = content.split('\n')
    start_line = max(0, line_num - 6)
    end_line = min(len(lines), line_num + 5)
    context = '\n'.join(lines[start_line:end_line])

    if rule.id == 'AI_PROCEDURAL_INTRO':
        return ai_client.analyze_procedural_intro(context, "", line_num)
    elif rule.id == 'HEADING_GERUND' and rule.pattern_type == 'ai_enhanced':
        return ai_client.analyze_heading_conversion(match_text, context)

    # Generic fallback - return None to skip AI analysis
    return None


def validate_tutorial(
    folder_path: str,
    rules: List[EditorialRule],
    apply_fixes_flag: bool = False,
    use_ai: bool = True,
    verbose: bool = False
) -> ValidationResult:
    """
    Validate all step files in a tutorial folder.

    Args:
        folder_path: Path to tutorial folder (tc-*)
        rules: List of EditorialRule objects
        apply_fixes_flag: Whether to apply fixes to files
        use_ai: Whether to use AI enhancement
        verbose: Show detailed processing info

    Returns:
        ValidationResult with all issues and metadata
    """
    start_time = time.time()

    result = ValidationResult(
        tutorial_folder=os.path.basename(folder_path),
        ai_available=use_ai
    )

    step_files = get_step_files(folder_path)
    if not step_files:
        print(f"Warning: No step files found in {folder_path}", file=sys.stderr)
        return result

    result.rules_applied = [r.id for r in rules]

    # Get tutorial title from sidecar.json if available
    tutorial_title = ""
    sidecar_path = os.path.join(folder_path, 'sidecar.json')
    if os.path.exists(sidecar_path):
        try:
            with open(sidecar_path, 'r', encoding='utf-8') as f:
                sidecar = json.load(f)
                tutorial_title = sidecar.get('title', '')
        except (json.JSONDecodeError, IOError):
            pass

    # Initialize acronym detector for stateful tracking across files
    script_dir = os.path.dirname(os.path.abspath(__file__))
    acronym_db_path = os.path.join(script_dir, ACRONYM_DB_FILE)
    acronym_detector = AcronymDetector(acronym_db_path)

    for file_path in step_files:
        if verbose:
            print(f"Processing: {file_path}")

        result.files_processed.append(os.path.basename(file_path))

        # Read file content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        relative_path = os.path.basename(file_path)

        # Validate file with regex rules
        issues = validate_file(file_path, rules, {}, verbose, use_ai)

        # Run duplicate paragraph detection
        duplicate_issues = detect_duplicate_paragraphs(content, relative_path)
        issues.extend(duplicate_issues)
        if verbose and duplicate_issues:
            print(f"  Found {len(duplicate_issues)} duplicate paragraph(s)")

        # Run acronym detection (stateful across files)
        acronym_issues, _ = acronym_detector.detect_acronyms(
            content=content,
            file_path=relative_path,
            tutorial_title=tutorial_title,
            verbose=verbose
        )
        issues.extend(acronym_issues)

        for issue in issues:
            result.add_issue(issue)

        # Apply fixes if requested
        if apply_fixes_flag and issues:
            new_content, fixes_count = apply_fixes(content, issues)
            if fixes_count > 0:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                result.fixes_applied += fixes_count

    result.acronym_state = acronym_detector.state
    result.processing_time_ms = int((time.time() - start_time) * 1000)
    result.calculate_score()

    return result


# =============================================================================
# Output Formatting
# =============================================================================

def format_console_output(result: ValidationResult) -> str:
    """Format validation result for console output."""
    lines = []
    lines.append(f"\nEditorial Validation Report: {result.tutorial_folder}")
    lines.append("=" * 60)
    lines.append("")

    if result.quality_score:
        lines.append(f"Quality Score: {result.quality_score.score}/10 ({result.quality_score.interpretation})")
        lines.append("")

    by_type = result.get_issues_by_type()

    # Auto-Fixed (SAFE)
    safe_issues = by_type['SAFE']
    if safe_issues:
        applied = [i for i in safe_issues if i.applied]
        lines.append(f"Auto-Fixed (SAFE): {len(applied)} items")
        lines.append("-" * 40)
        for issue in applied:
            lines.append(f"  ✓ {issue.file_path}:{issue.line_number} - \"{issue.original_text}\" → \"{issue.suggested_fix}\"")
        lines.append("")

    # Review Needed (REVIEW)
    review_issues = by_type['REVIEW']
    if review_issues:
        lines.append(f"Review Needed (REVIEW): {len(review_issues)} items")
        lines.append("-" * 40)
        for issue in review_issues:
            status = "✓" if issue.applied else "⚠"
            lines.append(f"  {status} {issue.file_path}:{issue.line_number} - {issue.message}")
            if issue.suggested_fix:
                lines.append(f"      Suggestion: \"{issue.original_text}\" → \"{issue.suggested_fix}\"")
        lines.append("")

    # Queries for Author (QUERY)
    query_issues = by_type['QUERY']
    if query_issues:
        lines.append(f"Queries for Author (QUERY): {len(query_issues)} items")
        lines.append("-" * 40)
        for issue in query_issues:
            lines.append(f"  ? {issue.file_path}:{issue.line_number} - {issue.message}")
        lines.append("")

    # Summary
    lines.append(f"Files processed: {len(result.files_processed)} | Time: {result.processing_time_ms/1000:.1f}s | AI: {'enabled' if result.ai_available else 'disabled'}")

    return '\n'.join(lines)


def format_json_output(result: ValidationResult) -> str:
    """Format validation result as JSON."""
    return json.dumps(result.to_dict(), indent=2)


# =============================================================================
# CLI Entry Point
# =============================================================================

def main():
    """Main entry point for editorial validation."""
    parser = argparse.ArgumentParser(
        description='Editorial Rules Engine - Validate Cisco U. tutorials for editorial style compliance',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    parser.add_argument(
        'folder_path',
        nargs='?',
        help='Path to tutorial folder (tc-*)'
    )
    parser.add_argument(
        '--apply-fixes',
        action='store_true',
        help='Apply SAFE and REVIEW fixes to files'
    )
    parser.add_argument(
        '--json-output',
        action='store_true',
        help='Output results as JSON'
    )
    parser.add_argument(
        '--pr-comment',
        action='store_true',
        help='Output as PR comment markdown'
    )
    parser.add_argument(
        '--no-ai',
        action='store_true',
        help='Disable AI enhancement'
    )
    parser.add_argument(
        '--list-rules',
        action='store_true',
        help='List available rules and exit'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed processing information'
    )
    parser.add_argument(
        '--debug-rules',
        action='store_true',
        help='Show rule matching details'
    )

    args = parser.parse_args()

    # Determine rules file path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    rules_path = os.path.join(script_dir, RULES_FILE)

    # Load rules
    rules = load_rules(rules_path)

    # List rules mode
    if args.list_rules:
        print(f"\nAvailable Editorial Rules ({len(rules)} rules loaded):")
        print("=" * 60)
        for rule in rules:
            status = "✓" if rule.enabled else "✗"
            print(f"  [{status}] {rule.id}: {rule.name}")
            print(f"       Category: {rule.category} | Severity: {rule.severity} | Fix: {rule.fix_type}")
        return 0

    # Require folder path for validation
    if not args.folder_path:
        parser.print_help()
        return 1

    folder_path = args.folder_path
    if not os.path.isdir(folder_path):
        print(f"Error: Not a valid directory: {folder_path}", file=sys.stderr)
        return 1

    # Run validation
    result = validate_tutorial(
        folder_path=folder_path,
        rules=rules,
        apply_fixes_flag=args.apply_fixes,
        use_ai=not args.no_ai,
        verbose=args.verbose or args.debug_rules
    )

    # Output results
    if args.json_output:
        print(format_json_output(result))
    elif args.pr_comment:
        # Import PR comment generator when needed
        try:
            from pr_comment_editorial import generate_pr_comment
            print(generate_pr_comment(result))
        except ImportError:
            print("Error: pr_comment_editorial module not found", file=sys.stderr)
            print(format_console_output(result))
    else:
        print(format_console_output(result))

    # Exit with error code if there are unfixed issues
    if result.quality_score and result.quality_score.query_count > 0:
        return 0  # Advisory only - don't fail on queries
    return 0


if __name__ == '__main__':
    sys.exit(main())
