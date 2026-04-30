from dataclasses import dataclass

@dataclass
class Meeting:
    kind: str
    size: int

class MeetingCoordinator:
    def schedule(self, meeting: Meeting) -> str:
        if meeting.kind == "team":
            return self._schedule_team(meeting)
        elif meeting.kind == "one_on_one":
            return self._schedule_one_on_one(meeting)
        elif meeting.kind == "all_hands":
            return self._schedule_all_hands(meeting)
        else:
            return self._schedule_default(meeting)

    def _schedule_team(self, meeting: Meeting) -> str:
        return f"Scheduled team meeting for {meeting.size} people"

    def _schedule_one_on_one(self, meeting: Meeting) -> str:
        return "Scheduled 1:1 meeting"

    def _schedule_all_hands(self, meeting: Meeting) -> str:
        return "Scheduled all-hands"

    def _schedule_default(self, meeting: Meeting) -> str:
        return "Scheduled generic meeting"
