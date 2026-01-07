#!/usr/bin/env python3
# /// script
# dependencies = ["python-dotenv", "requests"]
# ///
"""
Apify Actor Runner - Runs Apify actors and exports results.

Usage:
    uv run scripts/run_actor.py --actor ACTOR_ID --input '{}' --output leads.csv --format csv
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv, find_dotenv
import requests


def main():
    # Load .env from current dir or any parent dir - token stays in Python process
    load_dotenv(find_dotenv(usecwd=True))
    token = os.getenv("APIFY_TOKEN")
    if not token:
        print("Error: APIFY_TOKEN not found in .env file", file=sys.stderr)
        print("", file=sys.stderr)
        print("Add your token to .env file:", file=sys.stderr)
        print("  APIFY_TOKEN=your_token_here", file=sys.stderr)
        print("", file=sys.stderr)
        print("Get your token: https://console.apify.com/account/integrations", file=sys.stderr)
        sys.exit(1)

    args = parse_args()

    # Start the actor run
    print(f"Starting actor: {args.actor}")
    run_id, dataset_id = start_actor(token, args.actor, args.input)
    print(f"Run ID: {run_id}")
    print(f"Dataset ID: {dataset_id}")

    # Poll for completion
    status = poll_until_complete(token, run_id, args.timeout, args.poll_interval)

    if status != "SUCCEEDED":
        print(f"Error: Actor run {status}", file=sys.stderr)
        print(f"Details: https://console.apify.com/actors/runs/{run_id}", file=sys.stderr)
        sys.exit(1)

    # Download results
    download_results(token, dataset_id, args.output, args.format)

    # Report summary
    report_summary(args.output, args.format)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run Apify actor and export results",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Find coffee shops in Seattle, export as CSV
  uv run scripts/run_actor.py \\
    --actor "compass~crawler-google-places" \\
    --input '{"searchStringsArray": ["coffee shops"], "locationQuery": "Seattle, USA"}' \\
    --output leads.csv --format csv

  # Extract contacts from websites, export as JSON
  uv run scripts/run_actor.py \\
    --actor "vdrmota~contact-info-scraper" \\
    --input '{"startUrls": [{"url": "https://example.com"}]}' \\
    --output contacts.json --format json
        """,
    )
    parser.add_argument(
        "--actor",
        required=True,
        help="Actor ID (e.g., compass~crawler-google-places)",
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Actor input as JSON string",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output file path",
    )
    parser.add_argument(
        "--format",
        default="csv",
        choices=["csv", "json"],
        help="Output format (default: csv)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=600,
        help="Max wait time in seconds (default: 600)",
    )
    parser.add_argument(
        "--poll-interval",
        type=int,
        default=5,
        help="Seconds between status checks (default: 5)",
    )
    return parser.parse_args()


def start_actor(token: str, actor_id: str, input_json: str) -> tuple[str, str]:
    """Start an actor run and return (run_id, dataset_id)."""
    url = f"https://api.apify.com/v2/acts/{actor_id}/runs"
    headers = {"Content-Type": "application/json"}
    params = {"token": token}

    try:
        data = json.loads(input_json)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON input: {e}", file=sys.stderr)
        sys.exit(1)

    response = requests.post(url, headers=headers, params=params, json=data)

    if response.status_code == 404:
        print(f"Error: Actor '{actor_id}' not found", file=sys.stderr)
        sys.exit(1)

    response.raise_for_status()

    result = response.json()["data"]
    return result["id"], result["defaultDatasetId"]


def poll_until_complete(
    token: str, run_id: str, timeout: int, interval: int
) -> str:
    """Poll run status until complete or timeout."""
    url = f"https://api.apify.com/v2/actor-runs/{run_id}"
    params = {"token": token}

    start_time = time.time()
    last_status = None

    while True:
        response = requests.get(url, params=params)
        response.raise_for_status()

        status = response.json()["data"]["status"]

        # Only print when status changes
        if status != last_status:
            print(f"Status: {status}")
            last_status = status

        if status in ("SUCCEEDED", "FAILED", "ABORTED", "TIMED-OUT"):
            return status

        elapsed = time.time() - start_time
        if elapsed > timeout:
            print(f"Warning: Timeout after {timeout}s, actor still running", file=sys.stderr)
            return "TIMED-OUT"

        time.sleep(interval)


def download_results(
    token: str, dataset_id: str, output_path: str, format: str
) -> None:
    """Download dataset items in specified format."""
    url = f"https://api.apify.com/v2/datasets/{dataset_id}/items"
    params = {"token": token, "format": format}

    response = requests.get(url, params=params)
    response.raise_for_status()

    Path(output_path).write_bytes(response.content)
    print(f"Saved to: {output_path}")


def report_summary(output_path: str, format: str) -> None:
    """Print summary of downloaded data."""
    path = Path(output_path)
    size = path.stat().st_size

    try:
        if format == "json":
            data = json.loads(path.read_text())
            count = len(data) if isinstance(data, list) else 1
        else:  # csv
            lines = path.read_text().splitlines()
            count = max(0, len(lines) - 1)  # Exclude header
    except Exception:
        count = "unknown"

    print(f"Records: {count}")
    print(f"Size: {size:,} bytes")


if __name__ == "__main__":
    main()
