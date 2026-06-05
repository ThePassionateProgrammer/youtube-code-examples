from unittest.mock import patch

from src.after_observer import (
    AnalyticsSubscriber,
    EmailSubscriber,
    FakeSubscriber,
    Issue as ObserverIssue,
    MagazinePublisher,
    MobileSubscriber,
)
from src.before_polling import Issue as PollingIssue, Magazine, Reader, wait_for_new_issue


def test_polling_checks_then_waits_then_downloads_when_issue_appears():
    magazine = Magazine()
    reader = Reader()

    # The side effect simulates the issue appearing after the first wait.
    def issue_appears(_seconds):
        magazine.publish(PollingIssue("Patterns Monthly"))

    with patch("src.before_polling.sleep", side_effect=issue_appears) as fake_sleep:
        wait_for_new_issue(magazine, reader, delay_seconds=60)

    fake_sleep.assert_called_once_with(60)
    assert reader.downloaded == ["Patterns Monthly"]


def test_publisher_notifies_a_subscriber_without_polling():
    publisher = MagazinePublisher()
    subscriber = FakeSubscriber()

    publisher.subscribe(subscriber)
    publisher.publish(ObserverIssue("Design Patterns Monthly"))

    assert subscriber.received == ["Design Patterns Monthly"]


def test_multiple_subscribers_react_differently_to_same_issue():
    publisher = MagazinePublisher()
    email = EmailSubscriber()
    analytics = AnalyticsSubscriber()
    mobile = MobileSubscriber()

    publisher.subscribe(email)
    publisher.subscribe(analytics)
    publisher.subscribe(mobile)
    publisher.publish(ObserverIssue("Observer Pattern Special"))

    assert email.sent == ["Email: Observer Pattern Special"]
    assert analytics.events == ["Tracked: Observer Pattern Special"]
    assert mobile.notifications == ["Push: Observer Pattern Special"]


def test_publisher_only_depends_on_update_protocol():
    publisher = MagazinePublisher()
    subscriber = FakeSubscriber()

    publisher.subscribe(subscriber)
    publisher.publish(ObserverIssue("Loose Coupling"))

    assert subscriber.received == ["Loose Coupling"]
