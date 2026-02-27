# Course Content Testing - Docker Image
#
# Build: docker build -t course-content-testing .
# Run:   docker run -v $(pwd)/docs:/app/input course-content-testing input/course.docx
#
# For MCP SSE mode:
#   docker run -p 8000:8000 course-content-testing --mcp-server --port 8000

FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    pandoc \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY tools/ ./tools/
COPY .claude/references/ ./.claude/references/

# Create directories for input/output
RUN mkdir -p /app/input /app/output /app/data

# Volume mounts:
# - /app/input: Place DOCX files here
# - /app/output: Reports written here
# - /app/data/rules: Custom editorial_rules.yaml (optional)
# - /app/data/acronyms: Custom acronym-database.json (optional)
VOLUME ["/app/input", "/app/output", "/app/data"]

# Environment variables for configuration
ENV RULES_FILE=/app/data/rules/editorial_rules.yaml
ENV ACRONYM_DB=/app/data/acronyms/acronym-database.json
ENV PYTHONUNBUFFERED=1

# Copy entrypoint script
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# Default: run as CLI
ENTRYPOINT ["/docker-entrypoint.sh"]

# Default command (can be overridden)
CMD ["--help"]

# Health check for SSE mode
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Expose port for SSE mode
EXPOSE 8000
