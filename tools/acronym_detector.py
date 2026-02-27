"""
Editorial Rules Engine - Acronym Detector

Dynamic acronym detection with on-the-fly database lookup.
Tracks first-use across tutorial step files and generates
appropriate REVIEW or QUERY issues based on database presence.

Key Features:
    - Detects acronyms using pattern [A-Z]{2,}s?
    - Excludes code blocks, inline code, URLs, and file paths
    - Looks up each detected acronym in acronym-database.json
    - Tracks first-use state across all step files
    - Handles deprecated acronyms with replacement suggestions
    - Creates QUERY for unknown acronyms
"""
import os
import re
import json
from typing import List, Dict, Optional, Tuple, Set
from editorial_models import EditorialIssue, AcronymState


# Regex patterns
ACRONYM_PATTERN = re.compile(r'\b([A-Z]{2,}s?)\b')
CODE_BLOCK_PATTERN = re.compile(r'```[\s\S]*?```', re.MULTILINE)
INLINE_CODE_PATTERN = re.compile(r'`[^`]+`')
URL_PATTERN = re.compile(r'https?://[^\s\)]+')
FILE_PATH_PATTERN = re.compile(r'\./[^\s\)]+|\b[\w/-]+\.\w{2,4}\b')

# Common acronyms that don't need expansion (well-established)
SKIP_ACRONYMS = {
    'OK', 'AM', 'PM', 'US', 'UK', 'TV', 'PC', 'ID', 'IP',
    'GB', 'MB', 'KB', 'TB', 'CPU', 'RAM', 'ROM', 'USB', 'HTTP',
    'HTTPS', 'HTML', 'CSS', 'JSON', 'XML', 'PDF', 'YAML', 'PNG',
    'JPG', 'JPEG', 'GIF', 'SVG', 'MD', 'API', 'SDK', 'CLI', 'GUI',
    'OS', 'VM', 'AWS', 'GCP', 'UI', 'UX', 'FAQ', 'TBD', 'TODO',
    'NOTE', 'IMPORTANT', 'WARNING', 'TIP', 'INFO',
}


