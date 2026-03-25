#!/usr/bin/env python3
"""
LWC Jira Integration - Update Jira tickets from PR events

Provides functions to:
- Extract ticket ID from PR branch name or description
- Create new tickets for PRs without linked tickets
- Update ticket status based on linting/editorial results
- Add remote links to PRs

Usage:
    python lwc_jira.py update-from-pr --pr-url URL [OPTIONS]

Environment variables required:
    JIRA_EMAIL: Service account email
    JIRA_API_TOKEN: API token for authentication
"""

import argparse
import json
import logging
import os
import re
import sys
from dataclasses import dataclass
from typing import Optional

import requests
from requests.auth import HTTPBasicAuth

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@dataclass
class JiraConfig:
    """LWC Jira configuration."""
    base_url: str = "https://cisco-learning.atlassian.net"
    api_version: str = "3"
    project_key: str = "LACP"  # Default, will be overridden by Tom's project code


class LWCJiraClient:
    """
    Lightweight Jira client for LWC module workflow.

    Based on the tutorial-testing JiraClient but simplified for LWC use case.
    """

    # Pattern to extract ticket ID from branch name (e.g., LACP-1234-feature-name)
    BRANCH_PATTERN = re.compile(r'([A-Z]+-\d+)')

    def __init__(self, project_key: str = None):
        """
        Initialize LWC Jira client.

        Args:
            project_key: Jira project key (default: LACP, can be overridden)
        """
        self.config = JiraConfig()
        if project_key:
            self.config.project_key = project_key

        self.auth = self._get_auth()
        self.session = requests.Session()
        self.session.auth = self.auth
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json"
        })

    def _get_auth(self) -> HTTPBasicAuth:
        """Get authentication from environment variables."""
        email = os.environ.get("JIRA_EMAIL") or os.environ.get("EMAIL")
        token = os.environ.get("JIRA_API_TOKEN") or os.environ.get("API_TOKEN")

        if not email or not token:
            raise ValueError(
                "JIRA_EMAIL and JIRA_API_TOKEN environment variables required"
            )

        return HTTPBasicAuth(email, token)

    @property
    def api_url(self) -> str:
        """Base URL for API calls."""
        return f"{self.config.base_url}/rest/api/{self.config.api_version}"

    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Make HTTP request to Jira API."""
        url = f"{self.api_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)

        if response.status_code == 401:
            raise ValueError("Invalid Jira credentials")

        if response.status_code >= 400:
            logger.error(f"Jira API error: {response.status_code} - {response.text}")
            response.raise_for_status()

        return response

    def extract_ticket_id(self, text: str) -> Optional[str]:
        """
        Extract Jira ticket ID from text (branch name, PR title, etc.)

        Args:
            text: Text to search for ticket ID

        Returns:
            Ticket ID (e.g., 'LACP-1234') or None
        """
        match = self.BRANCH_PATTERN.search(text)
        if match:
            return match.group(1)
        return None

    def issue_exists(self, issue_key: str) -> bool:
        """Check if an issue exists."""
        try:
            response = self._request("GET", f"/issue/{issue_key}", params={"fields": "key"})
            return response.status_code == 200
        except Exception:
            return False

    def get_issue(self, issue_key: str) -> dict:
        """Get issue details."""
        response = self._request("GET", f"/issue/{issue_key}")
        return response.json()

    def add_comment(self, issue_key: str, body: str) -> dict:
        """Add a comment to an issue."""
        payload = {
            "body": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [{"type": "text", "text": body}]
                    }
                ]
            }
        }
        response = self._request("POST", f"/issue/{issue_key}/comment", json=payload)
        return response.json()

    def add_remote_link(self, issue_key: str, url: str, title: str) -> dict:
        """Add a remote link (e.g., GitHub PR URL) to an issue."""
        payload = {
            "object": {
                "url": url,
                "title": title,
                "icon": {
                    "url16x16": "https://github.githubassets.com/favicon.ico"
                }
            }
        }
        response = self._request("POST", f"/issue/{issue_key}/remotelink", json=payload)
        return response.json()

    def get_transitions(self, issue_key: str) -> list:
        """Get available transitions for an issue."""
        response = self._request("GET", f"/issue/{issue_key}/transitions")
        return response.json().get("transitions", [])

    def transition_issue(self, issue_key: str, transition_name: str) -> bool:
        """
        Transition an issue to a new status.

        Args:
            issue_key: Issue key (e.g., LACP-1234)
            transition_name: Target status name

        Returns:
            True if successful, False if transition not available
        """
        transitions = self.get_transitions(issue_key)

        # Find matching transition
        target = None
        for t in transitions:
            if t["name"].lower() == transition_name.lower():
                target = t
                break
            if t.get("to", {}).get("name", "").lower() == transition_name.lower():
                target = t
                break

        if not target:
            logger.warning(f"Transition '{transition_name}' not available for {issue_key}")
            return False

        self._request(
            "POST",
            f"/issue/{issue_key}/transitions",
            json={"transition": {"id": target["id"]}}
        )
        logger.info(f"Transitioned {issue_key} to '{transition_name}'")
        return True

    def create_issue(
        self,
        summary: str,
        description: str = None,
        issue_type: str = "Task"
    ) -> Optional[str]:
        """
        Create a new Jira issue.

        Args:
            summary: Issue summary/title
            description: Issue description (optional)
            issue_type: Issue type (default: Task)

        Returns:
            Created issue key (e.g., LACP-1234) or None on failure
        """
        payload = {
            "fields": {
                "project": {"key": self.config.project_key},
                "summary": summary,
                "issuetype": {"name": issue_type}
            }
        }

        if description:
            payload["fields"]["description"] = {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [{"type": "text", "text": description}]
                    }
                ]
            }

        try:
            response = self._request("POST", "/issue", json=payload)
            result = response.json()
            issue_key = result.get("key")
            logger.info(f"Created issue: {issue_key}")
            return issue_key
        except Exception as e:
            logger.error(f"Failed to create issue: {e}")
            return None

    def update_from_pr(
        self,
        pr_url: str,
        branch_name: str = None,
        pr_title: str = None,
        linting_passed: bool = True,
        issues_count: int = 0,
        create_if_missing: bool = False
    ) -> Optional[str]:
        """
        Update Jira ticket based on PR information.

        This is the main entry point for GitHub Actions workflow.

        Args:
            pr_url: GitHub PR URL
            branch_name: PR branch name (for ticket ID extraction)
            pr_title: PR title (alternative source for ticket ID)
            linting_passed: Whether linting passed
            issues_count: Number of editorial issues needing review
            create_if_missing: Create a new ticket if none found

        Returns:
            Ticket key if found/updated/created, None otherwise
        """
        # Try to find ticket ID
        ticket_key = None
        if branch_name:
            ticket_key = self.extract_ticket_id(branch_name)
        if not ticket_key and pr_title:
            ticket_key = self.extract_ticket_id(pr_title)

        # If no ticket found and creation enabled, create one
        if not ticket_key:
            if create_if_missing:
                logger.info("No ticket ID found, creating new ticket")
                summary = pr_title or f"Editorial review for PR: {pr_url.split('/')[-1]}"
                description = f"Automatically created for PR: {pr_url}"
                ticket_key = self.create_issue(summary, description)
                if not ticket_key:
                    logger.error("Failed to create ticket")
                    return None
            else:
                logger.info("No ticket ID found in branch name or PR title")
                return None
        # Verify ticket exists (if we extracted one from branch/title)
        elif not self.issue_exists(ticket_key):
            logger.warning(f"Ticket {ticket_key} does not exist")
            return None

        logger.info(f"Found ticket: {ticket_key}")

        # Add remote link to PR (if not already linked)
        try:
            self.add_remote_link(
                ticket_key,
                pr_url,
                f"GitHub PR: {pr_title or pr_url.split('/')[-1]}"
            )
            logger.info(f"Added PR link to {ticket_key}")
        except Exception as e:
            logger.warning(f"Could not add remote link: {e}")

        # Add comment with status
        status_emoji = "✓" if linting_passed and issues_count == 0 else "⚠️"
        comment = f"{status_emoji} Editorial Review Complete\n\n"
        comment += f"- Linting: {'Passed' if linting_passed else 'Failed'}\n"
        comment += f"- Editorial Issues Needing Review: {issues_count}\n"
        comment += f"- PR: {pr_url}"

        try:
            self.add_comment(ticket_key, comment)
            logger.info(f"Added comment to {ticket_key}")
        except Exception as e:
            logger.warning(f"Could not add comment: {e}")

        # Transition to appropriate status
        if linting_passed and issues_count == 0:
            # All checks passed - ready for review
            self.transition_issue(ticket_key, "Ready for Review")
        elif not linting_passed:
            # Linting failed - needs work
            self.transition_issue(ticket_key, "In Progress")

        return ticket_key


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="LWC Jira Integration")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # update-from-pr command
    pr_parser = subparsers.add_parser(
        "update-from-pr",
        help="Update Jira ticket from PR information"
    )
    pr_parser.add_argument("--pr-url", required=True, help="GitHub PR URL")
    pr_parser.add_argument("--branch-name", help="PR branch name")
    pr_parser.add_argument("--pr-title", help="PR title")
    pr_parser.add_argument(
        "--linting-passed",
        type=lambda x: x.lower() in ('true', '1', 'yes'),
        default=True,
        help="Whether linting passed"
    )
    pr_parser.add_argument(
        "--issues-count",
        type=int,
        default=0,
        help="Number of editorial issues needing review"
    )
    pr_parser.add_argument("--project-key", help="Jira project key (default: LACP)")
    pr_parser.add_argument(
        "--create-if-missing",
        action="store_true",
        help="Create a new ticket if none found in branch name"
    )

    # test-auth command
    auth_parser = subparsers.add_parser("test-auth", help="Test Jira authentication")
    auth_parser.add_argument("--project-key", help="Jira project key")

    args = parser.parse_args()

    try:
        client = LWCJiraClient(project_key=getattr(args, 'project_key', None))

        if args.command == "update-from-pr":
            result = client.update_from_pr(
                pr_url=args.pr_url,
                branch_name=args.branch_name,
                pr_title=args.pr_title,
                linting_passed=args.linting_passed,
                issues_count=args.issues_count,
                create_if_missing=args.create_if_missing
            )
            if result:
                print(f"Updated ticket: {result}")
            else:
                print("No ticket found to update")

        elif args.command == "test-auth":
            # Simple auth test
            response = client._request("GET", "/myself")
            user = response.json()
            print(f"✓ Authenticated as: {user.get('displayName', user.get('emailAddress'))}")

    except ValueError as e:
        print(f"✗ Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
