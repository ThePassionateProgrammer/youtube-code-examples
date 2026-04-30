from dataclasses import dataclass

@dataclass
class Meeting:
    kind: str


class TeamScheduling:
    def schedule(self, meeting: Meeting) -> str:
        return "Scheduled team meeting"


class OneOnOneScheduling:
    def schedule(self, meeting: Meeting) -> str:
        return "Scheduled 1:1 meeting"


class AllHandsScheduling:
    def schedule(self, meeting: Meeting) -> str:
        return "Scheduled all-hands meeting"


class SchedulerFactory:
    def create(self, meeting: Meeting):
        if meeting.kind == "team":
            return TeamScheduling()
        elif meeting.kind == "one_on_one":
            return OneOnOneScheduling()
        return AllHandsScheduling()


def handle_request(meeting: Meeting, factory) -> str:
    scheduler = factory.create(meeting)
    return scheduler.schedule(meeting)


class FakeScheduler:
    def __init__(self):
        self.was_called = False

    def schedule(self, meeting: Meeting) -> str:
        self.was_called = True
        return "fake result"


class FakeFactory:
    def __init__(self, scheduler=None):
        self.scheduler = scheduler or FakeScheduler()

    def create(self, meeting: Meeting):
        return self.scheduler
