# UML Before / After

## Before

```text
handle_request(meeting)
   ├── if meeting.kind == "team"         -> TeamScheduling()
   ├── elif meeting.kind == "one_on_one" -> OneOnOneScheduling()
   └── else                              -> AllHandsScheduling()

Caller:
- chooses concrete type
- creates concrete dependency
- immediately uses it
```

## After

```text
handle_request(meeting, factory)
        │
        ▼
  SchedulerFactory.create(meeting)
        ├── TeamScheduling()
        ├── OneOnOneScheduling()
        └── AllHandsScheduling()

Testing:
FakeFactory -> FakeScheduler
```

## Design Insight

- Without a factory, the caller controls instantiation.
- When the caller controls instantiation, testing is harder because you cannot easily substitute a fake.
- With a factory, construction is isolated and easy to control in tests.
- The factory knows identities. The rest of the system knows behavior.
