from dataclasses import dataclass

@dataclass
class Meeting:
    kind: str

class Scheduler:
    def schedule(self, meeting: Meeting) -> str:
        return f"scheduled {meeting.kind}"

class ProtectionProxy:
    def __init__(self, scheduler: Scheduler, allowed: bool):
        self.scheduler = scheduler
        self.allowed = allowed

    def schedule(self, meeting: Meeting) -> str:
        if not self.allowed:
            return "access denied"
        return self.scheduler.schedule(meeting)

class LoggingProxy:
    def __init__(self, scheduler: Scheduler):
        self.scheduler = scheduler
        self.log: list[str] = []

    def schedule(self, meeting: Meeting) -> str:
        self.log.append(f"before {meeting.kind}")
        result = self.scheduler.schedule(meeting)
        self.log.append(f"after {meeting.kind}")
        return result
