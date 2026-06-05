"""After: Observer reverses responsibility.

Subscribers declare interest once. The publisher announces change.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class Issue:
    title: str


class Subscriber(Protocol):
    def update(self, issue: Issue) -> None:
        ...


class MagazinePublisher:
    def __init__(self) -> None:
        self._subscribers: list[Subscriber] = []
        self.latest_issue: Issue | None = None

    def subscribe(self, subscriber: Subscriber) -> None:
        self._subscribers.append(subscriber)

    def publish(self, issue: Issue) -> None:
        self.latest_issue = issue
        self._notify_subscribers(issue)

    def _notify_subscribers(self, issue: Issue) -> None:
        for subscriber in self._subscribers:
            subscriber.update(issue)

class EmailSubscriber:
    def __init__(self) -> None:
        self.sent: list[str] = []

    def update(self, issue: Issue) -> None:
        self.sent.append(f"Email: {issue.title}")

class AnalyticsSubscriber:
    def __init__(self) -> None:
        self.events: list[str] = []

    def update(self, issue: Issue) -> None:
        self.events.append(f"Tracked: {issue.title}")


class MobileSubscriber:
    def __init__(self) -> None:
        self.notifications: list[str] = []

    def update(self, issue: Issue) -> None:
        self.notifications.append(f"Push: {issue.title}")


class FakeSubscriber:
    def __init__(self) -> None:
        self.received: list[str] = []

    def update(self, issue: Issue) -> None:
        self.received.append(issue.title)
