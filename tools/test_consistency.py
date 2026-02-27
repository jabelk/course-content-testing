#!/usr/bin/env python3
"""
Consistency Test Script for Course AI Editing

Validates that the same DOCX file produces consistent results across multiple runs.
This addresses User Story 3: Compare Results with Previous Attempts.

Key Metrics:
- Issue count variance (target: <5%)
- Category breakdown variance
- Quality score variance

Usage:
    python test_consistency.py <docx_path> [OPTIONS]

Options:
    --runs N        Number of test runs (default: 3)
    --threshold N   Maximum acceptable variance percentage (default: 5)
    --verbose       Show detailed per-run output
    --json          Output results as JSON
"""
import os
import sys
import json
import argparse
import statistics
from typing import List, Dict, Tuple
from datetime import datetime

# Add tools directory to path
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

from course_editor import convert_and_validate, validate_docx_file


def run_consistency_test(
    docx_path: str,
    num_runs: int = 3,
    verbose: bool = False
) -> List[Dict]:
    """
    Run validation multiple times and collect results.

    Args:
        docx_path: Path to DOCX file
        num_runs: Number of times to run validation
        verbose: Show per-run output

    Returns:
        List of result dictionaries with issue counts
    """
    results = []

    for i in range(num_runs):
        if verbose:
            print(f"Run {i + 1}/{num_runs}...", end=" ", flush=True)

        result, course_module, error = convert_and_validate(
            docx_path=docx_path,
            use_ai=False,  # Disable AI for deterministic testing
            verbose=False,
            show_progress=False
        )

        if error:
            if verbose:
                print(f"ERROR: {error}")
            results.append({
                'run': i + 1,
                'success': False,
                'error': error
            })
            continue

        score = result.quality_score
        by_type = result.get_issues_by_type()

        run_data = {
            'run': i + 1,
            'success': True,
            'total_issues': score.total_issues,
            'safe_count': score.safe_count,
            'review_count': score.review_count,
            'query_count': score.query_count,
            'quality_score': score.score,
            'processing_time_ms': result.processing_time_ms,
            'rules_applied': len(result.rules_applied)
        }

        results.append(run_data)

        if verbose:
            print(f"done ({score.total_issues} issues, {result.processing_time_ms}ms)")

    return results


def calculate_variance(values: List[float]) -> Tuple[float, float, float]:
    """
    Calculate variance statistics for a list of values.

    Returns:
        Tuple of (mean, stddev, variance_percent)
    """
    if len(values) < 2:
        return values[0] if values else 0, 0, 0

    mean = statistics.mean(values)
    stddev = statistics.stdev(values)

    # Calculate variance as percentage of mean
    variance_percent = (stddev / mean * 100) if mean > 0 else 0

    return mean, stddev, variance_percent


def analyze_results(results: List[Dict]) -> Dict:
    """
    Analyze consistency across multiple runs.

    Args:
        results: List of run results

    Returns:
        Dictionary with analysis metrics
    """
    successful_runs = [r for r in results if r.get('success')]

    if not successful_runs:
        return {
            'success': False,
            'error': 'All runs failed',
            'runs': len(results),
            'successful_runs': 0
        }

    # Extract metrics from successful runs
    total_issues = [r['total_issues'] for r in successful_runs]
    safe_counts = [r['safe_count'] for r in successful_runs]
    review_counts = [r['review_count'] for r in successful_runs]
    query_counts = [r['query_count'] for r in successful_runs]
    quality_scores = [r['quality_score'] for r in successful_runs]
    processing_times = [r['processing_time_ms'] for r in successful_runs]

    # Calculate variances
    total_mean, total_std, total_var = calculate_variance(total_issues)
    safe_mean, safe_std, safe_var = calculate_variance(safe_counts)
    review_mean, review_std, review_var = calculate_variance(review_counts)
    query_mean, query_std, query_var = calculate_variance(query_counts)
    score_mean, score_std, score_var = calculate_variance(quality_scores)
    time_mean, time_std, time_var = calculate_variance(processing_times)

    # Check if all runs produced identical results
    is_deterministic = len(set(total_issues)) == 1

    return {
        'success': True,
        'runs': len(results),
        'successful_runs': len(successful_runs),
        'is_deterministic': is_deterministic,
        'metrics': {
            'total_issues': {
                'values': total_issues,
                'mean': round(total_mean, 2),
                'stddev': round(total_std, 2),
                'variance_percent': round(total_var, 2)
            },
            'safe_count': {
                'values': safe_counts,
                'mean': round(safe_mean, 2),
                'stddev': round(safe_std, 2),
                'variance_percent': round(safe_var, 2)
            },
            'review_count': {
                'values': review_counts,
                'mean': round(review_mean, 2),
                'stddev': round(review_std, 2),
                'variance_percent': round(review_var, 2)
            },
            'query_count': {
                'values': query_counts,
                'mean': round(query_mean, 2),
                'stddev': round(query_std, 2),
                'variance_percent': round(query_var, 2)
            },
            'quality_score': {
                'values': quality_scores,
                'mean': round(score_mean, 2),
                'stddev': round(score_std, 2),
                'variance_percent': round(score_var, 2)
            },
            'processing_time_ms': {
                'values': processing_times,
                'mean': round(time_mean, 2),
                'stddev': round(time_std, 2),
                'variance_percent': round(time_var, 2)
            }
        }
    }


