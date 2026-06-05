class MagazinePublisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def publish(self, issue):
        for subscriber in self.subscribers:
            subscriber.update(issue)

class EmailSubscriber:
    def update(self, issue):
        print(f"Email: new issue published — {issue}")

publisher = MagazinePublisher()
publisher.subscribe(EmailSubscriber())
publisher.publish("Design Patterns Monthly")
