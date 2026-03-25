"""
Component Skipper - Extract and restore LWC custom components for editorial validation.

Provides functions to:
- Extract custom components from markdown, replacing with placeholders
- Restore original components after editorial processing
- Strip directive markers from content
- Map line numbers between clean and original text
"""

import logging
import re
from dataclasses import dataclass, field
from typing import List, Tuple, Optional

from lwc_constants import COMPONENT_NAMES, MARKERS

# Configure logging
logger = logging.getLogger(__name__)


@dataclass
class ComponentBlock:
    """Represents an extracted custom component."""
    type: str           # Component name (e.g., 'CustomNote')
    start_line: int     # Starting line in original file (1-indexed)
    end_line: int       # Ending line in original file (1-indexed)
    raw_content: str    # Full component including tags
    inner_content: str  # Content between opening/closing tags
    placeholder: str    # Replacement placeholder string
    is_malformed: bool = False  # True if component had parsing issues


@dataclass
class ExtractionResult:
    """Result of component extraction with warnings."""
    clean_text: str
    components: List[ComponentBlock]
    warnings: List[str] = field(default_factory=list)


def extract_components(markdown: str, strict: bool = False) -> Tuple[str, List[ComponentBlock]]:
    """
    Extract all custom components from markdown content.

    Args:
        markdown: Raw markdown string with embedded components
        strict: If True, raise exception on malformed components

    Returns:
        Tuple of (clean_text, components):
        - clean_text: Markdown with components replaced by placeholders
        - components: List of extracted ComponentBlock objects

    Note:
        Malformed components (unclosed tags) are kept as-is and logged.
        Use extract_components_with_warnings() for detailed error info.
    """
    result = extract_components_with_warnings(markdown, strict)
    return result.clean_text, result.components


def extract_components_with_warnings(
    markdown: str,
    strict: bool = False
) -> ExtractionResult:
    """
    Extract all custom components with detailed warnings.

    Args:
        markdown: Raw markdown string with embedded components
        strict: If True, raise exception on malformed components

    Returns:
        ExtractionResult with clean_text, components, and warnings
    """
    components = []
    warnings = []
    lines = markdown.split('\n')
    result_lines = []

    i = 0
    component_index = 0

    while i < len(lines):
        line = lines[i]

        # Check for component opening tag
        matched_component = None
        for comp_name in COMPONENT_NAMES:
            # Match opening tag with optional whitespace and attributes
            if re.match(rf'^\s*<{comp_name}(\s[^>]*)?>?\s*$', line):
                matched_component = comp_name
                break

        if matched_component:
            # Found opening tag, find closing tag
            start_line = i + 1  # 1-indexed
            component_lines = [line]
            i += 1

            # Find closing tag
            closing_pattern = rf'^\s*</{matched_component}>\s*$'
            found_closing = False
            nesting_level = 1

            while i < len(lines):
                current_line = lines[i]
                component_lines.append(current_line)

                # Check for nested same-type component (warn but continue)
                if re.match(rf'^\s*<{matched_component}(\s[^>]*)?>?\s*$', current_line):
                    nesting_level += 1
                    warning = f"Nested <{matched_component}> detected at line {i+1}"
                    warnings.append(warning)
                    logger.warning(warning)

                if re.match(closing_pattern, current_line):
                    nesting_level -= 1
                    if nesting_level == 0:
                        found_closing = True
                        break
                i += 1

            if found_closing:
                end_line = i + 1  # 1-indexed
                raw_content = '\n'.join(component_lines)

                # Extract inner content (between tags)
                inner_lines = component_lines[1:-1]  # Exclude opening and closing tags
                inner_content = '\n'.join(inner_lines)

                placeholder = f'<!-- COMPONENT_PLACEHOLDER_{component_index} -->'

                components.append(ComponentBlock(
                    type=matched_component,
                    start_line=start_line,
                    end_line=end_line,
                    raw_content=raw_content,
                    inner_content=inner_content,
                    placeholder=placeholder,
                    is_malformed=nesting_level != 0
                ))

                result_lines.append(placeholder)
                component_index += 1
            else:
                # No closing tag found - malformed component
                warning = f"Unclosed <{matched_component}> at line {start_line} - keeping as-is"
                warnings.append(warning)
                logger.warning(warning)

                if strict:
                    raise ValueError(f"Malformed component: unclosed <{matched_component}> at line {start_line}")

                # Keep as-is (malformed)
                result_lines.extend(component_lines)
        else:
            # Check for orphan closing tags
            for comp_name in COMPONENT_NAMES:
                if re.match(rf'^\s*</{comp_name}>\s*$', line):
                    warning = f"Orphan closing tag </{comp_name}> at line {i+1}"
                    warnings.append(warning)
                    logger.warning(warning)
                    break

            result_lines.append(line)

        i += 1

    clean_text = '\n'.join(result_lines)
    return ExtractionResult(
        clean_text=clean_text,
        components=components,
        warnings=warnings
    )