class AcronymDetector:
    """
    Detects and tracks acronyms across tutorial files.

    Maintains state to ensure first-use expansion is only flagged once
    per acronym per tutorial.
    """

    def __init__(self, db_path: str = None):
        """
        Initialize the detector with optional database path.

        Args:
            db_path: Path to acronym-database.json
        """
        self.database: Dict[str, dict] = {}
        self.state: Dict[str, AcronymState] = {}
        self._load_database(db_path)

    def _load_database(self, db_path: str = None):
        """Load acronym database from JSON file."""
        if not db_path:
            # Default path relative to tools/
            script_dir = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(script_dir, '..', '.claude', 'references', 'acronym-database.json')

        if not os.path.exists(db_path):
            return

        with open(db_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Flatten nested structure into single lookup dict
        for category, acronyms in data.items():
            if category.startswith('_'):  # Skip metadata
                continue
            if isinstance(acronyms, dict):
                for acronym, info in acronyms.items():
                    if isinstance(info, dict):
                        self.database[acronym] = {
                            **info,
                            'category': category
                        }

    def reset_state(self):
        """Reset tracking state for new tutorial."""
        self.state = {}

    def detect_acronyms(
        self,
        content: str,
        file_path: str,
        tutorial_title: str = "",
        verbose: bool = False
    ) -> Tuple[List[EditorialIssue], Dict[str, AcronymState]]:
        """
        Detect acronyms in content and generate issues.

        Args:
            content: File content to analyze
            file_path: Relative path to the file
            tutorial_title: Tutorial title for context
            verbose: Show detection details

        Returns:
            Tuple of (list of issues, updated acronym state)
        """
        issues = []
        lines = content.split('\n')

        # Find regions to skip (code blocks)
        skip_regions = self._get_skip_regions(content)

        # Find all acronym matches
        for line_idx, line in enumerate(lines):
            line_num = line_idx + 1
            line_start = sum(len(lines[i]) + 1 for i in range(line_idx))

            for match in ACRONYM_PATTERN.finditer(line):
                acronym = match.group(1)

                # Remove trailing 's' for lookup
                base_acronym = acronym.rstrip('s') if acronym.endswith('s') and len(acronym) > 2 else acronym

                # Skip if in code block region
                absolute_pos = line_start + match.start()
                if self._is_in_skip_region(absolute_pos, skip_regions):
                    if verbose:
                        print(f"  Skipping {acronym} at line {line_num}: in code block")
                    continue

                # Skip if in inline code or URL
                if self._is_in_inline_skip(match.group(), line):
                    if verbose:
                        print(f"  Skipping {acronym} at line {line_num}: in inline code/URL")
                    continue

                # Skip well-established acronyms
                if base_acronym in SKIP_ACRONYMS or acronym in SKIP_ACRONYMS:
                    if verbose:
                        print(f"  Skipping {acronym} at line {line_num}: well-established")
                    continue

                # Process the acronym
                issue = self._process_acronym(
                    acronym=base_acronym,
                    original_text=acronym,
                    file_path=file_path,
                    line_num=line_num,
                    line=line,
                    tutorial_title=tutorial_title,
                    verbose=verbose
                )

                if issue:
                    issues.append(issue)

        return issues, self.state

    def _get_skip_regions(self, content: str) -> List[Tuple[int, int]]:
        """Get list of (start, end) positions for code blocks to skip."""
        regions = []
        for match in CODE_BLOCK_PATTERN.finditer(content):
            regions.append((match.start(), match.end()))
        return regions

    def _is_in_skip_region(self, pos: int, regions: List[Tuple[int, int]]) -> bool:
        """Check if position is inside any skip region."""
        for start, end in regions:
            if start <= pos < end:
                return True
        return False

    def _is_in_inline_skip(self, match_text: str, line: str) -> bool:
        """Check if match is inside inline code, URL, or file path."""
        # Check inline code
        for code_match in INLINE_CODE_PATTERN.finditer(line):
            if match_text in code_match.group():
                return True

        # Check URLs
        for url_match in URL_PATTERN.finditer(line):
            if match_text in url_match.group():
                return True

        # Check file paths
        for path_match in FILE_PATH_PATTERN.finditer(line):
            if match_text in path_match.group():
                return True

        return False

    def _process_acronym(
        self,
        acronym: str,
        original_text: str,
        file_path: str,
        line_num: int,
        line: str,
        tutorial_title: str,
        verbose: bool = False
    ) -> Optional[EditorialIssue]:
        """
        Process a single acronym and determine if an issue should be created.

        Returns None if no issue needed (already expanded or tracked).
        """
        # Check if already tracked
        if acronym in self.state:
            # Already seen - no new issue needed
            if verbose:
                print(f"  Acronym {acronym} already tracked from {self.state[acronym].first_seen_file}")
            return None

        # Check if already expanded inline
        expansion_pattern = rf'\([^)]*{re.escape(acronym)}[^)]*\)'
        if re.search(expansion_pattern, line):
            # Acronym appears in parentheses - likely an expansion
            self.state[acronym] = AcronymState(
                acronym=acronym,
                first_seen_file=file_path,
                first_seen_line=line_num,
                is_expanded=True,
                source='inline'
            )
            if verbose:
                print(f"  Acronym {acronym} found expanded inline at line {line_num}")
            return None

        # Check full expansion pattern: "Full Name (ACRONYM)"
        full_expansion_pattern = rf'\b[\w\s]+\({re.escape(acronym)}\)'
        if re.search(full_expansion_pattern, line):
            self.state[acronym] = AcronymState(
                acronym=acronym,
                first_seen_file=file_path,
                first_seen_line=line_num,
                is_expanded=True,
                source='inline'
            )
            if verbose:
                print(f"  Acronym {acronym} found with full expansion at line {line_num}")
            return None

        # Look up in database
        db_entry = self.database.get(acronym)

        if db_entry:
            # Check if this is a skip pattern (HTTP methods, course codes, etc.)
            if db_entry.get('skip', False):
                if verbose:
                    print(f"  Acronym {acronym} is in skip patterns - ignoring")
                self.state[acronym] = AcronymState(
                    acronym=acronym,
                    first_seen_file=file_path,
                    first_seen_line=line_num,
                    is_expanded=True,  # Mark as "expanded" to skip future occurrences
                    source='skip_pattern'
                )
                return None

            # Check if expansion should be skipped (well-known terms)
            if db_entry.get('skip_expansion', False) or db_entry.get('skip_in_cli', False):
                if verbose:
                    print(f"  Acronym {acronym} has skip_expansion/skip_in_cli - ignoring")
                self.state[acronym] = AcronymState(
                    acronym=acronym,
                    first_seen_file=file_path,
                    first_seen_line=line_num,
                    is_expanded=True,
                    source='skip_expansion'
                )
                return None

            # Known acronym - check if deprecated
            if db_entry.get('deprecated', False):
                return self._create_deprecated_issue(
                    acronym, original_text, file_path, line_num, db_entry, verbose
                )
            else:
                return self._create_expansion_issue(
                    acronym, original_text, file_path, line_num, db_entry, verbose
                )
        else:
            # Unknown acronym - create QUERY
            return self._create_unknown_issue(
                acronym, original_text, file_path, line_num, verbose
            )

    def _create_expansion_issue(
        self,
        acronym: str,
        original_text: str,
        file_path: str,
        line_num: int,
        db_entry: dict,
        verbose: bool
    ) -> EditorialIssue:
        """Create a REVIEW issue for acronym needing expansion."""
        expansion = db_entry.get('expansion', '')
        first_use = db_entry.get('first_use', f"{expansion} ({acronym})")

        # Track state
        self.state[acronym] = AcronymState(
            acronym=acronym,
            first_seen_file=file_path,
            first_seen_line=line_num,
            is_expanded=False,
            expansion=expansion,
            source='database'
        )

        if verbose:
            print(f"  Creating expansion issue for {acronym} at line {line_num}")

        return EditorialIssue(
            rule_id='ACRONYM_FIRST_USE',
            file_path=file_path,
            line_number=line_num,
            original_text=original_text,
            fix_type='REVIEW',
            message=f"Acronym '{acronym}' not expanded on first use",
            confidence=0.85,
            suggested_fix=first_use
        )

    def _create_deprecated_issue(
        self,
        acronym: str,
        original_text: str,
        file_path: str,
        line_num: int,
        db_entry: dict,
        verbose: bool
    ) -> EditorialIssue:
        """Create a REVIEW issue for deprecated acronym."""
        full_name = db_entry.get('full_name', db_entry.get('expansion', acronym))
        notes = db_entry.get('notes', '')

        # Track state
        self.state[acronym] = AcronymState(
            acronym=acronym,
            first_seen_file=file_path,
            first_seen_line=line_num,
            is_expanded=False,
            expansion=full_name,
            source='database'
        )

        if verbose:
            print(f"  Creating deprecated issue for {acronym} at line {line_num}")

        message = f"Acronym '{acronym}' is deprecated - use '{full_name}' instead"
        if notes:
            message += f". Note: {notes[:100]}..."

        return EditorialIssue(
            rule_id='ACRONYM_DEPRECATED',
            file_path=file_path,
            line_number=line_num,
            original_text=original_text,
            fix_type='REVIEW',
            message=message,
            confidence=0.9,
            suggested_fix=full_name
        )

    def _create_unknown_issue(
        self,
        acronym: str,
        original_text: str,
        file_path: str,
        line_num: int,
        verbose: bool
    ) -> EditorialIssue:
        """Create a QUERY issue for unknown acronym."""
        # Track state
        self.state[acronym] = AcronymState(
            acronym=acronym,
            first_seen_file=file_path,
            first_seen_line=line_num,
            is_expanded=False,
            source=None
        )

        if verbose:
            print(f"  Creating unknown acronym query for {acronym} at line {line_num}")

        return EditorialIssue(
            rule_id='ACRONYM_UNKNOWN',
            file_path=file_path,
            line_number=line_num,
            original_text=original_text,
            fix_type='QUERY',
            message=f"Unknown acronym '{acronym}' - please provide expansion or confirm intentional",
            confidence=0.5,
            suggested_fix=None
        )


def detect_acronyms_in_tutorial(
    folder_path: str,
    db_path: str = None,
    verbose: bool = False
) -> Tuple[List[EditorialIssue], Dict[str, AcronymState]]:
    """
    Detect acronyms across all step files in a tutorial.

    Args:
        folder_path: Path to tutorial folder
        db_path: Path to acronym database
        verbose: Show detection details

    Returns:
        Tuple of (all issues, acronym state)
    """
    detector = AcronymDetector(db_path)

    # Get tutorial title from sidecar.json if available
    tutorial_title = ""
    sidecar_path = os.path.join(folder_path, 'sidecar.json')
    if os.path.exists(sidecar_path):
        with open(sidecar_path, 'r', encoding='utf-8') as f:
            sidecar = json.load(f)
            tutorial_title = sidecar.get('title', '')

    # Get step files sorted by number
    step_files = []
    for filename in os.listdir(folder_path):
        if filename.startswith('step-') and filename.endswith('.md'):
            step_files.append(os.path.join(folder_path, filename))

    step_files.sort(key=lambda p: int(os.path.basename(p).replace('step-', '').replace('.md', '')))

    all_issues = []
    for file_path in step_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        issues, _ = detector.detect_acronyms(
            content=content,
            file_path=os.path.basename(file_path),
            tutorial_title=tutorial_title,
            verbose=verbose
        )
        all_issues.extend(issues)

    return all_issues, detector.state
