# Quickstart: Course AI Editing

**Feature**: 014-course-ai-editing
**Date**: 2026-02-27

## Prerequisites

1. **Python 3.10+** (matches existing tutorial-testing tools)
2. **Pandoc** installed and available in PATH
   ```bash
   # macOS
   brew install pandoc

   # Ubuntu/Debian
   sudo apt-get install pandoc

   # Verify installation
   pandoc --version
   ```
3. **Repository cloned** with tutorial-testing submodule

## Quick Start (PoC Usage)

### 1. Process a Course Module

```bash
cd tutorial-testing/tools

# Basic usage - generates markdown report to stdout
python3 course_editor.py "/path/to/course.docx"

# Save report to file
python3 course_editor.py "/path/to/course.docx" --output report.md

# JSON output for automation
python3 course_editor.py "/path/to/course.docx" --json --output report.json

# Verbose mode for debugging
python3 course_editor.py "/path/to/course.docx" --verbose

# Show progress for large documents
python3 course_editor.py "/path/to/course.docx" --progress
```

### 2. Process All Test Courses

```bash
# Use the convenience script
./run_poc.sh

# With verbose output
./run_poc.sh --verbose

# Generate JSON reports
./run_poc.sh --json

# Include consistency testing
./run_poc.sh --consistency
```

### 3. Run Consistency Tests

```bash
# Test consistency with 3 runs (default)
python3 test_consistency.py "/path/to/course.docx"

# More runs for higher confidence
python3 test_consistency.py "/path/to/course.docx" --runs 5

# JSON output
python3 test_consistency.py "/path/to/course.docx" --json
```

### 4. Review Output

The generated report includes:

```markdown
# Editorial Review Report: SD-WAN Evolution and Core Concepts

**Quality Score**: 🔴 1.0/10 (Needs work - many unresolved issues)

| Property | Value |
|----------|-------|
| Word Count | 8,500 |
| Estimated Duration | 56m |
| Processing Time | 0.8s |

## Summary

**Total Issues**: 255

| Fix Type | Count | Description |
|----------|-------|-------------|
| SAFE | 120 | Auto-fixable with high confidence |
| REVIEW | 85 | Applied but needs human verification |
| QUERY | 50 | Questions for author - not auto-fixed |

## Changes by Category

### Cisco Style Guide (30 issues)

**Auto-fixable (SAFE)**:

| Line | Original | Suggested | Rationale |
|------|----------|-----------|-----------|
| 45 | `click on` | `click` | Use 'click' instead of 'click on' |

### Acronyms (45 issues)

**Questions for Author (QUERY)**:

- **Line 36**: Unknown acronym 'VXLAN' - please provide expansion
```

## CLI Reference

### course_editor.py

```
usage: course_editor.py [-h] [--output OUTPUT] [--json] [--verbose] [--no-ai] [--progress] docx_path

Process a DOCX course module through editorial validation.

positional arguments:
  docx_path        Path to DOCX file to process

optional arguments:
  -h, --help       Show this help message
  --output, -o     Output path for report
  --json           Output as JSON instead of markdown
  --verbose, -v    Show detailed processing information
  --no-ai          Disable AI enhancement (regex rules only)
  --progress       Show progress indicator for large documents
```

### test_consistency.py

```
usage: test_consistency.py [-h] [--runs N] [--threshold N] [--verbose] [--json] docx_path

Test consistency of course editorial validation across multiple runs.

positional arguments:
  docx_path           Path to DOCX file to test

optional arguments:
  -h, --help          Show this help message
  --runs, -r N        Number of test runs (default: 3)
  --threshold, -t N   Maximum acceptable variance percentage (default: 5)
  --verbose, -v       Show detailed per-run output
  --json              Output results as JSON
```

## Example Workflow

### For Kim (Course Editor)

1. **Submit course for review**:
   ```bash
   python course_editor.py "802.1X EAP Authentication_Sec 01_orig.docx"
   ```

2. **Review the markdown report** in your text editor or markdown viewer

3. **Provide feedback** to Jason on:
   - Are the SAFE fixes appropriate?
   - Any REVIEW items incorrectly flagged?
   - Are QUERY questions clear?

### For Jason (Developer)

1. **Run on all test courses**:
   ```bash
   ./run_poc.sh
   ```

2. **Run with consistency testing**:
   ```bash
   ./run_poc.sh --consistency
   ```

3. **Compare results**:
   - Check consistency: same input → same output (0% variance)
   - Validate quality scores make sense
   - Identify rule gaps in gap-analysis.md

4. **Iterate**:
   - Add missing rules to `editorial_rules.yaml`
   - Update acronym database
   - Re-run and compare

## Troubleshooting

### "pandoc not found"

Install pandoc:
```bash
brew install pandoc  # macOS
```

### "DOCX conversion failed"

Check DOCX is valid:
```bash
# Try manual conversion
pandoc input.docx -t markdown -o test.md
```

### "No issues found"

The document may already be well-formatted, or rules need expansion:
```bash
# Run with verbose to see rule matching
python course_editor.py input.docx --verbose
```

## Next Steps After PoC

1. **Gather feedback** from Kim on report usefulness
2. **Identify rule gaps** from test course results
3. **Add grammar rules** as needed
4. **Build DOCX track changes output** (follow-up phase)
