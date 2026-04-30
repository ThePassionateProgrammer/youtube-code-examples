# UML Before / After

## Before

```text
MeetingCoordinator
└── schedule(meeting)
    ├── if meeting.kind == "team"         -> _schedule_team(meeting)
    ├── elif meeting.kind == "one_on_one" -> _schedule_one_on_one(meeting)
    ├── elif meeting.kind == "all_hands"  -> _schedule_all_hands(meeting)
    └── else                              -> _schedule_default(meeting)
```

Observations:
- one class owns all scheduling behavior
- behavior is coupled to identity
- one method changes for multiple reasons

## After

```text
MeetingCoordinator
 └── SchedulingStrategyFactory.create(meeting)
      ├── TeamStrategy
      ├── OneOnOneStrategy
      ├── AllHandsStrategy
      └── DefaultStrategy

MeetingCoordinator -> SchedulingStrategy.schedule(meeting)
```

Observations:
- decision moved out of coordinator
- identity coupling isolated in factory
- usage is interface-based
- Strategy emerges, with factory choosing strategy
