# Course Editorial Review - Walkthrough for Kim

**Last Updated**: March 2, 2026

Upload a DOCX file, click a button, get an editorial review report. No coding required!

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
   - **AI suggestions**: Check this box for smarter suggestions (recommended first time)
   - **Verbose logs**: Leave unchecked (unless debugging)
3. Click green **"Run workflow"** button

**Tip**: Try running with AI enabled first to see the full capabilities. If you want faster/deterministic results later, run with AI unchecked.

### 2.3 Wait for completion

- Yellow dot = running (~1-3 minutes)
- Green checkmark = done!
- Red X = error (see Troubleshooting below)

---

## Step 3: View Your Report

### 3.1 Go to reports folder

**Direct link**: https://github.com/CiscoLearning/course-content-testing/tree/main/reports

### 3.2 Find your report

Your report is named: `<your-filename>-report.md`

Example: `SD-WAN_Module_1.docx` → `SD-WAN_Module_1-report.md`

### 3.3 Read the report

Click the file to view. GitHub renders it nicely with tables and formatting.

---

## Understanding the Report

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
4. **Chicago Manual** - Punctuation, grammar, structure

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
         → Run workflow button (right side) → Run workflow

VIEW:    reports/ folder → <filename>-report.md
```

**Direct workflow link**: https://github.com/CiscoLearning/course-content-testing/actions/workflows/generate-reports.yml

---

## Existing Reports

Check `reports/` folder for examples from the test courses:
- SD-WAN Evolution and Core Concepts
- SD-WAN Components and Roles
- 802.1X EAP Authentication
- And more...

---

## Getting Help

| Issue | Contact |
|-------|---------|
| Access problems | Jason (jabelk@cisco.com) |
| Report questions | Jason |
| Feature requests | Create GitHub Issue |

---

*Guide by Jason with Claude Code - March 2026*
