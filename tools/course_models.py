"""
Course AI Editing - Data Models

Defines course-specific dataclasses for processing DOCX course modules:
- CourseModule: Represents a DOCX course document
- Section: A logical section within a course module
- ChangeReport: Output format for markdown change reports
- ReportSummary: Summary statistics for report header

Reuses existing models from editorial_models.py:
- EditorialIssue, ValidationResult, QualityScore, AcronymState
"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime


# Category mapping from existing editorial categories to Kim's 4 categories
CATEGORY_MAPPING = {
    'heading': 'Cisco Style Guide',
    'terminology': 'Cisco Style Guide',
    'punctuation': 'Grammar & Punctuation',  # May also be Cisco Style Guide for specific rules
    'structure': 'Grammar & Punctuation',
    'gui_format': 'Cisco Style Guide',
    'code_style': 'Technical Terms',
    'product_naming': 'Technical Terms',
    'acronym': 'Acronyms',
}

# Punctuation rules that belong to Cisco Style Guide instead of Grammar & Punctuation
CISCO_PUNCTUATION_RULES = [
    'PUNCTUATION_CLICK_ON',  # "click on" vs "click"
    'PUNCTUATION_GUI_COLON',  # Colons after GUI elements
]


def map_category(existing_category: str, rule_id: str = '') -> str:
    """
    Map existing editorial category to Kim's 4 categories.

    Args:
        existing_category: Category from editorial_models (lowercase)
        rule_id: Optional rule ID for context-specific mapping

    Returns:
        One of: 'Cisco Style Guide', 'Acronyms', 'Technical Terms', 'Grammar & Punctuation'
    """
    category_lower = existing_category.lower()

    # Special handling for punctuation rules that are Cisco-specific
    if category_lower == 'punctuation' and rule_id in CISCO_PUNCTUATION_RULES:
        return 'Cisco Style Guide'

    return CATEGORY_MAPPING.get(category_lower, 'Grammar & Punctuation')


@dataclass
class Section:
    """
    A logical section within a course module (heading + content).

    Attributes:
        heading: Section heading text
        level: Heading level (1-6)
        content: Section content (markdown)
        start_line: Starting line number in full document
        end_line: Ending line number
        word_count: Word count for duration estimation
    """
    heading: str
    level: int
    content: str
    start_line: int
    end_line: int
    word_count: int = 0

    def __post_init__(self):
        """Calculate word count if not provided"""
        if self.word_count == 0:
            self.word_count = len(self.content.split())

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            'heading': self.heading,
            'level': self.level,
            'content': self.content,
            'start_line': self.start_line,
            'end_line': self.end_line,
            'word_count': self.word_count
        }


@dataclass
class CourseModule:
    """
    Represents a single DOCX course document submitted for review.

    Attributes:
        file_path: Path to original DOCX file
        name: Course module name (from filename or metadata)
        topic: Topic area (e.g., "SD-WAN", "Security")
        estimated_duration: Estimated content duration (e.g., "1h30m")
        markdown_content: Converted markdown text
        sections: Parsed document sections
        metadata: Any extracted DOCX metadata
    """
    file_path: str
    name: str
    markdown_content: str = ''
    topic: str = ''
    estimated_duration: str = ''
    sections: List[Section] = field(default_factory=list)
    metadata: Dict = field(default_factory=dict)

    @classmethod
    def from_docx(cls, file_path: str, markdown_content: str) -> 'CourseModule':
        """
        Create CourseModule from DOCX file path and converted markdown.

        Args:
            file_path: Path to the DOCX file
            markdown_content: Markdown content from pandoc conversion

        Returns:
            CourseModule instance with parsed sections
        """
        import os

        # Extract name from filename
        filename = os.path.basename(file_path)
        name = os.path.splitext(filename)[0]

        # Parse sections from markdown
        sections = cls._parse_sections(markdown_content)

        # Estimate duration based on word count (150 words/minute average)
        total_words = sum(s.word_count for s in sections)
        minutes = total_words // 150
        hours = minutes // 60
        remaining_minutes = minutes % 60
        if hours > 0:
            estimated_duration = f"{hours}h{remaining_minutes:02d}m"
        else:
            estimated_duration = f"{minutes}m"

        return cls(
            file_path=file_path,
            name=name,
            markdown_content=markdown_content,
            estimated_duration=estimated_duration,
            sections=sections
        )

    @staticmethod
    def _parse_sections(markdown_content: str) -> List[Section]:
        """
        Parse markdown content into logical sections.

        Args:
            markdown_content: Full markdown text

        Returns:
            List of Section objects
        """
        import re

        lines = markdown_content.split('\n')
        sections = []
        current_heading = ''
        current_level = 0
        current_content = []
        current_start = 1

        heading_pattern = re.compile(r'^(#{1,6})\s+(.+)$')

        for i, line in enumerate(lines, 1):
            match = heading_pattern.match(line)
            if match:
                # Save previous section if exists
                if current_heading or current_content:
                    content = '\n'.join(current_content)
                    sections.append(Section(
                        heading=current_heading,
                        level=current_level,
                        content=content,
                        start_line=current_start,
                        end_line=i - 1
                    ))

                # Start new section
                current_level = len(match.group(1))
                current_heading = match.group(2).strip()
                current_content = []
                current_start = i
            else:
                current_content.append(line)

        # Don't forget the last section
        if current_heading or current_content:
            content = '\n'.join(current_content)
            sections.append(Section(
                heading=current_heading,
                level=current_level,
                content=content,
                start_line=current_start,
                end_line=len(lines)
            ))

        return sections

    @property
    def total_word_count(self) -> int:
        """Total word count across all sections"""
        return sum(s.word_count for s in self.sections)

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            'file_path': self.file_path,
            'name': self.name,
            'topic': self.topic,
            'estimated_duration': self.estimated_duration,
            'total_word_count': self.total_word_count,
            'section_count': len(self.sections),
            'sections': [s.to_dict() for s in self.sections],
            'metadata': self.metadata
        }


@dataclass
class ReportSummary:
    """
    Summary statistics for the report header.

    Attributes:
        total_issues: Total number of issues found
        safe_count: Auto-fixable issues
        review_count: Issues needing human review
        query_count: Questions for author
        by_category: Count per Kim's category
        processing_time_ms: Time to process
    """
    total_issues: int
    safe_count: int
    review_count: int
    query_count: int
    by_category: Dict[str, int] = field(default_factory=dict)
    processing_time_ms: int = 0

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            'total_issues': self.total_issues,
            'safe_count': self.safe_count,
            'review_count': self.review_count,
            'query_count': self.query_count,
            'by_category': self.by_category,
            'processing_time_ms': self.processing_time_ms
        }


@dataclass
class ChangeReport:
    """
    Output format for the markdown change report.

    Attributes:
        course_name: Course module name
        generated_at: Report generation timestamp
        quality_score: QualityScore from validation
        summary: ReportSummary statistics
        changes_by_category: Issues grouped by Kim's 4 categories
        changes_by_location: Issues sorted by line number
        metadata: Processing info (duration, rules applied)
    """
    course_name: str
    generated_at: datetime
    quality_score: 'QualityScore'  # Forward reference to editorial_models
    summary: ReportSummary
    changes_by_category: Dict[str, List['EditorialIssue']] = field(default_factory=dict)
    changes_by_location: List['EditorialIssue'] = field(default_factory=list)
    metadata: Dict = field(default_factory=dict)

    @classmethod
    def from_validation_result(cls, result: 'ValidationResult', course_name: str) -> 'ChangeReport':
        """
        Create ChangeReport from ValidationResult.

        Args:
            result: ValidationResult from editorial_validation
            course_name: Name of the course module

        Returns:
            ChangeReport instance ready for markdown generation
        """
        from editorial_models import QualityScore

        # Calculate quality score if not already done
        quality_score = result.quality_score
        if quality_score is None:
            quality_score = QualityScore.calculate(result.issues)

        # Group by Kim's categories
        changes_by_category: Dict[str, List] = {
            'Cisco Style Guide': [],
            'Acronyms': [],
            'Technical Terms': [],
            'Grammar & Punctuation': []
        }

        for issue in result.issues:
            # Get category from rule_id (format: CATEGORY_RULE_NAME)
            parts = issue.rule_id.split('_')
            existing_category = parts[0].lower() if parts else 'other'
            kim_category = map_category(existing_category, issue.rule_id)
            changes_by_category[kim_category].append(issue)

        # Create summary
        by_category = {cat: len(issues) for cat, issues in changes_by_category.items() if issues}
        summary = ReportSummary(
            total_issues=len(result.issues),
            safe_count=quality_score.safe_count,
            review_count=quality_score.review_count,
            query_count=quality_score.query_count,
            by_category=by_category,
            processing_time_ms=result.processing_time_ms
        )

        # Sort by location
        changes_by_location = sorted(result.issues, key=lambda x: x.line_number)

        return cls(
            course_name=course_name,
            generated_at=datetime.now(),
            quality_score=quality_score,
            summary=summary,
            changes_by_category=changes_by_category,
            changes_by_location=changes_by_location,
            metadata={
                'rules_applied': result.rules_applied,
                'files_processed': result.files_processed,
                'ai_available': result.ai_available,
                'fixes_applied': result.fixes_applied
            }
        )

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            'course_name': self.course_name,
            'generated_at': self.generated_at.isoformat(),
            'quality_score': self.quality_score.to_dict(),
            'summary': self.summary.to_dict(),
            'changes_by_category': {
                cat: [issue.to_dict() for issue in issues]
                for cat, issues in self.changes_by_category.items()
            },
            'changes_by_location': [issue.to_dict() for issue in self.changes_by_location],
            'metadata': self.metadata
        }
