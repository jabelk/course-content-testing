"""
LWC Module Data Models

Defines entities for module repositories, topic files, editorial results, and linting results.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from enum import Enum
from pathlib import Path


class EditorialCategory(Enum):
    """Categories for editorial issues."""
    CISCO_STYLE = 'cisco_style'
    ACRONYM = 'acronym'
    GRAMMAR = 'grammar'
    TERMINOLOGY = 'terminology'
    PUNCTUATION = 'punctuation'
    HEADING = 'heading'
    PRODUCT_NAMING = 'product_naming'
    GUI_FORMAT = 'gui_format'
    STRUCTURE = 'structure'


class FixSeverity(Enum):
    """Severity levels for suggested fixes."""
    SAFE = 'SAFE'       # Auto-apply safe
    REVIEW = 'REVIEW'   # Needs human review
    QUERY = 'QUERY'     # Flagged for discussion


class LintingSeverity(Enum):
    """Severity levels for linting issues."""
    ERROR = 'error'     # Blocking - fails the check
    WARNING = 'warning' # Non-blocking - reported but continues


@dataclass
class EditorialRule:
    """An editorial validation rule from editorial_rules.yaml."""
    id: str                        # Unique ID (e.g., TERM_CLICK_ON)
    name: str                      # Human-readable name
    category: str                  # Rule category
    severity: str                  # high, medium, low
    fix_type: str                  # SAFE, REVIEW, QUERY
    pattern: str                   # Regex pattern
    pattern_type: str              # regex, stateful, ai_enhanced
    message: str                   # Issue description
    suggestion_template: str       # Fix suggestion template
    enabled: bool = True           # Whether rule is active
    priority: int = 50             # Lower = higher priority
    context_skip: List[str] = field(default_factory=list)  # Contexts to skip

    def get_fix_severity(self) -> 'FixSeverity':
        """Convert fix_type string to FixSeverity enum."""
        mapping = {
            'SAFE': FixSeverity.SAFE,
            'REVIEW': FixSeverity.REVIEW,
            'QUERY': FixSeverity.QUERY,
        }
        return mapping.get(self.fix_type.upper(), FixSeverity.REVIEW)

    def get_category_enum(self) -> 'EditorialCategory':
        """Convert category string to EditorialCategory enum."""
        mapping = {
            'terminology': EditorialCategory.TERMINOLOGY,
            'punctuation': EditorialCategory.PUNCTUATION,
            'heading': EditorialCategory.HEADING,
            'product_naming': EditorialCategory.PRODUCT_NAMING,
            'gui_format': EditorialCategory.GUI_FORMAT,
            'acronym': EditorialCategory.ACRONYM,
            'grammar': EditorialCategory.GRAMMAR,
            'structure': EditorialCategory.STRUCTURE,
            'cisco_style': EditorialCategory.CISCO_STYLE,
        }
        return mapping.get(self.category.lower(), EditorialCategory.GRAMMAR)


@dataclass
class AcronymEntry:
    """An acronym definition from the database."""
    acronym: str                   # The acronym (e.g., VLAN)
    expansion: str                 # Full expansion
    category: str = ''             # Database category (cisco_products, networking, etc.)
    full_name: Optional[str] = None  # Cisco full product name
    first_use: Optional[str] = None  # Recommended first use text
    subsequent: List[str] = field(default_factory=list)  # Acceptable subsequent uses
    deprecated: bool = False       # Whether acronym is deprecated
    well_known: bool = False       # Skip expansion check
    skip_expansion: bool = False   # Never require expansion
    notes: Optional[str] = None    # Additional guidance


@dataclass
class ContentSegment:
    """A segment of content within a topic file."""
    type: str                      # 'regular' or 'component'
    content: str                   # Segment text
    start_line: int                # Starting line number
    end_line: int                  # Ending line number
    component_name: Optional[str] = None  # Component name if type='component'


@dataclass
class Metadata:
    """Module metadata from Metadata.json."""
    title: str
    description: str
    tags: List[str] = field(default_factory=list)
    guid: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Metadata':
        """Create Metadata from dictionary."""
        return cls(
            title=data.get('title', ''),
            description=data.get('description', ''),
            tags=data.get('tags', []),
            guid=data.get('guid')
        )


@dataclass
class TopicEntry:
    """Single topic within module structure."""
    id: str
    file: str
    title: str
    duration: str
    type: str  # 'Topic', 'Lab', 'SummaryChallenge'

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TopicEntry':
        """Create TopicEntry from dictionary."""
        return cls(
            id=data.get('id', ''),
            file=data.get('file', ''),
            title=data.get('title', ''),
            duration=data.get('duration', ''),
            type=data.get('type', 'Topic')
        )


@dataclass
class ModuleStructure:
    """Module structure from ModuleStructure.json."""
    topics: List[TopicEntry] = field(default_factory=list)
    labs: List[TopicEntry] = field(default_factory=list)
    duration_total: str = ''

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ModuleStructure':
        """Create ModuleStructure from dictionary."""
        topics = [TopicEntry.from_dict(t) for t in data.get('topics', [])]
        labs = [TopicEntry.from_dict(l) for l in data.get('labs', [])]
        return cls(
            topics=topics,
            labs=labs,
            duration_total=data.get('duration_total', data.get('duration', ''))
        )


@dataclass
class ComponentBlock:
    """Extracted custom component from markdown."""
    type: str           # Component name (e.g., 'CustomNote')
    start_line: int     # Starting line in original file (1-indexed)
    end_line: int       # Ending line in original file (1-indexed)
    raw_content: str    # Full component including tags
    inner_content: str  # Content between opening/closing tags
    placeholder: str    # Replacement placeholder string


@dataclass
class TopicFile:
    """Markdown content file in Content/ directory."""
    path: Path
    filename: str
    raw_content: str
    clean_content: str = ''
    components: List[ComponentBlock] = field(default_factory=list)
    word_count: int = 0

    def __post_init__(self):
        """Calculate word count from clean content."""
        if self.clean_content:
            self.word_count = len(self.clean_content.split())


@dataclass
class EditorialIssue:
    """Single editorial issue detected."""
    id: str
    category: EditorialCategory
    severity: FixSeverity
    line: int
    original: str
    suggested: str
    rule_id: str
    rationale: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'category': self.category.value,
            'severity': self.severity.value,
            'line': self.line,
            'original': self.original,
            'suggested': self.suggested,
            'rule_id': self.rule_id,
            'rationale': self.rationale
        }


@dataclass
class EditorialResult:
    """Result of editorial validation for a topic file."""
    file: TopicFile
    issues: List[EditorialIssue] = field(default_factory=list)
    auto_fixed: int = 0
    needs_review: int = 0
    skipped_components: int = 0

    def __post_init__(self):
        """Calculate auto_fixed and needs_review counts."""
        self.auto_fixed = sum(1 for i in self.issues if i.severity == FixSeverity.SAFE)
        self.needs_review = sum(1 for i in self.issues if i.severity in [FixSeverity.REVIEW, FixSeverity.QUERY])
        self.skipped_components = len(self.file.components)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            'file': self.file.filename,
            'issues': [i.to_dict() for i in self.issues],
            'auto_fixed': self.auto_fixed,
            'needs_review': self.needs_review,
            'skipped_components': self.skipped_components
        }


@dataclass
class LintingError:
    """Blocking structural error."""
    rule_id: str
    message: str
    path: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            'rule_id': self.rule_id,
            'message': self.message,
            'path': self.path,
            'severity': 'error'
        }


@dataclass
class LintingWarning:
    """Non-blocking structural warning."""
    rule_id: str
    message: str
    path: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            'rule_id': self.rule_id,
            'message': self.message,
            'path': self.path,
            'severity': 'warning'
        }


@dataclass
class LintingResult:
    """Result of module structure linting."""
    passed: bool = True
    errors: List[LintingError] = field(default_factory=list)
    warnings: List[LintingWarning] = field(default_factory=list)

    def __post_init__(self):
        """Update passed status based on errors."""
        self.passed = len(self.errors) == 0

    def add_error(self, rule_id: str, message: str, path: str = ''):
        """Add a linting error."""
        self.errors.append(LintingError(rule_id, message, path))
        self.passed = False

    def add_warning(self, rule_id: str, message: str, path: str = ''):
        """Add a linting warning."""
        self.warnings.append(LintingWarning(rule_id, message, path))

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            'passed': self.passed,
            'errors': [e.to_dict() for e in self.errors],
            'warnings': [w.to_dict() for w in self.warnings],
            'error_count': len(self.errors),
            'warning_count': len(self.warnings)
        }


@dataclass
class ModuleRepository:
    """Represents a single LWC module Git repository."""
    name: str
    owner: str
    branch: str
    content_dir: Path
    metadata: Optional[Metadata] = None
    structure: Optional[ModuleStructure] = None
    topic_files: List[TopicFile] = field(default_factory=list)

    def get_topic_file(self, filename: str) -> Optional[TopicFile]:
        """Get a topic file by filename."""
        for tf in self.topic_files:
            if tf.filename == filename:
                return tf
        return None


@dataclass
class PRComment:
    """Formatted PR comment for GitHub."""
    summary_table: str = ''
    category_sections: Dict[str, str] = field(default_factory=dict)
    linting_section: str = ''
    full_markdown: str = ''

    def build(self, editorial_results: List[EditorialResult], linting_result: Optional[LintingResult] = None) -> str:
        """Build full PR comment markdown."""
        sections = ['## Editorial Review Results\n']

        # Summary table
        total_issues = sum(len(r.issues) for r in editorial_results)
        total_fixed = sum(r.auto_fixed for r in editorial_results)
        total_review = sum(r.needs_review for r in editorial_results)

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

        for cat, issues in by_category.items():
            fixed = sum(1 for i in issues if i.severity == FixSeverity.SAFE)
            review = len(issues) - fixed
            sections.append(f'| {cat.replace("_", " ").title()} | {len(issues)} | {fixed} | {review} |')

        sections.append(f'| **Total** | **{total_issues}** | **{total_fixed}** | **{total_review}** |')
        sections.append('')

        # Linting section
        if linting_result:
            if linting_result.passed:
                sections.append('### Module Structure: ✓ Passed\n')
            else:
                sections.append('### Module Structure: ✗ Failed\n')
                for error in linting_result.errors:
                    sections.append(f'- **{error.rule_id}**: {error.message}')
                sections.append('')

        self.full_markdown = '\n'.join(sections)
        return self.full_markdown
