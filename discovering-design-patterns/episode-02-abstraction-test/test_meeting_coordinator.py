from meeting_coordinator_before import MeetingCoordinator as BeforeCoordinator, Meeting as BeforeMeeting
from scheduling_process_after import (
    TeamSchedulingProcess,
    OneOnOneSchedulingProcess,
    AllHandsSchedulingProcess,
    Meeting as AfterMeeting,
)


def test_before_team_schedule():
    coordinator = BeforeCoordinator()
    meeting = BeforeMeeting(kind="team", size=6, time="10:00")
    result = coordinator.schedule_team(meeting)
    assert "Reserved Room for 6 at 10:00" in result
    assert "Notified team" in result


def test_before_one_on_one_schedule():
    coordinator = BeforeCoordinator()
    meeting = BeforeMeeting(kind="one_on_one", size=2, time="11:00")
    result = coordinator.schedule_one_on_one(meeting)
    assert "Reserved Room for 2 at 11:00" in result
    assert "Notified individuals" in result


def test_before_all_hands_schedule():
    coordinator = BeforeCoordinator()
    meeting = BeforeMeeting(kind="all_hands", size=100, time="13:00")
    result = coordinator.schedule_all_hands(meeting)
    assert "Reserved Auditorium at 13:00" in result
    assert "Notified everyone" in result


def test_after_team_schedule():
    process = TeamSchedulingProcess()
    meeting = AfterMeeting(kind="team", size=6, time="10:00")
    result = process.schedule(meeting)
    assert result == "Reserved Room for 6 at 10:00 | Notified team for team"


def test_after_one_on_one_schedule():
    process = OneOnOneSchedulingProcess()
    meeting = AfterMeeting(kind="one_on_one", size=2, time="11:00")
    result = process.schedule(meeting)
    assert result == "Reserved Room for 2 at 11:00 | Notified individuals for one_on_one"


def test_after_all_hands_schedule():
    process = AllHandsSchedulingProcess()
    meeting = AfterMeeting(kind="all_hands", size=100, time="13:00")
    result = process.schedule(meeting)
    assert result == "Reserved Auditorium at 13:00 | Notified everyone for all_hands"
