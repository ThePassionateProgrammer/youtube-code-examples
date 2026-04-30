from dataclasses import dataclass


@dataclass
class Meeting:
    kind: str
    size: int
    time: str


class MeetingCoordinator:
    def schedule_team(self, meeting: Meeting) -> str:
        room = self._find_room(meeting.size)
        self._reserve(room, meeting.time)
        self._notify_team(meeting)
        return f"Scheduled team meeting in {room}"

    def schedule_one_on_one(self, meeting: Meeting) -> str:
        room = self._find_room(2)
        self._reserve(room, meeting.time)
        self._notify_individuals(meeting)
        return f"Scheduled 1:1 meeting in {room}"

    def schedule_all_hands(self, meeting: Meeting) -> str:
        room = self._find_auditorium()
        self._reserve(room, meeting.time)
        self._notify_everyone(meeting)
        return f"Scheduled all-hands in {room}"

    def _find_room(self, size: int) -> str:
        return f"Room-{size}"

    def _find_auditorium(self) -> str:
        return "Auditorium"

    def _reserve(self, room: str, time: str) -> None:
        pass

    def _notify_team(self, meeting: Meeting) -> None:
        pass

    def _notify_individuals(self, meeting: Meeting) -> None:
        pass

    def _notify_everyone(self, meeting: Meeting) -> None:
        pass
