from strategy_example import Meeting as StrategyMeeting, TeamStrategy, OneOnOneStrategy, schedule_with, schedule_two_ways
from template_method_example import Meeting as TemplateMeeting, TeamScheduler, OneOnOneScheduler
from proxy_example import Meeting as ProxyMeeting, Scheduler, ProtectionProxy, LoggingProxy
from bridge_example import Meeting as BridgeMeeting, EmailChannel, SlackChannel, TeamMeetingNotifier, CustomerMeetingNotifier
from factory_and_tests_example import MeetingRules, StrategyFactory, FakeStrategy, run_with_fake

def test_strategy_runs_two_interchangeable_behaviors():
    meeting = StrategyMeeting("weekly", participants=6)
    assert schedule_with(TeamStrategy(), meeting) == "team meeting for 6 people"
    assert schedule_with(OneOnOneStrategy(), meeting) == "1:1 meeting"

def test_strategy_two_calls_from_one_method():
    assert schedule_two_ways(StrategyMeeting("weekly", participants=6)) == ["team meeting for 6 people", "1:1 meeting"]

def test_template_method_varies_steps_inside_stable_process():
    meeting = TemplateMeeting("weekly", participants=6)
    assert TeamScheduler().schedule(meeting) == "large room for 6 | notify team"
    assert OneOnOneScheduler().schedule(meeting) == "small room | notify both people"

def test_protection_proxy_controls_access():
    scheduler = Scheduler()
    assert ProtectionProxy(scheduler, allowed=False).schedule(ProxyMeeting("team")) == "access denied"
    assert ProtectionProxy(scheduler, allowed=True).schedule(ProxyMeeting("team")) == "scheduled team"

def test_logging_proxy_varies_interaction_sequence():
    proxy = LoggingProxy(Scheduler())
    assert proxy.schedule(ProxyMeeting("team")) == "scheduled team"
    assert proxy.log == ["before team", "after team"]

def test_bridge_varies_two_independent_axes():
    assert TeamMeetingNotifier(EmailChannel()).notify(BridgeMeeting("planning")) == "email: team meeting: planning"
    assert CustomerMeetingNotifier(SlackChannel()).notify(BridgeMeeting("review")) == "slack: customer meeting: review"

def test_fake_strategy_records_structure_call():
    fake = FakeStrategy()
    result = run_with_fake(fake, StrategyMeeting("weekly", participants=6))
    assert result == "fake result"
    assert fake.called is True

def test_each_strategy_behavior_directly():
    meeting = StrategyMeeting("weekly", participants=6)
    assert TeamStrategy().schedule(meeting) == "team meeting for 6 people"
    assert OneOnOneStrategy().schedule(meeting) == "1:1 meeting"

def test_factory_selects_right_strategy():
    factory = StrategyFactory()
    assert isinstance(factory.create(MeetingRules("team")), TeamStrategy)
    assert isinstance(factory.create(MeetingRules("one_on_one")), OneOnOneStrategy)
