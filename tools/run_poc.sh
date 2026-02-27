#!/bin/bash
#
# Course AI Editing - PoC Runner Script
#
# Processes all test courses and generates reports.
# Usage: ./run_poc.sh [options]
#
# Options:
#   --help        Show this help message
#   --verbose     Show detailed output for each course
#   --json        Generate JSON output instead of markdown
#   --consistency Run consistency tests on each course
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPEC_DIR="$(cd "$SCRIPT_DIR/../../specs/014-course-ai-editing" && pwd)"
TEST_COURSES_DIR="$SPEC_DIR/Test Courses"
REPORTS_DIR="$SPEC_DIR/reports"

# Parse arguments
VERBOSE=""
JSON=""
CONSISTENCY=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --help|-h)
            echo "Course AI Editing - PoC Runner"
            echo ""
            echo "Usage: $0 [options]"
            echo ""
            echo "Options:"
            echo "  --help, -h        Show this help message"
            echo "  --verbose, -v     Show detailed output for each course"
            echo "  --json            Generate JSON output instead of markdown"
            echo "  --consistency     Run consistency tests on each course"
            exit 0
            ;;
        --verbose|-v)
            VERBOSE="--verbose"
            shift
            ;;
        --json)
            JSON="--json"
            shift
            ;;
        --consistency)
            CONSISTENCY="1"
            shift
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Create reports directory
mkdir -p "$REPORTS_DIR"

echo "============================================================"
echo "Course AI Editing - PoC Test Runner"
echo "============================================================"
echo ""
echo "Test Courses: $TEST_COURSES_DIR"
echo "Reports Dir:  $REPORTS_DIR"
echo ""

# Count courses
COURSE_COUNT=$(ls -1 "$TEST_COURSES_DIR"/*.docx 2>/dev/null | wc -l | tr -d ' ')
echo "Found $COURSE_COUNT test courses"
echo ""

# Track summary
TOTAL_ISSUES=0
TOTAL_TIME=0
declare -a COURSE_RESULTS

# Process each course
for docx in "$TEST_COURSES_DIR"/*.docx; do
    if [ ! -f "$docx" ]; then
        continue
    fi

    name=$(basename "$docx" .docx)
    echo "Processing: $name"

    # Determine output extension
    if [ -n "$JSON" ]; then
        output_file="$REPORTS_DIR/${name}-report.json"
        flags="--json"
    else
        output_file="$REPORTS_DIR/${name}-report.md"
        flags=""
    fi

    # Add verbose flag if set
    if [ -n "$VERBOSE" ]; then
        flags="$flags --verbose"
    fi

    # Run course editor
    start_time=$(python3 -c "import time; print(int(time.time() * 1000))")

    if python3 "$SCRIPT_DIR/course_editor.py" "$docx" --no-ai --output "$output_file" $flags 2>&1; then
        end_time=$(python3 -c "import time; print(int(time.time() * 1000))")
        duration=$((end_time - start_time))

        # Extract issue count from report
        if [ -n "$JSON" ]; then
            issues=$(python3 -c "import json; d=json.load(open('$output_file')); print(d['validation']['quality_score']['total_issues'])" 2>/dev/null || echo "0")
        else
            issues=$(grep "Total Issues" "$output_file" | head -1 | grep -o '[0-9]*' | head -1 || echo "0")
        fi

        echo "  -> Done: $issues issues in ${duration}ms"

        TOTAL_ISSUES=$((TOTAL_ISSUES + issues))
        TOTAL_TIME=$((TOTAL_TIME + duration))
        COURSE_RESULTS+=("$name: $issues issues")
    else
        echo "  -> ERROR: Processing failed"
        COURSE_RESULTS+=("$name: FAILED")
    fi

    # Run consistency test if requested
    if [ -n "$CONSISTENCY" ]; then
        echo "  -> Running consistency test..."
        python3 "$SCRIPT_DIR/test_consistency.py" "$docx" --runs 3 2>&1 | grep -E "(RESULT|OVERALL)" || true
    fi

    echo ""
done

echo "============================================================"
echo "SUMMARY"
echo "============================================================"
echo ""
echo "Courses Processed: $COURSE_COUNT"
echo "Total Issues:      $TOTAL_ISSUES"
echo "Total Time:        ${TOTAL_TIME}ms ($(echo "scale=1; $TOTAL_TIME / 1000" | bc)s)"
echo ""
echo "Results by Course:"
for result in "${COURSE_RESULTS[@]}"; do
    echo "  - $result"
done
echo ""
echo "Reports saved to: $REPORTS_DIR"
