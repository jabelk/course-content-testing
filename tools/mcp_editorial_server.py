#!/usr/bin/env python3
"""
MCP Editorial Server

Model Context Protocol (MCP) server for editorial validation.
Allows IDEs like Cursor and Claude Code to access editorial tools directly.

Usage:
    # Local stdio transport (for Cursor/Claude Code)
    python mcp_editorial_server.py

    # Network SSE transport (for remote access)
    python mcp_editorial_server.py --transport sse --port 8000

MCP Configuration (for Cursor/Claude Code):
    Add to your MCP settings:
    {
        "mcpServers": {
            "editorial": {
                "command": "python",
                "args": ["/path/to/mcp_editorial_server.py"]
            }
        }
    }

Dependencies:
    pip install fastmcp python-docx pyyaml
"""
import os
import sys
import json
import argparse
from pathlib import Path
from typing import Optional, Dict, Any, List

# Add tools directory to path
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    print("Error: fastmcp not installed. Run: pip install fastmcp", file=sys.stderr)
    sys.exit(1)

# =============================================================================
# Configuration
# =============================================================================

RULES_FILE = os.path.join(script_dir, 'editorial_rules.yaml')
ACRONYM_DB_FILE = os.path.join(script_dir, '..', '.claude', 'references', 'acronym-database.json')

# =============================================================================
# Initialize MCP Server
# =============================================================================

mcp = FastMCP("Editorial Server")

# Cache for loaded resources
_acronym_db: Optional[Dict] = None
_rules: Optional[List] = None


def get_acronym_db() -> Dict:
    """Load and cache acronym database."""
    global _acronym_db
    if _acronym_db is None:
        db_path = os.path.abspath(ACRONYM_DB_FILE)
        if os.path.exists(db_path):
            with open(db_path, 'r', encoding='utf-8') as f:
                _acronym_db = json.load(f)
        else:
            _acronym_db = {}
    return _acronym_db


def get_rules() -> List:
    """Load and cache editorial rules."""
    global _rules
    if _rules is None:
        if os.path.exists(RULES_FILE):
            from editorial_validation import load_rules
            _rules = load_rules(RULES_FILE)
        else:
            _rules = []
    return _rules


# =============================================================================
# MCP Tools
# =============================================================================

