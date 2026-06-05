"""Before: polling spreads timing logic everywhere.

This file is intentionally simple for screen capture. The first function matches
David's narration exactly: check for change, wait, check again.
"""

from __future__ import annotations

from dataclasses import dataclass
from time import sleep
from typing import Optional


@dataclass(frozen=True)
class Issue:
    title: str


class Magazine:
    def __init__(self) -> None:
        self.latest_issue: Optional[Issue] = None

    def has_new_issue(self) -> bool:
        return self.latest_issue is not None

    def publish(self, issue: Issue) -> None:
        self.latest_issue = issue


class Reader:
    def __init__(self) -> None:
        self.downloaded: list[str] = []

    def download(self, issue: Issue) -> None:
        self.downloaded.append(issue.title)

# check for change, wait, check again.
def wait_for_new_issue(magazine: Magazine, reader: Reader, 
                    delay_seconds: float = 60) -> None:
    while not magazine.has_new_issue():
        sleep(delay_seconds)

    reader.download(magazine.latest_issue)  # type: ignore[arg-type]

# polling spreads as more collaborators care about the same change.
def poll_all_collaborators(magazine: Magazine, collaborators: list[object]) -> None:
    if magazine.has_new_issue():
        for collaborator in collaborators:
            collaborator.check_for_issue(magazine)  # type: ignore[attr-defined]

class EmailService:
    def __init__(self) -> None:
        self.sent: list[str] = []

    def check_for_issue(self, magazine: Magazine) -> None:
        if magazine.has_new_issue():
            self.sent.append(f"Email: {magazine.latest_issue.title}")  # type: ignore[union-attr]

class Analytics:
    def __init__(self) -> None:
        self.events: list[str] = []

    def check_for_issue(self, magazine: Magazine) -> None:
        if magazine.has_new_issue():
            self.events.append(f"Tracked: {magazine.latest_issue.title}")  # type: ignore[union-attr]


class MobileApp:
    def __init__(self) -> None:
        self.notifications: list[str] = []

    def check_for_issue(self, magazine: Magazine) -> None:
        if magazine.has_new_issue():
            self.notifications.append(f"Push: {magazine.latest_issue.title}")  # type: ignore[union-attr]