def restore_components(clean_text: str, components: List[ComponentBlock]) -> str:
    """
    Restore original components from placeholders.

    Args:
        clean_text: Processed markdown with placeholders
        components: Original extracted ComponentBlock list

    Returns:
        Full markdown with components restored
    """
    result = clean_text
    for component in components:
        result = result.replace(component.placeholder, component.raw_content)
    return result


def strip_markers(markdown: str) -> str:
    """
    Remove directive markers from content.

    Args:
        markdown: Markdown string (component-free or inner content)

    Returns:
        Clean markdown with markers removed
    """
    lines = markdown.split('\n')
    result_lines = []

    for line in lines:
        # Check if line is a marker (with optional leading/trailing whitespace)
        is_marker = False
        for marker in MARKERS:
            if line.strip() == marker or line.strip().startswith(marker):
                is_marker = True
                break

        if not is_marker:
            result_lines.append(line)

    return '\n'.join(result_lines)


def map_line_number(clean_line: int, components: List[ComponentBlock]) -> int:
    """
    Map line number from clean text back to original file.

    When components are extracted, multi-line components are replaced with
    single-line placeholders. This function reverses that mapping.

    Args:
        clean_line: Line number in clean text (1-indexed)
        components: Extracted components with line ranges

    Returns:
        Corresponding line number in original file (1-indexed)
    """
    if not components:
        return clean_line

    # Sort components by start_line
    sorted_components = sorted(components, key=lambda c: c.start_line)

    # Calculate cumulative offset
    # Each component reduces line count by (component_lines - 1)
    offset = 0

    for component in sorted_components:
        component_lines = component.end_line - component.start_line + 1
        lines_saved = component_lines - 1  # Placeholder is 1 line

        # Position of placeholder in clean text = original start - previous offsets
        placeholder_pos = component.start_line - offset

        # If clean_line is before this placeholder, we're done
        if clean_line < placeholder_pos:
            break

        # If clean_line is at or after the placeholder, add this component's offset
        offset += lines_saved

    return clean_line + offset


def preprocess_content(markdown: str) -> Tuple[str, List[ComponentBlock]]:
    """
    Full preprocessing: extract components and strip markers.

    Args:
        markdown: Raw markdown content

    Returns:
        Tuple of (clean_text, components)
    """
    clean_text, components = extract_components(markdown)
    clean_text = strip_markers(clean_text)
    return clean_text, components


def validate_component_syntax(markdown: str) -> List[str]:
    """
    Validate component syntax without modifying content.

    Args:
        markdown: Raw markdown content

    Returns:
        List of validation error/warning messages (empty if valid)
    """
    result = extract_components_with_warnings(markdown, strict=False)
    errors = list(result.warnings)

    # Additional validation checks
    lines = markdown.split('\n')

    # Check for partially opened tags (missing >)
    for i, line in enumerate(lines, 1):
        for comp_name in COMPONENT_NAMES:
            # Opening tag without closing >
            if re.match(rf'^\s*<{comp_name}(\s|$)', line) and '>' not in line:
                errors.append(f"Incomplete opening tag <{comp_name} at line {i}")
            # Closing tag without closing >
            if re.match(rf'^\s*</{comp_name}(\s|$)', line) and '>' not in line:
                errors.append(f"Incomplete closing tag </{comp_name} at line {i}")

    return errors
