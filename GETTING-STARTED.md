# Getting Started Guide

Welcome! This guide helps you navigate the Course Content Testing repository.

## What is This?

This is an **AI-powered editorial review tool** that checks DOCX course files for style, grammar, and consistency issues. Think of it as an automated editor that catches common problems.

## Where to Find Things

### If You Want To...

| I want to... | Go here |
|--------------|---------|
| **See the editorial reports** | [reports/](reports/) folder - one file per course |
| **Understand what the tool found** | Open any report in `reports/` |
| **Learn what gaps we found** | [docs/gap-analysis.md](docs/gap-analysis.md) |
| **Run the tool myself** | [docs/quickstart.md](docs/quickstart.md) |
| **Understand the architecture** | [docs/learnings.md](docs/learnings.md) |

## Reading the Reports

Each report (in the `reports/` folder) contains:

1. **Quality Score** - Overall rating (1-10)
2. **Summary** - Issue counts by type
3. **Changes by Category** - Organized into 4 groups:
   - Cisco Style Guide
   - Acronyms
   - Technical Terms
   - Chicago Manual (grammar/punctuation)
4. **Detailed Changes** - Every issue sorted by line number

### Understanding Fix Types

| Symbol | Type | What It Means |
|--------|------|---------------|
| 🟢 | SAFE | High confidence - can be auto-fixed |
| 🟡 | REVIEW | Probably correct - please verify |
| 🔴 | QUERY | Not sure - author decides |

## Test Courses

The `test-courses/` folder contains the 7 DOCX files we analyzed:

1. SD-WAN Evolution and Core Concepts
2. SD-WAN Components and Roles
3. 802.1X EAP Authentication
4. 802.1X on Cisco Wireless LAN Controllers
5. AUTOCOR
6. DCNAUTO
7. Network Access for Non-Supplicant Devices

## Questions?

- **Technical questions**: See [docs/learnings.md](docs/learnings.md)
- **What's missing**: See [docs/gap-analysis.md](docs/gap-analysis.md)
- **How to run**: See [docs/quickstart.md](docs/quickstart.md)

## Providing Feedback

After reviewing the reports, we'd love your feedback on:

1. Are the **SAFE** fixes accurate?
2. Any **false positives** (incorrectly flagged)?
3. What issues **weren't caught**?
4. Is the **report format** helpful?

You can:
- Create a GitHub Issue (click "Issues" tab above)
- Email Jason directly
- Add comments in the files
