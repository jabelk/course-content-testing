"""
Integration tests for the full LWC editorial pipeline.

Tests the complete flow from raw markdown through component extraction,
editorial validation, and output formatting.
"""

import os
import sys
from pathlib import Path

import pytest

# Add tools to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'tools'))

from component_skipper import extract_components, restore_components, preprocess_content
from lwc_editorial import load_topic_files, preprocess_for_editorial, validate_with_rules, format_pr_comment
from lwc_linter import validate_structure


class TestFullPipeline:
    """Integration tests for the complete editorial pipeline."""

    @pytest.fixture
    def sample_content(self):
        """Sample LWC module content with components."""
        return """# Topic Title

This is regular markdown content.

<CustomNote>
This is a custom note that should be skipped.
::: Help
Help text inside.
</CustomNote>

More regular content here with some  double spaces.

<QuestionMC>
::: Answers
Answer A
Answer B
::: Feedback
Good job!
</QuestionMC>

Final paragraph.
"""

    def test_component_extraction_preserves_content(self, sample_content):
        """Verify components are extracted and can be restored."""
        clean_text, components = extract_components(sample_content)

        # Check components were extracted
        assert len(components) == 2
        assert components[0].type == 'CustomNote'
        assert components[1].type == 'QuestionMC'

        # Check placeholders in clean text
        assert '<!-- COMPONENT_PLACEHOLDER_0 -->' in clean_text
        assert '<!-- COMPONENT_PLACEHOLDER_1 -->' in clean_text
        assert '<CustomNote>' not in clean_text
        assert '<QuestionMC>' not in clean_text

        # Check restoration
        restored = restore_components(clean_text, components)
        assert '<CustomNote>' in restored
        assert '<QuestionMC>' in restored
        assert restored == sample_content

    def test_preprocessing_strips_markers(self, sample_content):
        """Verify preprocessing extracts components and strips markers."""
        clean_text, components = preprocess_content(sample_content)

        # Check markers stripped
        assert '::: Help' not in clean_text
        assert '::: Answers' not in clean_text
        assert '::: Feedback' not in clean_text

        # Check regular content preserved
        assert 'This is regular markdown content.' in clean_text
        assert 'More regular content here' in clean_text

    def test_basic_validation_detects_issues(self, sample_content):
        """Verify basic validation finds issues like double spaces."""
        from lwc_models import TopicFile

        # Create topic file
        topic_file = TopicFile(
            path=Path('/test/Topic-1.md'),
            filename='Topic-1.md',
            raw_content=sample_content
        )

        # Preprocess
        preprocess_for_editorial(topic_file)

        # Validate
        result = validate_with_rules(topic_file, use_ai=False)

        # Should find double space issue
        assert len(result.issues) > 0
        double_space_issues = [i for i in result.issues if i.rule_id == 'DOUBLE_SPACE']
        assert len(double_space_issues) > 0

    def test_pr_comment_format(self, sample_content):
        """Verify PR comment is properly formatted."""
        from lwc_models import TopicFile

        # Create and process topic file
        topic_file = TopicFile(
            path=Path('/test/Topic-1.md'),
            filename='Topic-1.md',
            raw_content=sample_content
        )
        preprocess_for_editorial(topic_file)
        result = validate_with_rules(topic_file, use_ai=False)

        # Generate PR comment
        comment = format_pr_comment([result])

        # Check required sections
        assert '## Editorial Review Results' in comment
        assert '### Summary' in comment
        assert '| Metric | Count | Legend |' in comment


class TestLinterIntegration:
    """Integration tests for module structure linting."""

    @pytest.fixture
    def valid_module_path(self, tmp_path):
        """Create a valid module structure for testing."""
        # Create directories
        (tmp_path / 'Content').mkdir()

        # Create required files
        (tmp_path / 'ModuleStructure.json').write_text('{"topics": [{"file": "Topic-1.md"}]}')
        (tmp_path / 'Metadata.json').write_text('{"title": "Test Module"}')
        (tmp_path / 'Content' / 'Topic-1.md').write_text('# Topic 1\n\nContent here.')

        return tmp_path

    def test_valid_structure_passes(self, valid_module_path):
        """Verify valid module structure passes linting."""
        result = validate_structure(str(valid_module_path))
        assert result.passed
        assert len(result.errors) == 0

    def test_missing_content_fails(self, tmp_path):
        """Verify missing Content/ directory fails linting."""
        # Only create JSON files, no Content/
        (tmp_path / 'ModuleStructure.json').write_text('{}')
        (tmp_path / 'Metadata.json').write_text('{}')

        result = validate_structure(str(tmp_path))
        assert not result.passed
        assert any('Content' in e.message for e in result.errors)

    def test_missing_topic_files_fails(self, tmp_path):
        """Verify empty Content/ directory fails linting."""
        (tmp_path / 'Content').mkdir()
        (tmp_path / 'ModuleStructure.json').write_text('{}')
        (tmp_path / 'Metadata.json').write_text('{}')

        result = validate_structure(str(tmp_path))
        assert not result.passed
        assert any('Topic' in e.message for e in result.errors)
