# Course Editorial Review - Walkthrough for Kim

**Last Updated**: March 3, 2026

Upload a DOCX file, click a button, get an editorial review report. No coding required!

**NEW**: Inline-diff format shows the full document with changes marked `~~deleted~~` **added** so you can easily find and apply edits!

---

## Quick Overview

| Step | Action | Time |
|------|--------|------|
| 1 | Upload your DOCX file to `uploads/` | 2 min |
| 2 | Run the workflow | 1 min |
| 3 | View your report in `reports/` | 1 min |

**Total time**: ~5 minutes

---

## Step 1: Upload Your DOCX File

### 1.1 Go to the uploads folder

**Direct link**: https://github.com/CiscoLearning/course-content-testing/tree/main/uploads

Or navigate manually:
1. Go to https://github.com/CiscoLearning/course-content-testing
2. Click on the `uploads` folder

### 1.2 Upload your file

1. Click **"Add file"** button (top right)
2. Select **"Upload files"**
3. Drag and drop your `.docx` file (or click "choose your files")
4. Wait for upload to complete (green checkmark)

### 1.3 Commit the upload

1. Scroll down to **"Commit changes"**
2. (Optional) Add a message like "Add course for review"
3. Click green **"Commit changes"** button

---

## Step 2: Run the Editorial Review

### 2.1 Go to the workflow page

**Direct link** (recommended):
https://github.com/CiscoLearning/course-content-testing/actions/workflows/generate-reports.yml

Or navigate manually:
1. Click **"Actions"** tab (top of page)
2. In the **LEFT SIDEBAR**, click **"Generate Editorial Reports"**
   - Important: Click the workflow NAME, not a workflow run in the list!

### 2.2 Run the workflow

1. Look for the **"Run workflow"** button on the RIGHT side of the page
   - It's a dropdown button, may be blue or gray
2. Click it and set options:
   - **Which folder**: Select `uploads` (default)
   - **Report format**: Choose your preferred format:
     - `both` (recommended) - Get both table and inline-diff reports
     - `inline-diff` - Full document with changes marked inline
     - `standard` - Table format with line numbers
   - **AI suggestions**: Check this box for smarter suggestions (recommended first time)
   - **Verbose logs**: Leave unchecked (unless debugging)
3. Click green **"Run workflow"** button

**Tip**: Use `both` to get both report types - the inline-diff shows your full document with changes marked, while the table format groups issues by category.

### 2.3 Wait for completion

1. **Refresh the page** after clicking "Run workflow" to see it start
2. Look for your run at the top of the list:
   - Yellow dot = running (~1-3 minutes)
   - Green checkmark = done!
   - Red X = error (see Troubleshooting below)
3. Click on the run to watch progress in real-time

---

## Step 3: View Your Report

### 3.1 Go to reports folder

**Direct link**: https://github.com/CiscoLearning/course-content-testing/tree/main/reports

### 3.2 Find your report(s)

If you selected `both`, you'll have two reports:

| Report Type | Filename | Best For |
|-------------|----------|----------|
| **Inline Diff** | `<filename>-inline-diff.md` | Finding and applying changes |
| **Table Format** | `<filename>-report.md` | Summary view by category |

Example: `SD-WAN_Module_1.docx` generates:
- `SD-WAN_Module_1-inline-diff.md`
- `SD-WAN_Module_1-report.md`

### 3.3 Using the Inline-Diff Report (Recommended)

The inline-diff report shows your **entire document** with changes marked:

```
...misconfigured ~~ACL~~ **access control list (ACL)** [Explanation: Acronym
not expanded on first use. Category: Acronyms] shown in the following figure...
```

**How to read it:**
- `~~text~~` = text to remove (strikethrough)
- `**text**` = text to add (bold)
- `[Explanation: ...]` = why we flagged it

**How to find text in your Word doc:**
1. Copy the surrounding text (e.g., "misconfigured ACL shown in the following")
2. Ctrl+F in your Word document
3. Apply the suggested change

### 3.4 Using the Table Report

The table report groups issues by category with context preview:

| Line | Context | Change | Rationale |
|------|---------|--------|-----------|
| 17 | ...when a m... `ACL` shown in... | ~~ACL~~ → **access control...** | Acronym not expanded... |

The **Context** column shows text before/after so you can search for it in Word.

---

## Understanding the Report

### About Line Numbers

Line numbers in the table report refer to the **converted markdown file** (what the tool sees after converting your DOCX). They won't match Word line numbers exactly.

**Best approach**: Use the **Context** column or the **inline-diff report** to search for the actual text in your Word document.

### Quality Score

| Score | Meaning |
|-------|---------|
| 8-10 | Excellent - few issues |
| 5-7 | Good - some cleanup needed |
| 3-4 | Needs work - many issues |
| 1-2 | Significant revision needed |

### Issue Types

| Symbol | Type | What to Do |
|--------|------|------------|
| 🟢 SAFE | High confidence | Can auto-apply |
| 🟡 REVIEW | Probably correct | Please verify |
| 🔴 QUERY | Author decides | System is unsure |

### Categories

1. **Cisco Style Guide** - Headings, terminology, UI formatting
2. **Acronyms** - First-use expansion, unknown acronyms
3. **Technical Terms** - Product naming, code style
4. **Grammar & Punctuation** - Punctuation, grammar, structure

---

## File Requirements

### Supported Format

| Format | Extension | Status |
|--------|-----------|--------|
| Microsoft Word | `.docx` | Supported |
| Old Word | `.doc` | Convert to .docx first |
| PDF | `.pdf` | Not supported |

### File Naming

- **Good**: `SD-WAN Evolution_Sec 01.docx`
- **Avoid**: `Course #1 & More!.docx` (special characters)

