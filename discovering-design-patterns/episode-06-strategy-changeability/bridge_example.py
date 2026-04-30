from dataclasses import dataclass

@dataclass
class Meeting:
    kind: str

class NotificationChannel:
    def send(self, message: str) -> str:
        raise NotImplementedError()

class EmailChannel(NotificationChannel):
    def send(self, message: str) -> str:
        return f"email: {message}"

class SlackChannel(NotificationChannel):
    def send(self, message: str) -> str:
        return f"slack: {message}"

class MeetingNotifier:
    def __init__(self, channel: NotificationChannel):
        self.channel = channel

    def notify(self, meeting: Meeting) -> str:
        raise NotImplementedError()

class TeamMeetingNotifier(MeetingNotifier):
    def notify(self, meeting: Meeting) -> str:
        return self.channel.send(f"team meeting: {meeting.kind}")

class CustomerMeetingNotifier(MeetingNotifier):
    def notify(self, meeting: Meeting) -> str:
        return self.channel.send(f"customer meeting: {meeting.kind}")
