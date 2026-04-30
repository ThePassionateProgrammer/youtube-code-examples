from dataclasses import dataclass

@dataclass
class Meeting:
    kind: str
    participants: int = 2

class SchedulingTemplate:
    def schedule(self, meeting: Meeting) -> str:
        room = self.allocate_room(meeting)
        notification = self.notify(meeting)
        return f"{room} | {notification}"

    def allocate_room(self, meeting: Meeting) -> str:
        raise NotImplementedError()

    def notify(self, meeting: Meeting) -> str:
        raise NotImplementedError()

class TeamScheduler(SchedulingTemplate):
    def allocate_room(self, meeting: Meeting) -> str:
        return f"large room for {meeting.participants}"

    def notify(self, meeting: Meeting) -> str:
        return "notify team"

class OneOnOneScheduler(SchedulingTemplate):
    def allocate_room(self, meeting: Meeting) -> str:
        return "small room"

    def notify(self, meeting: Meeting) -> str:
        return "notify both people"