### Size Limits

- **Maximum**: 100 MB
- **Recommended**: Under 25 MB

---

## Troubleshooting

### "No DOCX files found in uploads/"

1. Make sure you uploaded to `uploads/` folder (not root)
2. Make sure file ends in `.docx`
3. Check your commit was successful

### Workflow failed (red X)

1. Click on the failed run
2. Click "Generate Editorial Reports" job
3. Expand the red step to see error
4. Common fixes:
   - Re-save DOCX in Word (fixes corruption)
   - Remove special characters from filename

### Report is empty

1. Check DOCX has actual text (not just images)
2. Try re-saving in Word
3. Make sure file isn't password-protected

### Can't see "Run workflow" button

1. Make sure you clicked **"Generate Editorial Reports"** in the LEFT SIDEBAR
   - Not a workflow run in the main list!
2. Use the direct link: https://github.com/CiscoLearning/course-content-testing/actions/workflows/generate-reports.yml
3. Try hard refresh (Ctrl+F5 or Cmd+Shift+R)
4. Try an incognito/private browser window
5. Check you have write access to the repo

### Can't upload files

1. Make sure you're logged into GitHub
2. Check you have write access to the repo
3. Contact Jason if needed

### Converting old .doc files

1. Open in Microsoft Word
2. File → Save As
3. Choose "Word Document (.docx)"
4. Upload the new file

---

## Quick Reference

```
UPLOAD:  github.com/CiscoLearning/course-content-testing
         → uploads/ → Add file → Upload files → Commit

RUN:     Actions tab → Click "Generate Editorial Reports" in LEFT SIDEBAR
         → Run workflow button → Select "both" format → Run workflow

VIEW:    reports/ folder → <filename>-inline-diff.md (recommended)
                        → <filename>-report.md (table format)
```

**Direct workflow link**: https://github.com/CiscoLearning/course-content-testing/actions/workflows/generate-reports.yml

### Report Formats at a Glance

| Format | File Suffix | Shows |
|--------|-------------|-------|
| Inline Diff | `-inline-diff.md` | Full document with ~~deleted~~ **added** markup |
| Table | `-report.md` | Issues grouped by category in tables |

---

## Existing Reports

Check `reports/` folder for examples from the test courses:
- SD-WAN Evolution and Core Concepts
- SD-WAN Components and Roles
- 802.1X EAP Authentication
- And more...

---

## How the Rules Work (Background)

### Where Rules Are Defined

| File | What It Contains | Link |
|------|------------------|------|
| `tools/editorial_rules.yaml` | All editorial rules (terminology, punctuation, style) | [View](https://github.com/CiscoLearning/course-content-testing/blob/main/tools/editorial_rules.yaml) |
| `.claude/references/acronym-database.json` | Acronym expansions and Cisco product naming | [View](https://github.com/CiscoLearning/course-content-testing/blob/main/.claude/references/acronym-database.json) |
| `docs/gap-analysis.md` | Known gaps and planned improvements | [View](https://github.com/CiscoLearning/course-content-testing/blob/main/docs/gap-analysis.md) |

### How We Built the Rules

The editorial rules come from **three sources**:

1. **Cisco Technical Content Style Guide** (stylegd.pdf, August 2022)
   - Official Cisco terminology and branding
   - Product naming conventions
   - Acronym expansion requirements

2. **Human Editor Patterns**
   - Analyzed 100+ PRs edited by Jill (masperli) and Jen (jlauterb-edit)
   - Extracted recurring corrections they made
   - Examples: "click on" → "click", imperative headings, em dash spacing

3. **Gap Analysis from Your Test Courses**
   - Processed the 7 DOCX files you provided
   - Identified 1,576 issues across all courses
   - Found missing acronyms (VXLAN, EAP, MAB, etc.)
   - See [gap-analysis.md](https://github.com/CiscoLearning/course-content-testing/blob/main/docs/gap-analysis.md)

### Rule Categories

| Category | Examples |
|----------|----------|
| **Terminology** | "click on" → "click", "utilize" → "use", "in order to" → "to" |
| **Headings** | Use imperative mood ("Configure X" not "Configuring X") |
| **Acronyms** | Expand on first use, flag unknown acronyms |
| **Punctuation** | Em dashes without spaces, serial commas |
| **Product Naming** | "Cisco Secure Firewall" not "FTD" (deprecated) |
| **GUI Formatting** | Bold for UI elements, code style for commands |

### Acronym Database

The acronym database contains **200+ acronyms** organized by category:

- **cisco_products**: ASA, ISE, NSO, ACI, etc.
- **networking**: VXLAN, BGP, OSPF, MPLS, etc.
- **security**: EAP, MAB, RADIUS, 802.1X, etc.
- **general_tech**: API, CLI, GUI, REST, etc.

Each acronym includes:
- Full expansion
- First-use format (e.g., "Cisco Identity Services Engine (ISE)")
- Whether it's deprecated
- Usage notes

### Providing Feedback on Rules

We need your input! After reviewing reports, please tell us:

1. **Missing rules** - What issues weren't caught?
2. **False positives** - What was incorrectly flagged?
3. **Missing acronyms** - What acronyms need to be added?
4. **Wrong suggestions** - Any fixes that would be incorrect?

**How to provide feedback**:
- Create a [GitHub Issue](https://github.com/CiscoLearning/course-content-testing/issues/new)
- Or email Jason directly with specific examples

---

## Getting Help

| Issue | Contact |
|-------|---------|
| Access problems | Jason (jabelk@cisco.com) |
| Report questions | Jason |
| Feature requests | Create GitHub Issue |

---

*Guide by Jason with Claude Code - March 2026*
