class MagazinePublisher {
  constructor() {
    this.listeners = [];
  }

  on(eventName, listener) {
    this.listeners.push({ eventName, listener });
  }

  emit(eventName, issue) {
    for (const entry of this.listeners) {
      if (entry.eventName === eventName) {
        entry.listener(issue);
      }
    }
  }
}

const publisher = new MagazinePublisher();
publisher.on("issuePublished", (issue) => {
  console.log(`Email: new issue published — ${issue}`);
});
publisher.emit("issuePublished", "Design Patterns Monthly");
