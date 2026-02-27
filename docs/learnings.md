# Implementation Learnings: Course AI Editing

**Feature**: 014-course-ai-editing
**Date**: 2026-02-27
**Author**: Jason (with Claude assistance)

## Summary

Successfully implemented a PoC for adapting the tutorial AI editorial pipeline to process DOCX course content for Kim's LWC team. The key differentiator from Circuit: **100% consistent results** (0% variance vs Circuit's 50%+ variance).

## What Worked Well

### 1. Reusing Existing Infrastructure

The tutorial editorial pipeline (`editorial_validation.py`, `editorial_rules.yaml`, `acronym_detector.py`) required minimal modification. Strategy:

- Created wrapper modules (`course_models.py`, `docx_converter.py`) instead of modifying originals
- Used temp directory structure to mimic `tc-*/step-*.md` format expected by validation
- Category mapping as a translation layer rather than changing rule definitions

**Lesson**: When adapting existing tools for new use cases, prefer wrapper/adapter patterns over modification.

### 2. Pandoc for DOCX Conversion

Pandoc proved extremely reliable:
- Deterministic output (critical for consistency requirement)
- Handles complex DOCX formatting (tables, images, nested lists)
- Fast: ~200ms for 10,000 word documents
- Subprocess wrapper pattern made error handling straightforward

**Lesson**: For document conversion, use battle-tested tools (pandoc, libreoffice) rather than Python libraries (python-docx).

### 3. Spec-Driven Development with Speckit

The speckit workflow (`/specify` → `/plan` → `/tasks` → `/implement`) provided:
- Clear requirements before coding
- Task breakdown that parallelized well
- Checklists that identified gaps early
- Documentation artifacts alongside implementation

**Lesson**: Time invested in specification pays off in reduced rework.

### 4. Quality Checklists

Creating focused checklists (editorial-accuracy, report-quality, consistency) before implementation:
- Identified 60 specific requirements to validate
- Surfaced gaps early (acronym database, category mapping)
- Provided clear "done" criteria
- Final score: 72% complete (acceptable for PoC)

**Lesson**: Checklists transform vague requirements into testable criteria.

## Challenges Encountered

### 1. Acronym Database Coverage

**Problem**: Course content uses many acronyms not in tutorial acronym database.

**Examples**:
- Data center: VXLAN, VTEP, POAP, NX-OS
- Security: EAP, MAB, 802.1X, RADIUS
- Course codes: DCNAUTO, AUTOCOR (not acronyms, just identifiers)

**Solution**: Flagged unknown acronyms as QUERY for author review. Documented in gap-analysis.md for future expansion.

**Lesson**: Domain-specific content requires domain-specific rules. Plan for iterative rule expansion.

### 2. Section Parsing

**Problem**: Course content has different structure than tutorials.
- Tutorials: Clear `step-*.md` boundaries
- Courses: Long-form with many sub-sections, no clear breaks

**Current approach**: Treat entire document as single section.

**Future improvement**: Parse heading hierarchy (H1 > H2 > H3) to identify logical sections.

**Lesson**: Content structure assumptions from one domain don't transfer directly to another.

### 3. Line Number Reference

**Problem**: Line numbers in reports reference converted markdown, not original DOCX.

**Impact**: Kim needs to mentally map report line numbers to DOCX locations.

**Future solution**: DOCX track changes output would eliminate this issue.

**Lesson**: Output format should match user's review workflow, not implementation convenience.

### 4. Category Mapping Granularity

**Problem**: Some rules don't cleanly map to Kim's 4 categories.

**Example**: `PUNCT_EXCLAMATION_IN_PROSE`
- Chicago Manual says: use sparingly
- Cisco Style Guide says: avoid in technical content
- Mapped to Chicago Manual, but really Cisco-specific

**Solution**: Created mapping table in `course_models.py` with special cases.

**Lesson**: Real-world categorization is messier than spec categories. Build in flexibility.

## Performance Results

| Metric | Target | Achieved |
|--------|--------|----------|
| Consistency variance | <5% | 0% (fully deterministic) |
| Processing time (2h content) | <10 min | <2 seconds |
| Auto-fixable rate | 85% | 60% SAFE, 15% REVIEW |
| Quality score variance | <5% | 0% |

## Architecture Decisions

### Why Wrapper Pattern?

```
DOCX → docx_converter.py → CourseModule
                               ↓
                     temp tc-*/step-1.md structure
                               ↓
                     editorial_validation.py (unchanged)
                               ↓
                     ValidationResult
                               ↓
                     course_report_generator.py → Report
```

Benefits:
- Zero changes to existing tutorial pipeline
- Easy to extend or replace any component
- Clear separation of concerns

### Why Markdown Report First?

Kim requested DOCX track changes, but we chose markdown for PoC:
1. Faster to implement (no DOCX manipulation libraries)
2. Easier to debug (human-readable output)
3. Works in any text editor
4. Can iterate on format before investing in DOCX output

**Future**: Add python-docx integration for track changes output.

## Recommendations for Production

### High Priority

1. **Expand Acronym Database**
   - Add 50+ networking/security/data center acronyms
   - Add course code ignore patterns
   - Estimated effort: 2-4 hours

2. **DOCX Track Changes Output**
   - Use python-docx to apply changes with track changes
   - Include rationale as comments
   - Estimated effort: 8-16 hours

3. **Batch Processing**
   - Process multiple courses in parallel
   - Generate summary report across courses
   - Estimated effort: 2-4 hours

### Medium Priority

4. **Section Parsing Enhancement**
   - Parse heading hierarchy
   - Calculate per-section word counts
   - Map issues to logical sections

5. **AI Enhancement Testing**
   - Enable AI for context-sensitive rules
   - Measure consistency impact
   - Tune prompts for course content

### Low Priority

6. **Integration Options**
   - Confluence plugin
   - SharePoint integration
   - Slack bot for submissions

## Files Created

| File | Purpose |
|------|---------|
| `course_models.py` | CourseModule, Section, ChangeReport dataclasses |
| `docx_converter.py` | Pandoc subprocess wrapper |
| `course_editor.py` | Main CLI entry point |
| `course_report_generator.py` | Markdown report generation |
| `test_consistency.py` | Consistency validation |
| `run_poc.sh` | Batch processing script |
| `gap-analysis.md` | Rule gaps documentation |
| `learnings.md` | This file |

## Metrics for Success Review

When Kim reviews the PoC reports, gather feedback on:

1. **Usefulness**: Are the SAFE suggestions accurate?
2. **Noise level**: Too many false positives?
3. **Missing rules**: What issues weren't caught?
4. **Report format**: Easy to navigate?
5. **Category mapping**: Do the 4 categories make sense?

## Conclusion

The PoC demonstrates that:
- Existing tutorial pipeline can adapt to course content
- DOCX conversion via pandoc is reliable and fast
- 100% consistency (vs Circuit's 50%+ variance) is achievable
- ~70% of checklist requirements met in first iteration

Next steps depend on Kim's feedback on the generated reports.
