from dataclasses import dataclass
from strategy_example import SchedulingStrategy, TeamStrategy, OneOnOneStrategy, schedule_with

@dataclass
class MeetingRules:
    meeting_type: str

class StrategyFactory:
    def create(self, rules: MeetingRules) -> SchedulingStrategy:
        if rules.meeting_type == "team":
            return TeamStrategy()
        if rules.meeting_type == "one_on_one":
            return OneOnOneStrategy()
        raise ValueError(f"Unknown meeting type: {rules.meeting_type}")

class FakeStrategy(SchedulingStrategy):
    def __init__(self):
        self.called = False

    def schedule(self, meeting) -> str:
        self.called = True
        return "fake result"

def run_with_fake(fake: FakeStrategy, meeting) -> str:
    return schedule_with(fake, meeting)
