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

# Hot reload support - auto-reloads rules/acronyms when files change
from hot_reload import RulesReloader
_reloader = RulesReloader(
    rules_path=RULES_FILE,
    acronym_path=ACRONYM_DB_FILE,
    check_interval=5.0  # Check for changes every 5 seconds
)


def get_acronym_db() -> Dict:
    """Load acronym database with hot reload support."""
    return _reloader.get_acronyms()


def get_rules() -> List:
    """Load editorial rules with hot reload support."""
    return _reloader.get_rules()


# =============================================================================
# MCP Tools
# =============================================================================

@mcp.tool()
def analyze_document(path: str, include_ai: bool = False) -> Dict[str, Any]:
    """
    Analyze a document and return editorial suggestions.

    Validates a DOCX file against editorial rules (Cisco Style Guide,
    Grammar & Punctuation) and returns categorized issues.

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
    status = _reloader.get_status()

    return {
        "name": "Editorial Server",
        "version": "1.0.0",
        "description": "MCP server for Cisco editorial validation",
        "tools": ["analyze_document", "apply_fixes", "lookup_acronym", "list_rules", "reload_rules", "get_server_info"],
        "configuration": {
            "rules_file": RULES_FILE,
            "acronym_db_file": os.path.abspath(ACRONYM_DB_FILE),
            "rules_loaded": len(rules),
            "acronyms_loaded": sum(
                len(v) for k, v in db.items()
                if isinstance(v, dict) and k != '_metadata'
            ),
            "hot_reload": {
                "enabled": True,
                "check_interval_seconds": _reloader.check_interval,
                "rules_last_modified": status['rules']['last_modified'],
                "acronyms_last_modified": status['acronyms']['last_modified']
            }
        }
    }


@mcp.tool()
def reload_rules() -> Dict[str, Any]:
    """
    Force reload of editorial rules and acronym database.

    Use this after updating rules or acronyms to immediately
    pick up changes without waiting for the automatic reload.

    Returns:
        Dictionary with reload status and updated counts
    """
    result = _reloader.reload_all()
    status = _reloader.get_status()

    return {
        "success": result['rules'] and result['acronyms'],
        "rules": {
            "reloaded": result['rules'],
            "count": status['rules']['count'],
            "error": status['rules']['error']
        },
        "acronyms": {
            "reloaded": result['acronyms'],
            "count": status['acronyms']['count'],
            "error": status['acronyms']['error']
        }
    }


# =============================================================================
# Onboarding & Trust-Building Tools
# =============================================================================

@mcp.tool()
def get_started() -> Dict[str, Any]:
    """
    Get started with the Editorial AI tools.

    New to this tool? Start here! This guide walks you through
    what the tool does and how to use it step by step.

    Returns:
        Welcome message with step-by-step instructions
    """
    return {
        "welcome": "Welcome to the Editorial AI Assistant!",
        "what_this_does": (
            "This tool helps you review course documents for editorial issues - "
            "things like style guide violations, acronym usage, punctuation, and grammar. "
            "It's based on the same rules our human editors use."
        ),
        "how_it_works": [
            "1. You give it a Word document (.docx file)",
            "2. It scans for issues using 47+ editorial rules",
            "3. It categorizes each issue by confidence level",
            "4. You review the suggestions and decide what to change"
        ],
        "fix_types_explained": {
            "SAFE": {
                "meaning": "High confidence - these are almost certainly correct",
                "confidence": "95%+",
                "action": "You can usually accept these without review",
                "examples": ["'datacenter' → 'data center'", "'make sure' → 'ensure'"]
            },
            "REVIEW": {
                "meaning": "Medium confidence - likely correct but please verify",
                "confidence": "70-95%",
                "action": "Look at the context before accepting",
                "examples": ["Hyphenation suggestions", "Number formatting"]
            },
            "QUERY": {
                "meaning": "Needs your judgment - the tool isn't sure",
                "confidence": "<70%",
                "action": "You decide - these are questions, not corrections",
                "examples": ["Unknown acronyms", "Ambiguous phrasing"]
            }
        },
        "quick_start": [
            "Step 1: Say 'analyze my document at /path/to/file.docx'",
            "Step 2: Review the quality score and issue summary",
            "Step 3: Ask 'explain issue TERM_DATACENTER' for any confusing rule",
            "Step 4: Say 'apply SAFE fixes to /path/to/file.docx' to auto-fix high-confidence items"
        ],
        "tips": [
            "Start with a short document to get familiar",
            "The quality score is 1-10 (higher is better)",
            "You can always ask 'what does [rule_id] mean?' for any rule",
            "Your original file is never modified - we create a backup"
        ],
        "try_this_now": "Say: 'analyze the document at [your file path]'"
    }


@mcp.tool()
def explain_issue(rule_id: str) -> Dict[str, Any]:
    """
    Explain what a specific rule means and why it matters.

    Confused about why something was flagged? Use this to understand
    the rule, see examples, and learn the style guide reference.

    Args:
        rule_id: The rule ID to explain (e.g., 'TERM_DATACENTER', 'CMS_SERIAL_COMMA')

    Returns:
        Detailed explanation with examples and references
    """
    # Rule explanations with context
    explanations = {
        # Terminology rules
        "TERM_DATACENTER": {
            "rule": "Use 'data center' (two words)",
            "why": "Cisco Style Guide specifies 'data center' as two words, not 'datacenter' or 'data-center'.",
            "category": "Cisco Style Guide",
            "confidence": "SAFE (95%+)",
            "example": {
                "before": "Our datacenter hosts 500 servers.",
                "after": "Our data center hosts 500 servers."
            },
            "reference": "Cisco Technical Content Style Guide, Section: Terminology"
        },
        "TERM_MAKE_SURE": {
            "rule": "Use 'ensure' instead of 'make sure'",
            "why": "'Ensure' is more formal and preferred in technical documentation.",
            "category": "Cisco Style Guide",
            "confidence": "SAFE (95%+)",
            "example": {
                "before": "Make sure the cable is connected.",
                "after": "Ensure the cable is connected."
            },
            "reference": "Cisco Technical Content Style Guide"
        },
        # Chicago Manual rules
        "GRAMMAR_SERIAL_COMMA": {
            "rule": "Use serial comma (Oxford comma) in lists",
            "why": "The serial comma before 'and' in a list prevents ambiguity.",
            "category": "Grammar & Punctuation",
            "confidence": "REVIEW (85%)",
            "example": {
                "before": "Configure routing, switching and security.",
                "after": "Configure routing, switching, and security."
            },
            "reference": "Grammar & Punctuation, 17th ed., Section 6.19"
        },
        "GRAMMAR_NUMBER_SPELL_OUT": {
            "rule": "Spell out numbers one through nine",
            "why": "In prose, small numbers are typically spelled out for readability.",
            "category": "Grammar & Punctuation",
            "confidence": "REVIEW (80%)",
            "example": {
                "before": "Configure 3 interfaces.",
                "after": "Configure three interfaces."
            },
            "note": "Exception: Keep numerals in technical contexts like 'port 3' or 'VLAN 3'",
            "reference": "Grammar & Punctuation, 17th ed., Section 9.3"
        },
        # Punctuation rules
        "PUNCT_EM_DASH_SPACE": {
            "rule": "No spaces around em dashes",
            "why": "Em dashes (—) should connect directly to the words they separate.",
            "category": "Grammar & Punctuation",
            "confidence": "SAFE (95%+)",
            "example": {
                "before": "The router — which is new — failed.",
                "after": "The router—which is new—failed."
            },
            "reference": "Grammar & Punctuation, 17th ed., Section 6.85"
        },
        "PUNCT_DOUBLE_SPACE": {
            "rule": "Use single space after periods",
            "why": "Modern typography uses single spacing. Double spaces are a typewriter-era convention.",
            "category": "Typography",
            "confidence": "SAFE (99%)",
            "example": {
                "before": "End of sentence.  Start of next.",
                "after": "End of sentence. Start of next."
            },
            "reference": "Grammar & Punctuation, 17th ed., Section 6.7"
        },
        # Compound modifiers
        "GRAMMAR_COMPOUND_WELL_KNOWN": {
            "rule": "Hyphenate 'well-known' before a noun",
            "why": "Compound modifiers before a noun are hyphenated for clarity.",
            "category": "Grammar & Punctuation",
            "confidence": "SAFE (90%)",
            "example": {
                "before": "This is a well known issue.",
                "after": "This is a well-known issue."
            },
            "note": "Don't hyphenate after the noun: 'The issue is well known.'",
            "reference": "Grammar & Punctuation, 17th ed., Section 7.81"
        },
        # Acronyms
        "ACRONYM_UNKNOWN": {
            "rule": "Unknown acronym needs expansion",
            "why": "Readers may not know this acronym. Consider spelling it out on first use.",
            "category": "Acronym Usage",
            "confidence": "QUERY (50%)",
            "example": {
                "before": "Configure the XYZ protocol.",
                "after": "Configure the Extended Yellowtail Zone (XYZ) protocol."
            },
            "what_to_do": [
                "If it's a common acronym, we may need to add it to our database",
                "If it's course-specific, spell it out on first use",
                "If it's a product name or code, it might be fine as-is"
            ],
            "reference": "Cisco Style Guide: Acronym Policy"
        }
    }

    rule_upper = rule_id.upper()

    if rule_upper in explanations:
        explanation = explanations[rule_upper]
        explanation["rule_id"] = rule_upper
        explanation["found"] = True
        return explanation
    else:
        # Try to find partial match
        matches = [r for r in explanations.keys() if rule_upper in r or r in rule_upper]

        return {
            "found": False,
            "rule_id": rule_id,
            "message": f"No detailed explanation available for '{rule_id}'.",
            "similar_rules": matches[:5] if matches else [],
            "tip": "Try 'list_rules' to see all available rules with their categories.",
            "help": "If you need this rule explained, let us know and we'll add documentation."
        }


@mcp.tool()
def suggest_workflow(document_path: Optional[str] = None) -> Dict[str, Any]:
    """
    Get a personalized workflow suggestion based on your document.

    Not sure what to do next? This tool analyzes your situation
    and recommends the best next steps.

    Args:
        document_path: Optional path to document (for context-aware suggestions)

    Returns:
        Recommended workflow with explanations
    """
    if document_path and os.path.exists(document_path):
        # Analyze the document first
        result = analyze_document(document_path, include_ai=False)

        if "error" in result:
            return {
                "status": "error",
                "message": result["error"],
                "suggestion": "Check the file path and try again."
            }

        score = result.get("quality_score", 5)
        summary = result.get("summary", {})
        safe_count = summary.get("safe_count", 0)
        review_count = summary.get("review_count", 0)
        query_count = summary.get("query_count", 0)

        # Personalized recommendation based on results
        if score >= 8:
            recommendation = {
                "assessment": "Your document is in great shape!",
                "quality_score": score,
                "recommended_steps": [
                    "1. Review the few issues found (if any)",
                    "2. Apply SAFE fixes if you agree with them",
                    "3. Your document is nearly ready for publication"
                ]
            }
        elif score >= 5:
            recommendation = {
                "assessment": "Your document needs some attention but is solid.",
                "quality_score": score,
                "recommended_steps": [
                    f"1. Apply the {safe_count} SAFE fixes (high confidence)",
                    f"2. Review the {review_count} REVIEW items carefully",
                    f"3. Address the {query_count} QUERY items (your judgment needed)",
                    "4. Re-run analysis to see your improved score"
                ]
            }
        else:
            recommendation = {
                "assessment": "Your document has several areas to improve.",
                "quality_score": score,
                "recommended_steps": [
                    f"1. Start with SAFE fixes ({safe_count} items) - these are quick wins",
                    "2. Use 'explain_issue [rule_id]' for any confusing rules",
                    f"3. Work through REVIEW items ({review_count}) one section at a time",
                    f"4. Handle QUERY items ({query_count}) last - these need your expertise",
                    "5. Re-run analysis after each batch of fixes to track progress"
                ],
                "tip": "Don't try to fix everything at once. Focus on one category at a time."
            }

        recommendation["summary"] = summary
        recommendation["next_command"] = f"apply_fixes('{document_path}', fix_types=['SAFE'])" if safe_count > 0 else "Review complete - no SAFE fixes needed"
        return recommendation

    else:
        # General workflow without a specific document
        return {
            "welcome": "Here's the recommended editorial review workflow:",
            "workflow": [
                {
                    "step": 1,
                    "action": "Analyze your document",
                    "command": "analyze_document('/path/to/your/file.docx')",
                    "what_happens": "Scans for issues and gives you a quality score"
                },
                {
                    "step": 2,
                    "action": "Review the summary",
                    "what_to_look_for": [
                        "Quality score (1-10, higher is better)",
                        "Count of SAFE vs REVIEW vs QUERY issues"
                    ]
                },
                {
                    "step": 3,
                    "action": "Apply SAFE fixes",
                    "command": "apply_fixes('/path/to/your/file.docx')",
                    "what_happens": "Creates a new file with tracked changes for high-confidence fixes"
                },
                {
                    "step": 4,
                    "action": "Review in Word",
                    "what_to_do": "Open the _edited.docx file and use Track Changes to accept/reject"
                },
                {
                    "step": 5,
                    "action": "Handle REVIEW and QUERY items",
                    "tip": "Use 'explain_issue [rule_id]' if you're unsure about any suggestion"
                }
            ],
            "tips": [
                "Your original file is never modified - we always create a backup",
                "Start with a small document to get comfortable",
                "The tool learns from our human editors' patterns"
            ]
        }


@mcp.tool()
def check_acronym_batch(acronyms: List[str]) -> Dict[str, Any]:
    """
    Check multiple acronyms at once.

    Reviewing a document with many acronyms? Check them all at once
    to see which ones are known and which need attention.

    Args:
        acronyms: List of acronyms to check (e.g., ["VXLAN", "BGP", "XYZ"])

    Returns:
        Status of each acronym with usage guidance
    """
    results = {
        "known": [],
        "unknown": [],
        "deprecated": [],
        "skip": []
    }

    for acronym in acronyms:
        info = lookup_acronym(acronym)

        if not info.get("found"):
            results["unknown"].append({
                "acronym": acronym,
                "action": "Consider spelling out on first use"
            })
        elif info.get("category") == "skip_patterns":
            results["skip"].append({
                "acronym": acronym,
                "reason": info.get("notes", "Skip pattern - no expansion needed")
            })
        elif info.get("deprecated"):
            results["deprecated"].append({
                "acronym": acronym,
                "expansion": info.get("expansion"),
                "note": info.get("notes"),
                "action": "Use the full product name instead"
            })
        else:
            results["known"].append({
                "acronym": acronym,
                "expansion": info.get("expansion"),
                "first_use": info.get("first_use", info.get("expansion"))
            })

    return {
        "total_checked": len(acronyms),
        "summary": {
            "known": len(results["known"]),
            "unknown": len(results["unknown"]),
            "deprecated": len(results["deprecated"]),
            "skip": len(results["skip"])
        },
        "results": results,
        "tip": "For unknown acronyms, either spell them out or request they be added to the database."
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
