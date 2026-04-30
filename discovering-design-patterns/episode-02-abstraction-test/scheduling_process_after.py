from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass(frozen=True)
class Meeting:
    kind: str
    size: int
    time: str

class SchedulingProcess(ABC):
    def schedule(self, meeting: Meeting) -> str:
        room = self.find_room(meeting)
        reservation = self.reserve(room, meeting)
        notice = self.notify(meeting)
        return f"{reservation} | {notice}"

    @abstractmethod
    def find_room(self, meeting: Meeting) -> str:
        raise NotImplementedError

    def reserve(self, room: str, meeting: Meeting) -> str:
        return f"Reserved {room} at {meeting.time}"

    @abstractmethod
    def notify(self, meeting: Meeting) -> str:
        raise NotImplementedError


class TeamSchedulingProcess(SchedulingProcess):
    def find_room(self, meeting: Meeting) -> str:
        return f"Room for {meeting.size}"

    def notify(self, meeting: Meeting) -> str:
        return f"Notified team for {meeting.kind}"


class OneOnOneSchedulingProcess(SchedulingProcess):
    def find_room(self, meeting: Meeting) -> str:
        return "Room for 2"

    def notify(self, meeting: Meeting) -> str:
        return f"Notified individuals for {meeting.kind}"


class AllHandsSchedulingProcess(SchedulingProcess):
    def find_room(self, meeting: Meeting) -> str:
        return "Auditorium"

    def notify(self, meeting: Meeting) -> str:
        return f"Notified everyone for {meeting.kind}"
