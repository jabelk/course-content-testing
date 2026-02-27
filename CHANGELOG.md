# Changelog

All notable changes to the Course Content Testing tools.

## [1.0.0] - 2026-02-27

### Added

- **Core Pipeline**
  - `course_editor.py` - Main CLI for processing DOCX files
  - Editorial validation with 47+ rules (Cisco Style Guide, Chicago Manual)
  - Quality scoring (1-10) with categorized issue breakdown
  - 100% consistency (0% variance between runs)

- **DOCX Track Changes Output** (Feature 017)
  - `--docx-output` flag generates Word documents with tracked changes
  - SAFE fixes appear as strikethrough + insertion
  - REVIEW/QUERY items appear as Word comments
  - Original document backed up automatically

- **MCP Editorial Server** (Feature 018)
  - `mcp_editorial_server.py` for Cursor/Claude Code integration
  - 5 tools: analyze_document, apply_fixes, lookup_acronym, list_rules, get_server_info
  - Supports stdio (local) and SSE (network) transports

- **Acronym Database**
  - 135 entries across 8 categories
  - Cisco products, networking, security, 802.1X, data center
  - Skip patterns for course codes and CLI keywords

- **Chicago Manual Rules** (16 rules)
  - Serial comma detection
  - Number spelling (1-9 in prose)
  - 8 compound modifier hyphenation rules
  - That vs. which, ampersands, introductory commas

- **Documentation**
  - [Quickstart Guide](docs/quickstart.md)
  - [Setup Guide](docs/setup-guide.md)
  - [Cursor Setup Guide](docs/cursor-setup-guide.md) - For MS Word users
  - [Architecture Decision](docs/architecture-decision.md)
  - [Gap Analysis](docs/gap-analysis.md)

### Test Results

| Course | Issues Found | Quality Score |
|--------|-------------|---------------|
| SD-WAN Evolution | 308 | 1.0/10 |
| SD-WAN Components | 446 | 1.0/10 |
| 802.1X EAP | 294 | 1.0/10 |
| 802.1X Wireless | 390 | 1.0/10 |
| AUTOCOR | 122 | 1.0/10 |
| DCNAUTO | 299 | 1.0/10 |
| Non-Supplicant | 258 | 1.0/10 |

---

## Upcoming

- [ ] Web upload interface (Issue #3)
- [ ] Auto-update rules on startup
- [ ] Batch processing with parallel execution
