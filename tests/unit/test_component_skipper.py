"""
Unit tests for component_skipper module.
"""

import pytest
import sys
import os

# Add tools directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'tools'))

from component_skipper import (
    extract_components,
    restore_components,
    strip_markers,
    map_line_number,
    preprocess_content,
    ComponentBlock
)


class TestExtractComponents:
    """Tests for extract_components function."""

    def test_extract_single_custom_note(self):
        """Should extract a single CustomNote component."""
        markdown = """Some intro text.

<CustomNote>

This is a note.

</CustomNote>

More content."""

        clean_text, components = extract_components(markdown)

        assert len(components) == 1
        assert components[0].type == 'CustomNote'
        assert '<!-- COMPONENT_PLACEHOLDER_0 -->' in clean_text
        assert '<CustomNote>' not in clean_text
        assert 'Some intro text.' in clean_text
        assert 'More content.' in clean_text

    def test_extract_multiple_components(self):
        """Should extract multiple different components."""
        markdown = """Intro.

<CustomNote>
Note content.
</CustomNote>

Middle text.

<QuestionMC>
Question content.
</QuestionMC>

Outro."""

        clean_text, components = extract_components(markdown)

        assert len(components) == 2
        assert components[0].type == 'CustomNote'
        assert components[1].type == 'QuestionMC'
        assert '<!-- COMPONENT_PLACEHOLDER_0 -->' in clean_text
        assert '<!-- COMPONENT_PLACEHOLDER_1 -->' in clean_text

    def test_extract_tabs_horizontal(self):
        """Should extract TabsHorizontal component."""
        markdown = """<TabsHorizontal>

# Tab 1
Content 1

# Tab 2
Content 2

</TabsHorizontal>"""

        clean_text, components = extract_components(markdown)

        assert len(components) == 1
        assert components[0].type == 'TabsHorizontal'
        assert '# Tab 1' in components[0].inner_content

    def test_preserve_line_numbers(self):
        """Should correctly record start and end line numbers."""
        markdown = """Line 1
Line 2
<CustomNote>
Note line 1
Note line 2
</CustomNote>
Line 7"""

        clean_text, components = extract_components(markdown)

        assert components[0].start_line == 3
        assert components[0].end_line == 6

    def test_no_components(self):
        """Should handle content with no components."""
        markdown = "Just regular markdown content."

        clean_text, components = extract_components(markdown)

        assert len(components) == 0
        assert clean_text == markdown

    def test_unclosed_component(self):
        """Should preserve unclosed components as-is."""
        markdown = """<CustomNote>
This note is never closed.
More text."""

        clean_text, components = extract_components(markdown)

        # Unclosed component should be preserved in output
        assert len(components) == 0
        assert '<CustomNote>' in clean_text


class TestRestoreComponents:
    """Tests for restore_components function."""

    def test_restore_single_component(self):
        """Should restore a single component."""
        original = """Intro.

<CustomNote>
Note content.
</CustomNote>

Outro."""

        clean_text, components = extract_components(original)
        restored = restore_components(clean_text, components)

        assert restored == original

    def test_restore_multiple_components(self):
        """Should restore multiple components."""
        original = """<CustomNote>
Note.
</CustomNote>

Text.

<QuestionMC>
Question.
</QuestionMC>"""

        clean_text, components = extract_components(original)
        restored = restore_components(clean_text, components)

        assert restored == original


class TestStripMarkers:
    """Tests for strip_markers function."""

    def test_strip_answers_marker(self):
        """Should remove ::: Answers marker."""
        content = """Question text

::: Answers

- [ ] Option A
- [x] Option B"""

        result = strip_markers(content)

        assert '::: Answers' not in result
        assert 'Option A' in result
        assert 'Option B' in result

    def test_strip_feedback_marker(self):
        """Should remove ::: Feedback marker."""
        content = """::: Feedback

The correct answer is B."""

        result = strip_markers(content)

        assert '::: Feedback' not in result
        assert 'correct answer' in result

    def test_strip_multiple_markers(self):
        """Should remove all marker types."""
        content = """::: Action
Do something.
::: Help
Get help here.
::: Enabling Objective
Learn this."""

        result = strip_markers(content)

        assert '::: Action' not in result
        assert '::: Help' not in result
        assert '::: Enabling Objective' not in result
        assert 'Do something.' in result

    def test_preserve_non_markers(self):
        """Should preserve regular content."""
        content = """Regular line.
Another line with ::: in the middle.
Final line."""

        result = strip_markers(content)

        # Lines with ::: in the middle should be preserved
        assert 'Regular line.' in result


class TestMapLineNumber:
    """Tests for map_line_number function."""

    def test_no_components(self):
        """Should return same line number when no components."""
        components = []
        assert map_line_number(5, components) == 5

    def test_line_before_component(self):
        """Should return same line for lines before any component."""
        component = ComponentBlock(
            type='CustomNote',
            start_line=10,
            end_line=15,
            raw_content='',
            inner_content='',
            placeholder='<!-- PLACEHOLDER -->'
        )
        # Line 5 is before the component, should be unchanged
        assert map_line_number(5, [component]) == 5


class TestPreprocessContent:
    """Tests for preprocess_content function."""

    def test_full_preprocessing(self):
        """Should extract components and strip markers."""
        content = """Intro text.

<CustomNote>
::: Help
Help text.
</CustomNote>

Regular text."""

        clean_text, components = preprocess_content(content)

        assert len(components) == 1
        assert '<CustomNote>' not in clean_text
        assert '::: Help' not in clean_text
        assert 'Intro text.' in clean_text
        assert 'Regular text.' in clean_text
