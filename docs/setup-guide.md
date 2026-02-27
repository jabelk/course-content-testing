# Setup Guide: Running the Editorial Pipeline

This guide explains how to set up and run the course editorial pipeline on your own system.

## Prerequisites

### Required Software

| Software | Version | Purpose | Install |
|----------|---------|---------|---------|
| Python | 3.10+ | Run tools | [python.org](https://python.org) |
| Pandoc | 2.0+ | DOCX conversion | `brew install pandoc` (Mac) |
| Git | Any | Clone repo | [git-scm.com](https://git-scm.com) |

### Optional: AI Enhancement

For AI-powered suggestions (not required for basic operation):

| Item | Purpose | Get It |
|------|---------|--------|
| Anthropic API Key | Claude Opus access | [console.anthropic.com](https://console.anthropic.com) |

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/CiscoLearning/course-content-testing.git
cd course-content-testing
```

### 2. Install Dependencies

```bash
pip install requests pyyaml
```

### 3. Process a Course

```bash
cd tools

# Without AI (deterministic only)
python3 course_editor.py "../test-courses/your-course.docx" --output report.md --no-ai

# With AI enhancement (requires API key)
export ANTHROPIC_API_KEY="sk-ant-..."
python3 course_editor.py "../test-courses/your-course.docx" --output report.md
```

### 4. View the Report

Open `report.md` in any markdown viewer or text editor.

## Running on Your Own System

### Option A: Local Command Line

Best for: Individual editors testing content

```bash
# One-time setup
git clone https://github.com/CiscoLearning/course-content-testing.git
cd course-content-testing/tools

# Each time you want to process a file
python3 course_editor.py "/path/to/your/file.docx" --output "/path/to/report.md"
```

### Option B: GitHub Actions (Automated)

Best for: Teams with multiple editors, consistent processing

1. Fork this repository to your GitHub organization
2. Add your DOCX files to `test-courses/`
3. Go to Actions → "Generate Editorial Reports" → Run workflow
4. Reports appear in `reports/` folder

**To add the API key:**
1. Go to repo Settings → Secrets → Actions
2. Add secret: `ANTHROPIC_API_KEY` = your key

### Option C: Local Server (Future)

For high-volume processing, we're exploring a server mode where:
- Editors upload DOCX via web form
- Server processes and returns report
- No local installation needed

Contact Jason if interested in this option.

## Configuration

### Editorial Rules

Rules are defined in `tools/editorial_rules.yaml`:

```yaml
rules:
  - id: em-dash-spacing
    pattern: ' — '
    replacement: '—'
    category: punctuation
    fix_type: SAFE
```

To add custom rules:
1. Edit `editorial_rules.yaml`
2. Add your pattern, replacement, and category
3. Re-run the tool

### Acronym Database

Known acronyms are in `.claude/references/acronym-database.json`:

```json
{
  "SD-WAN": {
    "expansion": "Software-Defined Wide Area Network",
    "category": "networking"
  }
}
```

To add acronyms:
1. Edit `acronym-database.json`
2. Add the acronym, expansion, and category
3. Re-run the tool

### Categories

Reports organize issues into 4 categories:

| Category | What It Covers |
|----------|----------------|
| Cisco Style Guide | Headings, terminology, GUI formatting |
| Acronyms | First-use expansion, unknown acronyms |
| Technical Terms | Product naming, code style |
| Chicago Manual | Punctuation, structure, grammar |

## Batch Processing

Process all DOCX files at once:

```bash
cd tools
./run_poc.sh
```

This runs all files in `test-courses/` and outputs to `reports/`.

## Verifying Consistency

Run the same file multiple times to confirm 0% variance:

```bash
python3 test_consistency.py "../test-courses/your-course.docx"
```

Expected output:
```
Run 1: 150 issues
Run 2: 150 issues
Run 3: 150 issues
Consistency: 100%
```

## Integrating with Your Workflow

### For Word-First Teams

1. Process DOCX through pipeline
2. Review markdown report
3. Apply changes manually in Word
4. (Future) Use DOCX track changes output

### For Xyleme-First Teams

1. Export content from Xyleme
2. Convert to DOCX or markdown
3. Process through pipeline
4. Use report to identify fixes
5. Apply changes in Xyleme

### For GitHub Teams

1. Create PR with content
2. GitHub Action processes automatically
3. Review AI comments on PR
4. Merge when satisfied

## Troubleshooting

### "pandoc: command not found"

Install pandoc:
```bash
# Mac
brew install pandoc

# Ubuntu/Debian
sudo apt-get install pandoc

# Windows
choco install pandoc
```

### "ANTHROPIC_API_KEY not set"

Either:
1. Set the key: `export ANTHROPIC_API_KEY="sk-ant-..."`
2. Or use `--no-ai` flag for regex-only mode

### "ModuleNotFoundError: No module named 'requests'"

```bash
pip install requests pyyaml
```

### Reports show 0 issues

Check that:
1. The DOCX file has actual text content
2. Pandoc is converting successfully
3. The file isn't corrupted

## Getting Help

- **Documentation**: See `docs/` folder
- **Issues**: [GitHub Issues](https://github.com/CiscoLearning/course-content-testing/issues)
- **Contact**: Jason (jabelk@cisco.com)

---

*For why this approach works better than Circuit, see [approach-comparison.md](approach-comparison.md)*
