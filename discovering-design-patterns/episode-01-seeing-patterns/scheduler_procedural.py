"""
Episode 1: Seeing Patterns in Problems
The Passionate Programmer — @ThePassionateProgrammer

TRAP: Procedural scheduling — directions, not a map.

Two functions that do the same thing with slight variation.
Clear. Works. But notice: no model, no relationships, no place to grow.
"""


def find_room(size: int) -> str:
    """Simulate finding an available room for a given capacity."""
    rooms = {2: "Room A", 5: "Room B", 10: "Room C"}
    return rooms.get(size, "Main Hall")


def reserve(room: str) -> None:
    print(f"Reserved: {room}")


def notify_team(meeting: dict) -> None:
    print(f"Team notified: {meeting['title']}")


def notify_individuals(meeting: dict) -> None:
    for attendee in meeting.get("attendees", []):
        print(f"Notified: {attendee}")


# ── The Trap ──────────────────────────────────────────────────────────────────
# Two functions. Same shape. Slight variation.
# Step 1 → Step 2 → Step 3. Directions, not a map.

def schedule_team(meeting: dict) -> None:
    room = find_room(meeting["size"])
    reserve(room)
    notify_team(meeting)


def schedule_one_on_one(meeting: dict) -> None:
    room = find_room(2)
    reserve(room)
    notify_individuals(meeting)
