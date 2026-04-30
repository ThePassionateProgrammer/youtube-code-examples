from dataclasses import dataclass


@dataclass
class Meeting:
    kind: str
    size: int
    time: str


class SchedulingProcess:
    def schedule(self, meeting: Meeting) -> str:
        room = self.find_room(meeting)
        self.reserve(room, meeting.time)
        self.notify(meeting)
        return self.scheduled_message(room)

    def find_room(self, meeting: Meeting) -> str:
        raise NotImplementedError()

    def notify(self, meeting: Meeting) -> None:
        raise NotImplementedError()

    def scheduled_message(self, room: str) -> str:
        return f"Scheduled in {room}"

    def reserve(self, room: str, time: str) -> None:
        pass


class TeamScheduling(SchedulingProcess):
    def find_room(self, meeting: Meeting) -> str:
        return f"Room-{meeting.size}"

    def notify(self, meeting: Meeting) -> None:
        pass

    def scheduled_message(self, room: str) -> str:
        return f"Scheduled team meeting in {room}"


class OneOnOneScheduling(SchedulingProcess):
    def find_room(self, meeting: Meeting) -> str:
        return "Room-2"

    def notify(self, meeting: Meeting) -> None:
        pass

    def scheduled_message(self, room: str) -> str:
        return f"Scheduled 1:1 meeting in {room}"


class AllHandsScheduling(SchedulingProcess):
    def find_room(self, meeting: Meeting) -> str:
        return "Auditorium"

    def notify(self, meeting: Meeting) -> None:
        pass

    def scheduled_message(self, room: str) -> str:
        return f"Scheduled all-hands in {room}"
