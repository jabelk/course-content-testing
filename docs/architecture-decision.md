# Architecture Decision: Hybrid Editorial System

**Date**: 2026-02-27
**Status**: Decided

## Summary

The editorial AI system uses a **hybrid architecture**:
- **Git-Centralized** for rules and acronym databases
- **Processing-Distributed** across CLI, MCP, and (future) web interfaces

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Git Repository (Source of Truth)                  │
│  ┌─────────────────────┐  ┌─────────────────────┐                   │
│  │ editorial_rules.yaml│  │acronym-database.json│                   │
│  └─────────────────────┘  └─────────────────────┘                   │
└──────────────────────────────┬──────────────────────────────────────┘
                               │ git pull / fetch
          ┌────────────────────┼────────────────────┐
          │                    │                    │
          ▼                    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│   CLI Mode      │  │  MCP Server     │  │  Web Interface  │
│                 │  │                 │  │   (Future)      │
│ course_editor.py│  │ mcp_editorial_  │  │                 │
│                 │  │ server.py       │  │                 │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

## Decision Rationale

### Why Not Pure Local?

- Rules would drift between users
- Updates require manual distribution
- No single source of truth

### Why Not Pure Centralized?

- Server infrastructure costs
- Network dependency
- Security review overhead
- Overkill for CLI power users

### Why Hybrid Works

| Benefit | How It's Achieved |
|---------|-------------------|
| Consistency | All pull from same Git repo |
| Offline support | CLI/MCP work without network |
| Low cost | No always-on server |
| Easy updates | `git pull` gets latest rules |
| Flexibility | Multiple interfaces, same rules |

## Current Implementation

| Interface | Status | Use Case |
|-----------|--------|----------|
| CLI (`course_editor.py`) | Done | Power users, automation |
| DOCX Track Changes | Done | SME review workflow |
| MCP Server | Done | Cursor/Claude Code integration |
| Web Interface | Not started | Non-technical users |

## How to Stay Current

```bash
# Before processing documents, update rules
cd course-content-testing
git pull origin main

# Then run your preferred interface
python3 tools/course_editor.py your-course.docx
```

## Future Considerations

If centralization becomes necessary:

1. MCP server already supports SSE transport for network deployment
2. Can add authentication wrapper
3. Can add central telemetry

---

*This decision supersedes any previous discussions about pure local or pure centralized approaches.*
