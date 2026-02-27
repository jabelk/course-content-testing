#!/bin/bash
set -e

# Course Content Testing - Docker Entrypoint
#
# Modes:
#   CLI:        docker run <image> /app/input/course.docx
#   MCP Server: docker run <image> --mcp-server [--port 8000]
#   Shell:      docker run -it <image> --shell

# Use custom rules if mounted, otherwise use defaults
if [ ! -f "$RULES_FILE" ]; then
    export RULES_FILE=/app/tools/editorial_rules.yaml
fi

if [ ! -f "$ACRONYM_DB" ]; then
    export ACRONYM_DB=/app/.claude/references/acronym-database.json
fi

# Parse arguments
case "$1" in
    --mcp-server)
        shift
        echo "Starting MCP Editorial Server (SSE mode)..."
        exec python3 /app/tools/mcp_editorial_server.py --transport sse "$@"
        ;;
    --shell)
        exec /bin/bash
        ;;
    --help)
        cat << 'EOF'
Course Content Testing - Docker Container

Usage:
  docker run <image> /app/input/course.docx [OPTIONS]
  docker run <image> --mcp-server [--port 8000]
  docker run -it <image> --shell

Options for course_editor.py:
  --output, -o    Output path for report
  --json          Output as JSON
  --docx-output   Generate DOCX with track changes
  --no-ai         Disable AI enhancement
  --verbose       Show detailed processing

Volume Mounts:
  /app/input      Place DOCX files here
  /app/output     Reports written here
  /app/data/rules Custom editorial_rules.yaml
  /app/data/acronyms Custom acronym-database.json

Examples:
  # Process a course
  docker run -v $(pwd):/app/input <image> /app/input/course.docx

  # Generate DOCX with track changes
  docker run -v $(pwd):/app/input -v $(pwd)/out:/app/output \
    <image> /app/input/course.docx --docx-output -o /app/output/

  # Start MCP server
  docker run -p 8000:8000 <image> --mcp-server --port 8000

  # Use custom rules
  docker run -v $(pwd)/my-rules.yaml:/app/data/rules/editorial_rules.yaml \
    <image> /app/input/course.docx
EOF
        exit 0
        ;;
    *)
        # Default: run course_editor.py
        exec python3 /app/tools/course_editor.py "$@"
        ;;
esac
