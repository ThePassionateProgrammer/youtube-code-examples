# UML Before / After

## Before

```text
MeetingCoordinator
├── schedule_team(meeting)
├── schedule_one_on_one(meeting)
├── schedule_all_hands(meeting)
├── _find_room(size)
├── _find_auditorium()
├── _reserve(room, time)
├── _notify_team(meeting)
├── _notify_individuals(meeting)
└── _notify_everyone(meeting)
```

Observation:
- Three public methods
- Same intent repeated: find room → reserve → notify
- Variation mixed with common process

## After

```text
SchedulingProcess
├── schedule(meeting)
├── find_room(meeting)        [abstract step]
├── notify(meeting)           [abstract step]
├── reserve(room, time)
└── scheduled_message(room)

TeamScheduling
OneOnOneScheduling
AllHandsScheduling
```

Observation:
- Common process captured once
- Variation isolated in overridable steps
- Template Method emerges from redundancy
