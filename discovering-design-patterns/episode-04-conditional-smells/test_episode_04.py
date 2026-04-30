from conditional_before import Meeting as BeforeMeeting, MeetingCoordinator as BeforeCoordinator
from strategy_after import Meeting as AfterMeeting, MeetingCoordinator as AfterCoordinator, SchedulingStrategyFactory


def test_before_team():
    coordinator = BeforeCoordinator()
    assert coordinator.schedule(BeforeMeeting(kind="team", size=6)) == "Scheduled team meeting for 6 people"


def test_before_one_on_one():
    coordinator = BeforeCoordinator()
    assert coordinator.schedule(BeforeMeeting(kind="one_on_one", size=2)) == "Scheduled 1:1 meeting"


def test_before_all_hands():
    coordinator = BeforeCoordinator()
    assert coordinator.schedule(BeforeMeeting(kind="all_hands", size=200)) == "Scheduled all-hands"


def test_after_team():
    coordinator = AfterCoordinator()
    assert coordinator.schedule(AfterMeeting(kind="team", size=6)) == "Scheduled team meeting for 6 people"


def test_after_one_on_one():
    coordinator = AfterCoordinator()
    assert coordinator.schedule(AfterMeeting(kind="one_on_one", size=2)) == "Scheduled 1:1 meeting"


def test_after_all_hands():
    coordinator = AfterCoordinator()
    assert coordinator.schedule(AfterMeeting(kind="all_hands", size=200)) == "Scheduled all-hands"


def test_factory_selects_expected_types():
    factory = SchedulingStrategyFactory()
    assert factory.create(AfterMeeting(kind="team", size=6)).__class__.__name__ == "TeamStrategy"
    assert factory.create(AfterMeeting(kind="one_on_one", size=2)).__class__.__name__ == "OneOnOneStrategy"
    assert factory.create(AfterMeeting(kind="all_hands", size=200)).__class__.__name__ == "AllHandsStrategy"
    assert factory.create(AfterMeeting(kind="other", size=1)).__class__.__name__ == "DefaultStrategy"
