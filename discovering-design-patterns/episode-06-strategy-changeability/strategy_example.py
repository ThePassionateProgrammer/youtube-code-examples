from dataclasses import dataclass

@dataclass
class Meeting:
    kind: str
    participants: int = 2

class SchedulingStrategy:
    def schedule(self, meeting: Meeting) -> str:
        raise NotImplementedError()

class TeamStrategy(SchedulingStrategy):
    def schedule(self, meeting: Meeting) -> str:
        return f"team meeting for {meeting.participants} people"

class OneOnOneStrategy(SchedulingStrategy):
    def schedule(self, meeting: Meeting) -> str:
        return "1:1 meeting"

def schedule_with(strategy: SchedulingStrategy, meeting: Meeting) -> str:
    return strategy.schedule(meeting)

def schedule_two_ways(meeting: Meeting) -> list[str]:
    return [
        schedule_with(TeamStrategy(), meeting),
        schedule_with(OneOnOneStrategy(), meeting),
    ]
