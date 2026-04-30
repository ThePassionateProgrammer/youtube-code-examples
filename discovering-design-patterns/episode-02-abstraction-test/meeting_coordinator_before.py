from dataclasses import dataclass


@dataclass(frozen=True)
class Meeting:
    kind: str
    size: int
    time: str


class MeetingCoordinator:
    def schedule_team(self, meeting: Meeting) -> str:
        room = self._find_room(meeting.size)
        reservation = self._reserve(room, meeting.time)
        notice = self._notify_team(meeting)
        return f"{reservation} | {notice}"

    def schedule_one_on_one(self, meeting: Meeting) -> str:
        room = self._find_room(2)
        reservation = self._reserve(room, meeting.time)
        notice = self._notify_individuals(meeting)
        return f"{reservation} | {notice}"

    def schedule_all_hands(self, meeting: Meeting) -> str:
        room = self._find_auditorium()
        reservation = self._reserve(room, meeting.time)
        notice = self._notify_everyone(meeting)
        return f"{reservation} | {notice}"



    def _find_room(self, seats: int) -> str:
        return f"Room for {seats}"

    def _find_auditorium(self) -> str:
        return "Auditorium"

    def _reserve(self, room: str, time: str) -> str:
        return f"Reserved {room} at {time}"

    def _notify_team(self, meeting: Meeting) -> str:
        return f"Notified team for {meeting.kind}"

    def _notify_individuals(self, meeting: Meeting) -> str:
        return f"Notified individuals for {meeting.kind}"

    def _notify_everyone(self, meeting: Meeting) -> str:
        return f"Notified everyone for {meeting.kind}"
