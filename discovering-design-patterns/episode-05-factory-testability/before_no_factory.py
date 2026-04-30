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

def handle_request(meeting: Meeting) -> str:
    if meeting.kind == "team":
        scheduler = TeamScheduling()
    elif meeting.kind == "one_on_one":
        scheduler = OneOnOneScheduling()
    else:
        scheduler = AllHandsScheduling()
    return scheduler.schedule(meeting)
