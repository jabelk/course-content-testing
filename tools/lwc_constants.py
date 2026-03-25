"""
LWC Module Editorial Constants

Defines component names, markers, and patterns for LWC content processing.
"""

# Custom component names (PascalCase, block-level)
COMPONENT_NAMES = [
    'CustomNote',
    'QuestionMC',
    'AssessmentQG',
    'TabsHorizontal',
    'TabsVertical',
    'TabsAccordian',
    'LabSteps',
    'TableSimple',
    'TableComplex',
]

# Video component uses markdown image syntax with VIDEO: prefix
VIDEO_PATTERN = r'!\[VIDEO:[^\]]*\]\([^)]+\)'

# Directive markers inside components
MARKERS = [
    '::: Answers',
    '::: Feedback',
    '::: Action',
    '::: Task',
    '::: Help',
    '::: Response',
    '::: Enabling Objective',
    '::: Row',
    '::: Data',
]

# Required files for module structure validation
REQUIRED_FILES = [
    'ModuleStructure.json',
    'Metadata.json',
]

REQUIRED_DIRS = [
    'Content',
]

# Topic file pattern
TOPIC_FILE_PATTERN = r'^Topic-\d+\.md$'

# Linting rule IDs
class LintingRules:
    CONTENT_FOLDER_MISSING = 'LWC-001'
    NO_TOPIC_FILES = 'LWC-002'
    MODULE_STRUCTURE_MISSING = 'LWC-003'
    METADATA_MISSING = 'LWC-004'
    UNEXPECTED_FILE_CHANGES = 'LWC-005'
    TOPIC_MISMATCH = 'LWC-006'

# Editorial categories
class EditorialCategories:
    CISCO_STYLE = 'cisco_style'
    ACRONYM = 'acronym'
    GRAMMAR = 'grammar'
    TERMINOLOGY = 'terminology'

# Fix severities
class FixSeverity:
    SAFE = 'SAFE'       # Auto-apply safe
    REVIEW = 'REVIEW'   # Needs human review
    QUERY = 'QUERY'     # Flagged for discussion
