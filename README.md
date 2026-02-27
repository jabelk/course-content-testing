# Course Content Testing

AI-powered editorial review for LWC course content. Adapts the tutorial editorial pipeline to process DOCX course modules with **consistent, repeatable results**.

## For Kim: Quick Links

### Generated Reports (Ready for Review)

| Course | Report | Issues |
|--------|--------|--------|
| SD-WAN Evolution and Core Concepts | [View Report](reports/01_SD-WAN%20Evolution%20and%20Core%20Concepts_orig-report.md) | 308 |
| SD-WAN Components and Roles | [View Report](reports/02_SD-WAN%20Components%20and%20Roles_orig-report.md) | 446 |
| 802.1X EAP Authentication | [View Report](reports/802.1X%20EAP%20Authentication_Sec%2001_orig-report.md) | 294 |
| 802.1X on Cisco Wireless LAN Controllers | [View Report](reports/802.1X%20on%20Cisco%20Wireless%20LAN%20Controllers_Sec%2001_orig-report.md) | 390 |
| AUTOCOR | [View Report](reports/AUTOCOR-Sec01_orig-report.md) | 122 |
| DCNAUTO | [View Report](reports/DCNAUTO-Sec%2001_orig-report.md) | 299 |
| Network Access for Non-Supplicant Devices | [View Report](reports/Network%20Access%20for%20Non-Supplicant%20Devices_Sec%2001_orig-report.md) | 258 |

### Key Documentation

- [Quickstart Guide](docs/quickstart.md) - How to run the tools
- [Setup Guide](docs/setup-guide.md) - Set up on your own system
- [Cursor Setup Guide](docs/cursor-setup-guide.md) - **For MS Word users** - step-by-step Cursor/MCP setup
- [Why This Works](docs/approach-comparison.md) - Why deterministic rules beat RAG/Circuit
- [Gap Analysis](docs/gap-analysis.md) - What's missing (acronyms, rules)
- [Implementation Learnings](docs/learnings.md) - Architecture and decisions
- [Architecture Decision](docs/architecture-decision.md) - Hybrid architecture (Git-centralized, processing-distributed)

### Backlog

