from before_no_factory import Meeting as BeforeMeeting, handle_request as handle_before
from after_factory import (
    Meeting as AfterMeeting, 
    handle_request as handle_after,
    SchedulerFactory, FakeFactory, FakeScheduler,
)

def test_before_team_request():
    result = handle_before(BeforeMeeting("team"))
    assert result == "Scheduled team meeting"

def test_before_one_on_one_request():
    result = handle_before(BeforeMeeting("one_on_one"))
    assert result == "Scheduled 1:1 meeting"

def test_before_all_hands_request():
    result = handle_before(BeforeMeeting("all_hands"))
    assert result == "Scheduled all-hands meeting"

def test_factory_creates_expected_scheduler_types():
    factory = SchedulerFactory()
    assert factory.create(AfterMeeting("team")).__class__.__name__ == "TeamScheduling"
    assert factory.create(AfterMeeting("one_on_one")).__class__.__name__ == "OneOnOneScheduling"
    assert factory.create(AfterMeeting("all_hands")).__class__.__name__ == "AllHandsScheduling"

def test_after_handle_request_with_fake_factory_returns_fake_result():
    fake_factory = FakeFactory()
    result = handle_after(AfterMeeting("team"), fake_factory)
    assert result == "fake result"

def test_after_handle_request_calls_fake_scheduler():
    fake_scheduler = FakeScheduler()
    fake_factory = FakeFactory(fake_scheduler)
    handle_after(AfterMeeting("team"), fake_factory)
    assert fake_scheduler.was_called is True
