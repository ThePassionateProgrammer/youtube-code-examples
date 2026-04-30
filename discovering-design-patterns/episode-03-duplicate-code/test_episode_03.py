from meeting_coordinator_before import MeetingCoordinator as BeforeCoordinator, Meeting as BeforeMeeting
from scheduling_process_after import (
    TeamScheduling,
    OneOnOneScheduling,
    AllHandsScheduling,
    Meeting as AfterMeeting,
)


def test_before_team_scheduling():
    coordinator = BeforeCoordinator()
    meeting = BeforeMeeting(kind="team", size=6, time="09:00")
    assert coordinator.schedule_team(meeting) == "Scheduled team meeting in Room-6"


def test_before_one_on_one_scheduling():
    coordinator = BeforeCoordinator()
    meeting = BeforeMeeting(kind="one_on_one", size=2, time="10:00")
    assert coordinator.schedule_one_on_one(meeting) == "Scheduled 1:1 meeting in Room-2"


def test_before_all_hands_scheduling():
    coordinator = BeforeCoordinator()
    meeting = BeforeMeeting(kind="all_hands", size=150, time="11:00")
    assert coordinator.schedule_all_hands(meeting) == "Scheduled all-hands in Auditorium"


def test_after_team_scheduling():
    process = TeamScheduling()
    meeting = AfterMeeting(kind="team", size=6, time="09:00")
    assert process.schedule(meeting) == "Scheduled team meeting in Room-6"


def test_after_one_on_one_scheduling():
    process = OneOnOneScheduling()
    meeting = AfterMeeting(kind="one_on_one", size=2, time="10:00")
    assert process.schedule(meeting) == "Scheduled 1:1 meeting in Room-2"


def test_after_all_hands_scheduling():
    process = AllHandsScheduling()
    meeting = AfterMeeting(kind="all_hands", size=150, time="11:00")
    assert process.schedule(meeting) == "Scheduled all-hands in Auditorium"