See [Issues](https://github.com/CiscoLearning/course-content-testing/issues) for planned improvements:
- ~~DOCX track changes output~~ ✅ Implemented
- ~~Expanded acronym database~~ ✅ Done (135 entries)
- Web upload interface
- ~~MCP server for Cursor integration~~ ✅ Implemented

## Key Results

| Metric | Circuit | This Tool |
|--------|---------|-----------|
| Consistency | 50%+ variance | **0% variance** |
| Processing Time | Minutes | **< 1 second per course** |
| Categorization | Uncategorized | **4 clear categories** |

### Recent Improvements (2026-02-27)

- **16 grammar rules** - Serial comma, number spelling, compound modifiers
- **Expanded acronym database** - 135+ entries (up from 58)
- **Skip patterns** - Course codes, HTTP methods, CLI keywords now ignored
- **False positive reduction** - AUTOCOR course: 128 → 122 issues (6 fewer)

## How Reports Are Organized

Each report categorizes issues into **Kim's 4 categories**:

1. **Cisco Style Guide** - Headings, terminology, GUI formatting
2. **Acronyms** - First-use expansion, unknown acronyms
3. **Technical Terms** - Product naming, code style
4. **Grammar & Punctuation** - Structure, punctuation, grammar (16 rules: serial comma, number spelling, compound modifiers)

### Fix Types

| Type | Meaning | Action |
|------|---------|--------|
| 🟢 SAFE | High confidence fix | Can auto-apply |
| 🟡 REVIEW | Needs verification | Review before applying |
| 🔴 QUERY | Author decision needed | Don't auto-fix |

## Feedback Needed

After reviewing the reports, please provide feedback on:

1. **Accuracy**: Are the SAFE suggestions correct?
2. **False Positives**: Any incorrectly flagged items?
3. **Missing Rules**: What issues weren't caught?
4. **Report Format**: Easy to navigate?
5. **Categories**: Do the 4 categories make sense?

## Architecture

```
DOCX Course Module
       ↓
   [pandoc]
       ↓
   Markdown
       ↓
[Editorial Validation]  ←── editorial_rules.yaml
       ↓                 ←── acronym-database.json
 ValidationResult
       ↓
[Report Generator]
       ↓
 Markdown Report
```

## Tools

| Tool | Purpose |
|------|---------|
| `course_editor.py` | Main CLI - process DOCX files |
| `course_editor.py --docx-output` | Generate DOCX with track changes |
| `mcp_editorial_server.py` | MCP server for IDE integration |
| `docx_track_changes.py` | Generate track changes documents |
| `test_consistency.py` | Verify results are repeatable |
| `run_poc.sh` | Batch process all test courses |
| `course_report_generator.py` | Generate categorized reports |
| `docx_converter.py` | DOCX to Markdown via pandoc |

## Running Locally

### Prerequisites

```bash
# Install pandoc
brew install pandoc  # macOS

# Python 3.10+
python3 --version
```

### Process a Course

```bash
cd tools

# Generate report
python3 course_editor.py "../test-courses/DCNAUTO-Sec 01_orig.docx" --output report.md

# Test consistency
python3 test_consistency.py "../test-courses/DCNAUTO-Sec 01_orig.docx"
```

### Process All Courses

```bash
cd tools
./run_poc.sh
```

### Generate DOCX with Track Changes

```bash
cd tools

# Generate DOCX with tracked changes instead of markdown report
python3 course_editor.py "../test-courses/DCNAUTO-Sec 01_orig.docx" --docx-output

# Output: DCNAUTO-Sec 01_orig_edited.docx
```

## MCP Server (For Cursor/Claude Code)

The MCP Editorial Server allows IDE integration via Model Context Protocol.

> **Cisco Employees**: Request Cursor at https://appstore.cisco.com/details/cursor

### Setup

1. Install dependencies:
```bash
pip install fastmcp python-docx pyyaml
```

2. Add to your MCP configuration:
```json
{
    "mcpServers": {
        "editorial": {
            "command": "python3",
            "args": ["/path/to/course-content-testing/tools/mcp_editorial_server.py"]
        }
    }
}
```

### Available Tools

| Tool | Description |
|------|-------------|
| `analyze_document` | Analyze DOCX and return editorial suggestions |
| `apply_fixes` | Apply SAFE fixes with track changes |
| `lookup_acronym` | Query the acronym database |
| `list_rules` | List all editorial rules by category |
| `get_server_info` | Server version and configuration |

### Example Usage (in Cursor/Claude Code)

```
> Run analyze_document on /path/to/course.docx
> Look up the acronym VXLAN
> Apply SAFE fixes to the document
```

## Repository Structure

```
course-content-testing/
├── README.md              # This file
├── tools/                 # Python tools
│   ├── course_editor.py   # Main CLI (--docx-output for track changes)
│   ├── mcp_editorial_server.py  # MCP server for IDE integration
│   ├── docx_track_changes.py    # Track changes generator
│   ├── editorial_*.py     # Validation engine
│   ├── editorial_rules.yaml  # Rule definitions
│   └── run_poc.sh         # Batch script
├── reports/               # Generated reports
│   └── *.md               # One per test course
├── test-courses/          # Kim's test DOCX files
│   └── *.docx
├── docs/                  # Documentation
│   ├── quickstart.md
│   ├── gap-analysis.md
│   └── learnings.md
└── .claude/
    └── references/
        └── acronym-database.json
```

## AI Enhancement (Optional)

The tool works fully with regex-only rules (no API needed). For smarter AI-powered suggestions:

### Setup

1. Get an Anthropic API key from https://console.anthropic.com/
2. Set the environment variable:
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-..."
   ```
3. Run without `--no-ai` flag:
   ```bash
   python3 course_editor.py "../test-courses/DCNAUTO-Sec 01_orig.docx"
   ```

### What AI Adds

- Smarter procedural intro detection
- Context-aware heading suggestions
- Better acronym relevance scoring

**Note**: Current PoC uses `--no-ai` for 100% deterministic results. AI adds ~5% variance but catches more issues.

## Next Steps

1. **Kim reviews reports** - Provide feedback on accuracy
2. ~~**Expand acronym database**~~ ✅ DONE - 135 entries with skip patterns
3. **Add DOCX track changes** - Output edits directly in Word format
4. **Integrate with workflow** - Confluence/SharePoint upload

## Related Resources

- [Feature Spec](https://github.com/CiscoLearning/tutorial-platform-specs/tree/main/specs/014-course-ai-editing) - Full specification
- [Tutorial Testing Tools](https://github.com/CiscoLearning/tutorial-testing) - Original tutorial pipeline

---

*Built by Jason with Claude Code assistance*
