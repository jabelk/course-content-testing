"""
DOCX to Markdown Converter

Provides pandoc-based conversion of DOCX files to markdown format.
Used by the course AI editing pipeline to process course modules.

Features:
- Subprocess wrapper for pandoc with timeout handling
- Error detection and reporting
- Temporary file management
- Conversion validation
"""
import subprocess
import tempfile
import os
import shutil
from typing import Tuple, Optional
from dataclasses import dataclass


@dataclass
class ConversionResult:
    """
    Result of a DOCX to markdown conversion.

    Attributes:
        success: Whether conversion succeeded
        markdown_content: Converted markdown text (if successful)
        error_message: Error description (if failed)
        source_path: Original DOCX file path
        word_count: Approximate word count of converted content
    """
    success: bool
    markdown_content: str
    error_message: str
    source_path: str
    word_count: int = 0

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization"""
        return {
            'success': self.success,
            'markdown_content': self.markdown_content if self.success else '',
            'error_message': self.error_message,
            'source_path': self.source_path,
            'word_count': self.word_count
        }


def check_pandoc_installed() -> Tuple[bool, str]:
    """
    Check if pandoc is installed and accessible.

    Returns:
        Tuple of (is_installed, version_or_error)
    """
    try:
        result = subprocess.run(
            ['pandoc', '--version'],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            # Extract version from first line
            version_line = result.stdout.split('\n')[0]
            return True, version_line
        return False, result.stderr or 'Unknown error'
    except FileNotFoundError:
        return False, 'pandoc not found in PATH. Install with: brew install pandoc (macOS) or apt-get install pandoc (Linux)'
    except subprocess.TimeoutExpired:
        return False, 'pandoc version check timed out'
    except Exception as e:
        return False, f'Error checking pandoc: {str(e)}'


def convert_docx_to_markdown(
    docx_path: str,
    timeout: int = 300,
    preserve_tables: bool = True,
    extract_media: bool = False
) -> ConversionResult:
    """
    Convert a DOCX file to markdown using pandoc.

    Args:
        docx_path: Path to the DOCX file
        timeout: Maximum conversion time in seconds (default 5 minutes)
        preserve_tables: Keep table formatting (default True)
        extract_media: Extract embedded images to temp folder (default False)

    Returns:
        ConversionResult with markdown content or error
    """
    # Validate input file exists
    if not os.path.exists(docx_path):
        return ConversionResult(
            success=False,
            markdown_content='',
            error_message=f'DOCX file not found: {docx_path}',
            source_path=docx_path
        )

    # Validate it's a DOCX file
    if not docx_path.lower().endswith('.docx'):
        return ConversionResult(
            success=False,
            markdown_content='',
            error_message=f'Not a DOCX file: {docx_path}',
            source_path=docx_path
        )

    # Check pandoc is available
    pandoc_ok, pandoc_msg = check_pandoc_installed()
    if not pandoc_ok:
        return ConversionResult(
            success=False,
            markdown_content='',
            error_message=pandoc_msg,
            source_path=docx_path
        )

    # Build pandoc command
    cmd = [
        'pandoc',
        docx_path,
        '-f', 'docx',
        '-t', 'markdown',
        '--wrap=none',  # Don't wrap lines
    ]

    if preserve_tables:
        cmd.extend(['--markdown-headings=atx'])  # Use # style headings

    # Handle media extraction
    media_dir = None
    if extract_media:
        media_dir = tempfile.mkdtemp(prefix='docx_media_')
        cmd.extend(['--extract-media', media_dir])

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        if result.returncode != 0:
            return ConversionResult(
                success=False,
                markdown_content='',
                error_message=f'Pandoc conversion failed: {result.stderr}',
                source_path=docx_path
            )

        markdown_content = result.stdout

        # Validate we got some content
        if not markdown_content.strip():
            return ConversionResult(
                success=False,
                markdown_content='',
                error_message='Pandoc produced empty output - DOCX may be empty or corrupted',
                source_path=docx_path
            )

        # Calculate word count
        word_count = len(markdown_content.split())

        return ConversionResult(
            success=True,
            markdown_content=markdown_content,
            error_message='',
            source_path=docx_path,
            word_count=word_count
        )

    except subprocess.TimeoutExpired:
        return ConversionResult(
            success=False,
            markdown_content='',
            error_message=f'Pandoc conversion timed out after {timeout} seconds',
            source_path=docx_path
        )
    except Exception as e:
        return ConversionResult(
            success=False,
            markdown_content='',
            error_message=f'Conversion error: {str(e)}',
            source_path=docx_path
        )
    finally:
        # Cleanup media directory if created
        if media_dir and os.path.exists(media_dir):
            shutil.rmtree(media_dir, ignore_errors=True)


def create_temp_tutorial_structure(
    markdown_content: str,
    course_name: str
) -> Tuple[str, str]:
    """
    Create a temporary folder structure mimicking a tutorial.

    This allows reuse of existing editorial_validation.py which expects:
    - A tc-* folder
    - step-*.md files

    For course content, we create:
    - tc-{course_name}/
    - step-1.md (contains full markdown content)

    Args:
        markdown_content: Converted markdown content
        course_name: Name of the course (sanitized for folder name)

    Returns:
        Tuple of (temp_folder_path, step_file_path)
    """
    import re

    # Sanitize course name for folder
    safe_name = re.sub(r'[^a-zA-Z0-9_-]', '-', course_name.lower())
    safe_name = re.sub(r'-+', '-', safe_name).strip('-')
    folder_name = f'tc-{safe_name}'

    # Create temp directory
    temp_dir = tempfile.mkdtemp(prefix='course_edit_')
    tutorial_folder = os.path.join(temp_dir, folder_name)
    os.makedirs(tutorial_folder)

    # Create step-1.md with full content
    step_file = os.path.join(tutorial_folder, 'step-1.md')
    with open(step_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    # Create images folder (required by validation)
    os.makedirs(os.path.join(tutorial_folder, 'images'))

    return tutorial_folder, step_file


def cleanup_temp_structure(temp_folder: str) -> None:
    """
    Remove temporary tutorial structure.

    Args:
        temp_folder: Path to temporary folder (parent of tc-* folder)
    """
    if temp_folder and os.path.exists(temp_folder):
        # Get parent directory (the temp root)
        parent = os.path.dirname(temp_folder)
        if parent.startswith(tempfile.gettempdir()):
            shutil.rmtree(parent, ignore_errors=True)


# CLI interface for testing
if __name__ == '__main__':
    import sys
    import argparse

    parser = argparse.ArgumentParser(
        description='Convert DOCX files to markdown using pandoc'
    )
    parser.add_argument('docx_path', nargs='?', help='Path to DOCX file')
    parser.add_argument('--output', '-o', help='Output markdown file (default: stdout)')
    parser.add_argument('--timeout', type=int, default=300, help='Conversion timeout in seconds')
    parser.add_argument('--check', action='store_true', help='Check pandoc installation only')

    args = parser.parse_args()

    if not args.check and not args.docx_path:
        parser.error('docx_path is required unless using --check')

    if args.check:
        installed, msg = check_pandoc_installed()
        if installed:
            print(f'Pandoc installed: {msg}')
            sys.exit(0)
        else:
            print(f'Pandoc not available: {msg}', file=sys.stderr)
            sys.exit(1)

    result = convert_docx_to_markdown(args.docx_path, timeout=args.timeout)

    if not result.success:
        print(f'Error: {result.error_message}', file=sys.stderr)
        sys.exit(1)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(result.markdown_content)
        print(f'Converted {result.source_path} to {args.output} ({result.word_count} words)')
    else:
        print(result.markdown_content)
