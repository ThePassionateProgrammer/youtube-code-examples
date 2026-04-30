from dataclasses import dataclass

@dataclass
class Meeting:
    kind: str
    size: int

class SchedulingStrategy:
    def schedule(self, meeting: Meeting) -> str:
        raise NotImplementedError()

class TeamStrategy(SchedulingStrategy):
    def schedule(self, meeting: Meeting) -> str:
        return f"Scheduled team meeting for {meeting.size} people"

class OneOnOneStrategy(SchedulingStrategy):
    def schedule(self, meeting: Meeting) -> str:
        return "Scheduled 1:1 meeting"

class AllHandsStrategy(SchedulingStrategy):
    def schedule(self, meeting: Meeting) -> str:
        return "Scheduled all-hands"

class DefaultStrategy(SchedulingStrategy):
    def schedule(self, meeting: Meeting) -> str:
        return "Scheduled generic meeting"

class SchedulingStrategyFactory:
    def create(self, meeting: Meeting):
        if meeting.kind == "team":
            return TeamStrategy()
        elif meeting.kind == "one_on_one":
            return OneOnOneStrategy()
        elif meeting.kind == "all_hands":
            return AllHandsStrategy()
        else:
            return DefaultStrategy()

class MeetingCoordinator:
    def __init__(self, factory=None):
        self.factory = factory or SchedulingStrategyFactory()

    def schedule(self, meeting: Meeting) -> str:
        strategy = self.factory.create(meeting)
        return strategy.schedule(meeting)
