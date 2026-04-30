"""
Episode 1: Seeing Patterns in Problems
The Passionate Programmer — @ThePassionateProgrammer

STRUCTURAL MOVE: From directions to a map.

Behavior now lives in objects.
The system becomes a set of interacting parts.
This is where patterns start to appear.
"""

from abc import ABC, abstractmethod


def find_room(size: int) -> str:
    rooms = {2: "Room A", 5: "Room B", 10: "Room C"}
    return rooms.get(size, "Main Hall")


def reserve(room: str) -> None:
    print(f"Reserved: {room}")


def notify_team(meeting: dict) -> None:
    print(f"Team notified: {meeting['title']}")


def notify_individuals(meeting: dict) -> None:
    for attendee in meeting.get("attendees", []):
        print(f"Notified: {attendee}")


# ── The Map ───────────────────────────────────────────────────────────────────
# Behavior lives in objects.
# Variation is isolated. The scheduler doesn't care what kind of meeting it is.
# Add new meeting types without touching Scheduler.

class SchedulingStrategy(ABC):
    """What varies: how a meeting is scheduled."""

    @abstractmethod
    def schedule(self, meeting: dict) -> None:
        pass


class TeamMeetingStrategy(SchedulingStrategy):
    def schedule(self, meeting: dict) -> None:
        room = find_room(meeting["size"])
        reserve(room)
        notify_team(meeting)


class OneOnOneMeetingStrategy(SchedulingStrategy):
    def schedule(self, meeting: dict) -> None:
        room = find_room(2)
        reserve(room)
        notify_individuals(meeting)


class Scheduler:
    """What stays stable: the scheduling workflow."""

    def schedule(self, meeting: dict, strategy: SchedulingStrategy) -> None:
        strategy.schedule(meeting)