@mcp.tool()
def analyze_document(path: str, include_ai: bool = False) -> Dict[str, Any]:
    """
    Analyze a document and return editorial suggestions.

    Validates a DOCX file against editorial rules (Cisco Style Guide,
    Chicago Manual of Style) and returns categorized issues.

    Args:
        path: Path to DOCX file to analyze
        include_ai: Enable AI-enhanced analysis for context-dependent rules

    Returns:
        Dictionary with issues, quality_score, and summary
    """
    from docx_converter import convert_docx_to_markdown, create_temp_tutorial_structure, cleanup_temp_structure
    from editorial_validation import load_rules, validate_tutorial
    from course_models import CourseModule

    # Validate input
    if not os.path.exists(path):
        return {"error": f"File not found: {path}"}

    if not path.lower().endswith('.docx'):
        return {"error": "File must be a .docx file"}

    try:
        # Convert DOCX to markdown
        conversion_result = convert_docx_to_markdown(path, timeout=300)
        if not conversion_result.success:
            return {"error": f"Conversion failed: {conversion_result.error_message}"}

        # Create temp tutorial structure
        course_module = CourseModule.from_docx(path, conversion_result.markdown_content)
        temp_folder, step_file = create_temp_tutorial_structure(
            conversion_result.markdown_content,
            course_module.name
        )

        try:
            # Load rules and validate
            rules = load_rules(RULES_FILE)
            result = validate_tutorial(
                folder_path=temp_folder,
                rules=rules,
                apply_fixes_flag=False,
                use_ai=include_ai,
                verbose=False
            )

            # Format response
            issues_list = []
            for issue in result.issues:
                issues_list.append({
                    "rule_id": issue.rule_id,
                    "line": issue.line_number,
                    "fix_type": issue.fix_type.name if hasattr(issue.fix_type, 'name') else str(issue.fix_type),
                    "message": issue.message,
                    "original": issue.original_text,
                    "suggestion": issue.suggested_fix,
                    "confidence": issue.confidence
                })

            score = result.quality_score
            return {
                "issues": issues_list,
                "quality_score": score.score,
                "summary": {
                    "safe_count": score.safe_count,
                    "review_count": score.review_count,
                    "query_count": score.query_count,
                    "total_issues": score.total_issues
                },
                "interpretation": score.interpretation,
                "word_count": conversion_result.word_count
            }

        finally:
            cleanup_temp_structure(temp_folder)

    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def apply_fixes(path: str, fix_types: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Apply editorial fixes to a document.

    Creates a new DOCX file with track changes showing applied fixes.
    SAFE fixes are applied automatically; REVIEW fixes are marked for
    human verification.

    Args:
        path: Path to DOCX file
        fix_types: Types of fixes to apply. Defaults to ["SAFE"].
                   Options: ["SAFE"], ["SAFE", "REVIEW"]

    Returns:
        Dictionary with fixes_applied count and backup_path
    """
    from docx_converter import convert_docx_to_markdown, create_temp_tutorial_structure, cleanup_temp_structure
    from editorial_validation import load_rules, validate_tutorial
    from course_models import CourseModule
    from docx_track_changes import generate_track_changes_docx

    if fix_types is None:
        fix_types = ["SAFE"]

    # Validate input
    if not os.path.exists(path):
        return {"error": f"File not found: {path}"}

    if not path.lower().endswith('.docx'):
        return {"error": "File must be a .docx file"}

    try:
        # First analyze the document
        conversion_result = convert_docx_to_markdown(path, timeout=300)
        if not conversion_result.success:
            return {"error": f"Conversion failed: {conversion_result.error_message}"}

        course_module = CourseModule.from_docx(path, conversion_result.markdown_content)
        temp_folder, step_file = create_temp_tutorial_structure(
            conversion_result.markdown_content,
            course_module.name
        )

        try:
            rules = load_rules(RULES_FILE)
            result = validate_tutorial(
                folder_path=temp_folder,
                rules=rules,
                apply_fixes_flag=False,
                use_ai=False,
                verbose=False
            )

            # Filter issues by fix type
            filtered_issues = [
                issue for issue in result.issues
                if (issue.fix_type.name if hasattr(issue.fix_type, 'name') else str(issue.fix_type)) in fix_types
            ]

            if not filtered_issues:
                return {
                    "message": "No changes needed",
                    "fixes_applied": 0,
                    "backup_path": None
                }

            # Generate output path
            base = os.path.splitext(path)[0]
            output_path = f"{base}_edited.docx"

            # Create backup
            import shutil
            backup_path = f"{base}_backup.docx"
            shutil.copy2(path, backup_path)

            # Convert issues to expected format
            validation_dict = {
                'issues': [
                    {
                        'original': issue.original_text,
                        'suggestion': issue.suggested_fix,
                        'line': issue.line_number,
                        'rule_id': issue.rule_id,
                        'category': getattr(issue, 'category', 'general'),
                        'fix_type': issue.fix_type.name if hasattr(issue.fix_type, 'name') else str(issue.fix_type),
                        'message': issue.message
                    }
                    for issue in filtered_issues
                ]
            }

            # Generate track changes document
            stats = generate_track_changes_docx(
                path,
                output_path,
                validation_dict,
                author="Editorial AI"
            )

            return {
                "fixes_applied": stats['changes_applied'],
                "comments_added": stats['comments_added'],
                "output_path": output_path,
                "backup_path": backup_path
            }

        finally:
            cleanup_temp_structure(temp_folder)

    except Exception as e:
        return {"error": str(e)}


@mcp.tool()
def lookup_acronym(acronym: str) -> Dict[str, Any]:
    """
    Look up an acronym in the database.

    Returns expansion, usage guidance, and deprecation status
    for known Cisco and networking acronyms.

    Args:
        acronym: Acronym to look up (e.g., "FTD", "VXLAN")

    Returns:
        Dictionary with found status, expansion, and notes
    """
    db = get_acronym_db()
    acronym_upper = acronym.upper()

    # Search across all categories
    categories_to_search = [
        'cisco_products',
        'networking',
        'security',
        'certifications',
        'data_center',
        'security_802.1x',
        'interface_cli',
        'well_established'
    ]

    for category in categories_to_search:
        if category in db:
            if acronym_upper in db[category]:
                entry = db[category][acronym_upper]
                return {
                    "found": True,
                    "acronym": acronym_upper,
                    "category": category,
                    "expansion": entry.get('expansion', ''),
                    "full_name": entry.get('full_name', entry.get('expansion', '')),
                    "first_use": entry.get('first_use', ''),
                    "deprecated": entry.get('deprecated', False),
                    "notes": entry.get('notes', '')
                }

    # Check skip_patterns (course codes, CLI keywords)
    if 'skip_patterns' in db:
        for pattern_type, patterns in db['skip_patterns'].items():
            if acronym_upper in patterns or acronym in patterns:
                return {
                    "found": True,
                    "acronym": acronym,
                    "category": "skip_patterns",
                    "pattern_type": pattern_type,
                    "expansion": None,
                    "notes": f"This is a {pattern_type.replace('_', ' ')} and should not be expanded"
                }

    # Not found
    return {
        "found": False,
        "acronym": acronym,
        "suggestion": "Consider adding this acronym to the database if it's commonly used",
        "submit_url": "https://github.com/CiscoLearning/course-content-testing/issues/new?labels=acronym-request"
    }


@mcp.tool()
def list_rules() -> Dict[str, Any]:
    """
    List all available editorial rules.

    Returns the complete set of editorial rules loaded from
    the configuration, organized by category.

    Returns:
        Dictionary with rules organized by category
    """
    rules = get_rules()

    by_category: Dict[str, List[Dict]] = {}
    for rule in rules:
        category = rule.category or 'uncategorized'
        if category not in by_category:
            by_category[category] = []
        by_category[category].append({
            "id": rule.id,
            "message": rule.message,
            "fix_type": rule.fix_type,
            "enabled": True
        })

    return {
        "total_rules": len(rules),
        "categories": list(by_category.keys()),
        "rules_by_category": by_category
    }


@mcp.tool()
def get_server_info() -> Dict[str, Any]:
    """
    Get information about the MCP Editorial Server.

    Returns version, available tools, and configuration paths.

    Returns:
        Dictionary with server information
    """
    db = get_acronym_db()
    rules = get_rules()

    return {
        "name": "Editorial Server",
        "version": "1.0.0",
        "description": "MCP server for Cisco editorial validation",
        "tools": ["analyze_document", "apply_fixes", "lookup_acronym", "list_rules", "get_server_info"],
        "configuration": {
            "rules_file": RULES_FILE,
            "acronym_db_file": os.path.abspath(ACRONYM_DB_FILE),
            "rules_loaded": len(rules),
            "acronyms_loaded": sum(
                len(v) for k, v in db.items()
                if isinstance(v, dict) and k != '_metadata'
            )
        }
    }


# =============================================================================
# CLI Entry Point
# =============================================================================

def main():
    """Main entry point for MCP server."""
    parser = argparse.ArgumentParser(
        description='MCP Editorial Server for IDE integration'
    )
    parser.add_argument(
        '--transport',
        choices=['stdio', 'sse'],
        default='stdio',
        help='Transport protocol (default: stdio)'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=8000,
        help='Port for SSE transport (default: 8000)'
    )
    parser.add_argument(
        '--host',
        default='localhost',
        help='Host for SSE transport (default: localhost)'
    )

    args = parser.parse_args()

    if args.transport == 'stdio':
        mcp.run()
    else:
        # SSE transport for network access
        mcp.run(transport='sse', host=args.host, port=args.port)


if __name__ == '__main__':
    main()