def format_report(analysis: Dict, threshold: float, docx_path: str) -> str:
    """
    Format analysis results as a human-readable report.

    Args:
        analysis: Analysis dictionary
        threshold: Maximum acceptable variance percentage
        docx_path: Path to DOCX file tested

    Returns:
        Formatted report string
    """
    lines = []

    lines.append("=" * 60)
    lines.append("CONSISTENCY TEST REPORT")
    lines.append("=" * 60)
    lines.append("")
    lines.append(f"File: {os.path.basename(docx_path)}")
    lines.append(f"Runs: {analysis['successful_runs']}/{analysis['runs']} successful")
    lines.append(f"Threshold: {threshold}% variance")
    lines.append("")

    if not analysis['success']:
        lines.append(f"ERROR: {analysis.get('error', 'Unknown error')}")
        return '\n'.join(lines)

    # Deterministic check
    if analysis['is_deterministic']:
        lines.append("RESULT: FULLY DETERMINISTIC")
        lines.append("All runs produced identical issue counts.")
        lines.append("")
    else:
        lines.append("RESULT: VARIANCE DETECTED")
        lines.append("")

    # Metrics table
    lines.append("METRICS:")
    lines.append("-" * 60)
    lines.append(f"{'Metric':<20} {'Mean':>10} {'StdDev':>10} {'Variance%':>12} {'Status':>10}")
    lines.append("-" * 60)

    metrics = analysis['metrics']
    all_pass = True

    for metric_name, data in metrics.items():
        if metric_name == 'processing_time_ms':
            display_name = 'Processing Time'
        else:
            display_name = metric_name.replace('_', ' ').title()

        variance = data['variance_percent']
        status = "PASS" if variance <= threshold else "FAIL"
        if status == "FAIL":
            all_pass = False

        lines.append(f"{display_name:<20} {data['mean']:>10.1f} {data['stddev']:>10.2f} {variance:>11.2f}% {status:>10}")

    lines.append("-" * 60)
    lines.append("")

    # Overall result
    if analysis['is_deterministic']:
        lines.append("OVERALL: PASS (100% consistent)")
    elif all_pass:
        lines.append(f"OVERALL: PASS (all metrics within {threshold}% variance)")
    else:
        lines.append(f"OVERALL: FAIL (some metrics exceed {threshold}% variance)")

    lines.append("")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    return '\n'.join(lines)


def main():
    """Main entry point for consistency testing."""
    parser = argparse.ArgumentParser(
        description='Test consistency of course editorial validation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    parser.add_argument(
        'docx_path',
        help='Path to DOCX file to test'
    )
    parser.add_argument(
        '--runs', '-r',
        type=int,
        default=3,
        help='Number of test runs (default: 3)'
    )
    parser.add_argument(
        '--threshold', '-t',
        type=float,
        default=5.0,
        help='Maximum acceptable variance percentage (default: 5)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Show detailed per-run output'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output results as JSON'
    )

    args = parser.parse_args()

    # Validate input
    is_valid, error = validate_docx_file(args.docx_path)
    if not is_valid:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    # Run tests
    print(f"Running {args.runs} consistency tests on: {os.path.basename(args.docx_path)}")
    print("")

    results = run_consistency_test(
        docx_path=args.docx_path,
        num_runs=args.runs,
        verbose=args.verbose
    )

    # Analyze results
    analysis = analyze_results(results)

    # Output
    if args.json:
        output = {
            'file': args.docx_path,
            'threshold': args.threshold,
            'results': results,
            'analysis': analysis,
            'timestamp': datetime.now().isoformat()
        }
        print(json.dumps(output, indent=2))
    else:
        print(format_report(analysis, args.threshold, args.docx_path))

    # Exit with appropriate code
    if not analysis['success']:
        return 1

    # Check if within threshold
    total_variance = analysis['metrics']['total_issues']['variance_percent']
    if total_variance > args.threshold:
        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
