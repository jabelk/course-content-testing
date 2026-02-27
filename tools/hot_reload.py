#!/usr/bin/env python3
"""
Hot Reload Module for Editorial Rules and Acronym Database

Provides automatic reloading of configuration files when they change.
Uses file modification time checking (no external dependencies).

Usage:
    from hot_reload import RulesReloader

    reloader = RulesReloader()

    # Get rules (auto-reloads if file changed)
    rules = reloader.get_rules()
    acronyms = reloader.get_acronyms()

    # Force reload
    reloader.reload_all()

    # Check if files changed (without reloading)
    if reloader.check_for_changes():
        print("Files changed!")
"""
import os
import json
import time
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class FileState:
    """Tracks state of a watched file."""
    path: str
    last_modified: float = 0.0
    last_checked: float = 0.0
    content: Any = None
    error: Optional[str] = None


@dataclass
class RulesReloader:
    """
    Hot-reloading manager for editorial rules and acronym database.

    Checks file modification times and reloads when changes detected.
    Caches loaded content to avoid unnecessary disk reads.
    """
    rules_path: str = ""
    acronym_path: str = ""
    check_interval: float = 5.0  # Seconds between file stat checks

    _rules_state: FileState = field(default_factory=lambda: FileState(""))
    _acronym_state: FileState = field(default_factory=lambda: FileState(""))
    _initialized: bool = False

    def __post_init__(self):
        """Initialize with default paths if not provided."""
        script_dir = os.path.dirname(os.path.abspath(__file__))

        if not self.rules_path:
            self.rules_path = os.path.join(script_dir, 'editorial_rules.yaml')

        if not self.acronym_path:
            self.acronym_path = os.path.join(
                script_dir, '..', '.claude', 'references', 'acronym-database.json'
            )

        self._rules_state = FileState(self.rules_path)
        self._acronym_state = FileState(self.acronym_path)

    def _check_file_changed(self, state: FileState) -> bool:
        """Check if a file has been modified since last load."""
        now = time.time()

        # Rate limit stat calls
        if now - state.last_checked < self.check_interval:
            return False

        state.last_checked = now

        try:
            mtime = os.path.getmtime(state.path)
            if mtime > state.last_modified:
                return True
        except OSError:
            pass

        return False

    def _load_rules(self) -> List[Dict]:
        """Load editorial rules from YAML file."""
        state = self._rules_state

        try:
            with open(state.path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)

            state.last_modified = os.path.getmtime(state.path)
            state.content = data.get('rules', []) if data else []
            state.error = None

            return state.content

        except Exception as e:
            state.error = str(e)
            if state.content is None:
                state.content = []
            return state.content

    def _load_acronyms(self) -> Dict:
        """Load acronym database from JSON file."""
        state = self._acronym_state

        try:
            with open(state.path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            state.last_modified = os.path.getmtime(state.path)
            state.content = data
            state.error = None

            return state.content

        except Exception as e:
            state.error = str(e)
            if state.content is None:
                state.content = {}
            return state.content

    def get_rules(self, force_reload: bool = False) -> List[Dict]:
        """
        Get editorial rules, reloading if file changed.

        Args:
            force_reload: Force reload regardless of modification time

        Returns:
            List of rule dictionaries
        """
        if force_reload or not self._initialized or self._check_file_changed(self._rules_state):
            self._load_rules()
            self._initialized = True

        return self._rules_state.content or []

    def get_acronyms(self, force_reload: bool = False) -> Dict:
        """
        Get acronym database, reloading if file changed.

        Args:
            force_reload: Force reload regardless of modification time

        Returns:
            Acronym database dictionary
        """
        if force_reload or not self._initialized or self._check_file_changed(self._acronym_state):
            self._load_acronyms()
            self._initialized = True

        return self._acronym_state.content or {}

    def reload_all(self) -> Dict[str, bool]:
        """
        Force reload of all configuration files.

        Returns:
            Dict with reload status for each file
        """
        rules_ok = True
        acronyms_ok = True

        try:
            self._load_rules()
        except Exception:
            rules_ok = False

        try:
            self._load_acronyms()
        except Exception:
            acronyms_ok = False

        return {
            'rules': rules_ok,
            'acronyms': acronyms_ok
        }

    def check_for_changes(self) -> bool:
        """
        Check if any watched files have changed.

        Returns:
            True if any file has been modified since last load
        """
        # Temporarily set check_interval to 0 to force stat
        original_interval = self.check_interval
        self.check_interval = 0

        changed = (
            self._check_file_changed(self._rules_state) or
            self._check_file_changed(self._acronym_state)
        )

        self.check_interval = original_interval
        return changed

    def get_status(self) -> Dict[str, Any]:
        """
        Get current status of watched files.

        Returns:
            Dict with status information
        """
        return {
            'rules': {
                'path': self._rules_state.path,
                'last_modified': self._rules_state.last_modified,
                'loaded': self._rules_state.content is not None,
                'count': len(self._rules_state.content or []),
                'error': self._rules_state.error
            },
            'acronyms': {
                'path': self._acronym_state.path,
                'last_modified': self._acronym_state.last_modified,
                'loaded': self._acronym_state.content is not None,
                'count': sum(
                    len(v) for k, v in (self._acronym_state.content or {}).items()
                    if isinstance(v, dict) and k != '_metadata'
                ),
                'error': self._acronym_state.error
            },
            'check_interval': self.check_interval
        }


# Singleton instance for shared use
_default_reloader: Optional[RulesReloader] = None


def get_reloader() -> RulesReloader:
    """Get the default reloader instance (singleton)."""
    global _default_reloader
    if _default_reloader is None:
        _default_reloader = RulesReloader()
    return _default_reloader


# CLI for testing
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Hot reload test utility')
    parser.add_argument('--watch', action='store_true', help='Watch for changes')
    parser.add_argument('--interval', type=float, default=2.0, help='Check interval')
    args = parser.parse_args()

    reloader = RulesReloader(check_interval=args.interval)

    print("Initial load:")
    rules = reloader.get_rules()
    acronyms = reloader.get_acronyms()
    print(f"  Rules: {len(rules)}")
    print(f"  Acronyms: {reloader.get_status()['acronyms']['count']}")

    if args.watch:
        print(f"\nWatching for changes (interval: {args.interval}s)...")
        print("Press Ctrl+C to stop\n")

        try:
            while True:
                time.sleep(args.interval)
                if reloader.check_for_changes():
                    print(f"[{time.strftime('%H:%M:%S')}] Changes detected, reloading...")
                    result = reloader.reload_all()
                    status = reloader.get_status()
                    print(f"  Rules: {status['rules']['count']} ({'OK' if result['rules'] else 'ERROR'})")
                    print(f"  Acronyms: {status['acronyms']['count']} ({'OK' if result['acronyms'] else 'ERROR'})")
        except KeyboardInterrupt:
            print("\nStopped.")
