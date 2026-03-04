"""
Editorial Rules Engine - Data Models

Defines the core dataclasses for the editorial validation system:
- EditorialRule: Rule definition loaded from YAML
- EditorialIssue: Instance of rule violation
- AcronymState: Tracks acronym usage across files
- QualityScore: Editorial quality metric
- ValidationResult: Aggregated validation output
- PRCommentPayload: Structured PR comment data
"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum


class FixType(Enum):
    """How the issue should be handled"""
    SAFE = "SAFE"      # Deterministic fix, auto-apply without review
    REVIEW = "REVIEW"  # Apply fix but flag for human verification
    QUERY = "QUERY"    # Don't fix, ask author for clarification


class PatternType(Enum):
    """Pattern matching strategy"""
    REGEX = "regex"           # Standard regex pattern matching
    STATEFUL = "stateful"     # Requires tracking state across files
    CONTEXT = "context"       # Requires surrounding context analysis
    AI_ENHANCED = "ai_enhanced"  # Uses AI for suggestion generation


class Severity(Enum):
    """Issue importance for reporting"""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Category(Enum):
    """Rule grouping categories"""
    HEADING = "heading"
    TERMINOLOGY = "terminology"
    ACRONYM = "acronym"
    PUNCTUATION = "punctuation"
    STRUCTURE = "structure"
    GUI_FORMAT = "gui_format"
    CODE_STYLE = "code_style"
    PRODUCT_NAMING = "product_naming"


@dataclass
class EditorialRule:
    """
    Represents a single validation rule loaded from YAML configuration.

    Attributes:
        id: Unique rule identifier (e.g., HEADING_GERUND)
        name: Human-readable rule name
        category: Rule grouping
        severity: Issue importance
        fix_type: How to handle fixes (SAFE/REVIEW/QUERY)
        pattern: Regex pattern for detection (optional)
        pattern_type: Pattern matching strategy
        message: Issue description template with {match} placeholder
        suggestion_template: Fix suggestion with {original}, {suggestion} placeholders
        enabled: Whether rule is active
        priority: Conflict resolution order (lower = higher priority)
        context_skip: Contexts where rule should not apply
    """
    id: str
    name: str
    category: str
    severity: str
    fix_type: str
    pattern_type: str
    message: str
    suggestion_template: str
    enabled: bool = True
    priority: int = 50
    pattern: Optional[str] = None
    context_skip: List[str] = field(default_factory=list)
    ai_prompt: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'EditorialRule':
        """Create EditorialRule from dictionary (YAML data)"""
        return cls(
            id=data['id'],
            name=data['name'],
            category=data['category'],
            severity=data['severity'],
            fix_type=data['fix_type'],
            pattern_type=data['pattern_type'],
            message=data['message'],
            suggestion_template=data['suggestion_template'],
            enabled=data.get('enabled', True),
            priority=data.get('priority', 50),
            pattern=data.get('pattern'),
            context_skip=data.get('context_skip', []),
            ai_prompt=data.get('ai_prompt')
        )


@dataclass
class EditorialIssue:
    """
    An instance of a rule violation detected in content.

    Attributes:
        rule_id: Reference to EditorialRule.id
        file_path: Relative path to file
        line_number: 1-indexed line number
        original_text: Matched text from content
        fix_type: Inherited from rule (SAFE/REVIEW/QUERY)
        message: Rendered message
        confidence: Fix confidence score (0.0-1.0)
        suggested_fix: Proposed correction (optional for QUERY)
        column_start: Column position start
        column_end: Column position end
        applied: Whether fix was applied
        context_before: ~20 chars before the match for locating in document
        context_after: ~20 chars after the match for locating in document
        absolute_offset: Character offset in full document for inline diff
    """
    rule_id: str
    file_path: str
    line_number: int
    original_text: str
    fix_type: str
    message: str
    confidence: float
    suggested_fix: Optional[str] = None
    column_start: int = 0
    column_end: int = 0
    applied: bool = False
    context_before: str = ""
    context_after: str = ""
    absolute_offset: int = 0

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            'rule_id': self.rule_id,
            'file_path': self.file_path,
            'line_number': self.line_number,
            'original_text': self.original_text,
            'fix_type': self.fix_type,
            'message': self.message,
            'confidence': self.confidence,
            'suggested_fix': self.suggested_fix,
            'column_start': self.column_start,
            'column_end': self.column_end,
            'applied': self.applied,
            'context_before': self.context_before,
            'context_after': self.context_after,
            'absolute_offset': self.absolute_offset
        }


@dataclass
class AcronymState:
    """
    Tracks acronym usage across tutorial step files for first-use detection.

    Attributes:
        acronym: The acronym (uppercase)
        first_seen_file: File where first seen
        first_seen_line: Line number of first use
        is_expanded: Was expansion found near first use
        expansion: The expansion text (if known)
        source: Where expansion came from (inline/database/ai_suggested)
        context_relevance: Relevance to tutorial topic (0.0-1.0)
    """
    acronym: str
    first_seen_file: str
    first_seen_line: int
    is_expanded: bool = False
    expansion: Optional[str] = None
    source: Optional[str] = None  # 'inline', 'database', 'ai_suggested'
    context_relevance: float = 0.0

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            'acronym': self.acronym,
            'first_seen_file': self.first_seen_file,
            'first_seen_line': self.first_seen_line,
            'is_expanded': self.is_expanded,
            'expansion': self.expansion,
            'source': self.source,
            'context_relevance': self.context_relevance
        }


@dataclass
class QualityScore:
    """
    Calculated metric representing editorial readiness.

    Score Calculation:
        base_score = 10.0
        score = base_score - (safe_count * 0.1) - (review_count * 0.5) - (query_count * 1.0)
        score = clamp(score, 1.0, 10.0)

    Interpretation:
        10: Perfect - no issues detected
        8-9.9: Minor - only auto-fixes needed
        6-7.9: Moderate - some items need verification
        3-5.9: Significant - author input required
        1-2.9: Needs work - many unresolved issues
    """
    score: float
    safe_count: int
    review_count: int
    query_count: int

    @property
    def total_issues(self) -> int:
        """Total number of issues"""
        return self.safe_count + self.review_count + self.query_count

    @property
    def interpretation(self) -> str:
        """Human-readable interpretation of score"""
        if self.score >= 10:
            return "Perfect - no issues detected"
        elif self.score >= 8:
            return "Minor - only auto-fixes needed"
        elif self.score >= 6:
            return "Moderate - some items need verification"
        elif self.score >= 3:
            return "Significant - author input required"
        else:
            return "Needs work - many unresolved issues"

    @classmethod
    def calculate(cls, issues: List[EditorialIssue]) -> 'QualityScore':
        """Calculate quality score from list of issues"""
        safe_count = sum(1 for i in issues if i.fix_type == 'SAFE')
        review_count = sum(1 for i in issues if i.fix_type == 'REVIEW')
        query_count = sum(1 for i in issues if i.fix_type == 'QUERY')

        score = 10.0 - (safe_count * 0.1) - (review_count * 0.5) - (query_count * 1.0)
        score = max(1.0, min(10.0, score))

        return cls(
            score=round(score, 1),
            safe_count=safe_count,
            review_count=review_count,
            query_count=query_count
        )

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            'score': self.score,
            'safe_count': self.safe_count,
            'review_count': self.review_count,
            'query_count': self.query_count,
            'total_issues': self.total_issues,
            'interpretation': self.interpretation
        }


@dataclass
class ValidationResult:
    """
    Aggregated result of running validation on a tutorial.

    Attributes:
        tutorial_folder: Path to tc-* folder
        files_processed: Files validated
        issues: All detected issues
        quality_score: Calculated score
        acronym_state: Acronym tracking state
        rules_applied: Rule IDs that were run
        processing_time_ms: Time to process
        ai_available: Whether AI was used
        fixes_applied: Number of auto-fixes applied
    """
    tutorial_folder: str
    files_processed: List[str] = field(default_factory=list)
    issues: List[EditorialIssue] = field(default_factory=list)
    quality_score: Optional[QualityScore] = None
    acronym_state: Dict[str, AcronymState] = field(default_factory=dict)
    rules_applied: List[str] = field(default_factory=list)
    processing_time_ms: int = 0
    ai_available: bool = False
    fixes_applied: int = 0

    def add_issue(self, issue: EditorialIssue):
        """Add an issue to the result"""
        self.issues.append(issue)

    def get_issues_by_file(self) -> Dict[str, List[EditorialIssue]]:
        """Group issues by file path"""
        by_file: Dict[str, List[EditorialIssue]] = {}
        for issue in self.issues:
            if issue.file_path not in by_file:
                by_file[issue.file_path] = []
            by_file[issue.file_path].append(issue)
        return by_file

    def get_issues_by_type(self) -> Dict[str, List[EditorialIssue]]:
        """Group issues by fix type"""
        by_type: Dict[str, List[EditorialIssue]] = {
            'SAFE': [],
            'REVIEW': [],
            'QUERY': []
        }
        for issue in self.issues:
            if issue.fix_type in by_type:
                by_type[issue.fix_type].append(issue)
        return by_type

    def calculate_score(self):
        """Calculate and set the quality score"""
        self.quality_score = QualityScore.calculate(self.issues)

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            'tutorial_folder': self.tutorial_folder,
            'files_processed': self.files_processed,
            'issues': [i.to_dict() for i in self.issues],
            'issues_by_file': {k: [i.to_dict() for i in v] for k, v in self.get_issues_by_file().items()},
            'quality_score': self.quality_score.to_dict() if self.quality_score else None,
            'acronym_state': {k: v.to_dict() for k, v in self.acronym_state.items()},
            'rules_applied': self.rules_applied,
            'processing_time_ms': self.processing_time_ms,
            'ai_available': self.ai_available,
            'fixes_applied': self.fixes_applied
        }


@dataclass
class PRCommentPayload:
    """
    Structured data for generating PR comment.

    Attributes:
        quality_score: Score summary
        auto_fixed: SAFE items that were applied
        review_needed: REVIEW items that were applied
        queries: QUERY items for author
        by_file: Issues grouped by file path
    """
    quality_score: QualityScore
    auto_fixed: List[EditorialIssue] = field(default_factory=list)
    review_needed: List[EditorialIssue] = field(default_factory=list)
    queries: List[EditorialIssue] = field(default_factory=list)

    @classmethod
    def from_validation_result(cls, result: ValidationResult) -> 'PRCommentPayload':
        """Create PRCommentPayload from ValidationResult"""
        by_type = result.get_issues_by_type()
        return cls(
            quality_score=result.quality_score or QualityScore.calculate(result.issues),
            auto_fixed=by_type['SAFE'],
            review_needed=by_type['REVIEW'],
            queries=by_type['QUERY']
        )

    def get_by_file(self) -> Dict[str, List[EditorialIssue]]:
        """Group all issues by file path"""
        by_file: Dict[str, List[EditorialIssue]] = {}
        for issue in self.auto_fixed + self.review_needed + self.queries:
            if issue.file_path not in by_file:
                by_file[issue.file_path] = []
            by_file[issue.file_path].append(issue)
        # Sort issues within each file by line number
        for file_path in by_file:
            by_file[file_path].sort(key=lambda x: x.line_number)
        return by_file
