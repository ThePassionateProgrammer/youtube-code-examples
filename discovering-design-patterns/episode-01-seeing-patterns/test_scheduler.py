"""
Tests for Episode 1: Seeing Patterns in Problems
The Passionate Programmer — @ThePassionateProgrammer

Tests show both the procedural and OOP approaches work identically.
The structural move doesn't change behavior — it changes where behavior lives.
"""

import pytest
from unittest.mock import patch, call

from scheduler_procedural import schedule_team, schedule_one_on_one
from scheduler_oop import (
    Scheduler,
    TeamMeetingStrategy,
    OneOnOneMeetingStrategy,
    SchedulingStrategy,
)


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture
def team_meeting():
    return {"title": "Sprint Planning", "size": 5}


@pytest.fixture
def one_on_one_meeting():
    return {
        "title": "1:1 with Alex",
        "size": 2,
        "attendees": ["Alex", "David"],
    }


# ── Procedural tests ──────────────────────────────────────────────────────────

class TestProceduralScheduler:

    def test_schedule_team_reserves_correct_room(self, team_meeting, capsys):
        schedule_team(team_meeting)
        output = capsys.readouterr().out
        assert "Room B" in output          # size 5 → Room B

    def test_schedule_team_notifies_team(self, team_meeting, capsys):
        schedule_team(team_meeting)
        output = capsys.readouterr().out
        assert "Sprint Planning" in output

    def test_schedule_one_on_one_reserves_room_a(self, one_on_one_meeting, capsys):
        schedule_one_on_one(one_on_one_meeting)
        output = capsys.readouterr().out
        assert "Room A" in output          # size 2 → Room A

    def test_schedule_one_on_one_notifies_each_attendee(self, one_on_one_meeting, capsys):
        schedule_one_on_one(one_on_one_meeting)
        output = capsys.readouterr().out
        assert "Alex" in output
        assert "David" in output


# ── OOP / Strategy tests ──────────────────────────────────────────────────────

class TestStrategyScheduler:

    def test_team_strategy_reserves_correct_room(self, team_meeting, capsys):
        Scheduler().schedule(team_meeting, TeamMeetingStrategy())
        output = capsys.readouterr().out
        assert "Room B" in output

    def test_team_strategy_notifies_team(self, team_meeting, capsys):
        Scheduler().schedule(team_meeting, TeamMeetingStrategy())
        output = capsys.readouterr().out
        assert "Sprint Planning" in output

    def test_one_on_one_strategy_reserves_room_a(self, one_on_one_meeting, capsys):
        Scheduler().schedule(one_on_one_meeting, OneOnOneMeetingStrategy())
        output = capsys.readouterr().out
        assert "Room A" in output

    def test_one_on_one_strategy_notifies_individuals(self, one_on_one_meeting, capsys):
        Scheduler().schedule(one_on_one_meeting, OneOnOneMeetingStrategy())
        output = capsys.readouterr().out
        assert "Alex" in output
        assert "David" in output

    def test_strategy_is_swappable(self, team_meeting, one_on_one_meeting, capsys):
        """The Scheduler doesn't care what strategy it gets — it just calls it."""
        scheduler = Scheduler()
        scheduler.schedule(team_meeting, TeamMeetingStrategy())
        scheduler.schedule(one_on_one_meeting, OneOnOneMeetingStrategy())
        output = capsys.readouterr().out
        assert "Room B" in output
        assert "Room A" in output

    def test_strategy_follows_interface(self):
        """Any new strategy must implement schedule()."""
        class CustomStrategy(SchedulingStrategy):
            def schedule(self, meeting: dict) -> None:
                pass  # custom behavior here

        # Should not raise — follows the interface
        Scheduler().schedule({"title": "All Hands", "size": 10}, CustomStrategy())

    def test_procedural_and_oop_produce_same_output(self, team_meeting, capsys):
        """Structural move preserves behavior. Only the structure changed."""
        schedule_team(team_meeting)
        procedural_output = capsys.readouterr().out

        Scheduler().schedule(team_meeting, TeamMeetingStrategy())
        oop_output = capsys.readouterr().out

        assert procedural_output == oop_output
