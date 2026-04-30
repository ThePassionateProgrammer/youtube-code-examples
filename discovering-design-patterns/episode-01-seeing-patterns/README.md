# Episode 1: Seeing Patterns in Problems

**The Passionate Programmer** — [@ThePassionateProgrammer](https://youtube.com/@ThePassionateProgrammer)

---

## What This Episode Teaches

Most developers see code as a series of steps. Experienced developers see **structure**.

This episode shows the shift from **procedural thinking** (directions) to **structural thinking** (a map) — and how that shift is what lets patterns emerge.

---

## The Code Story

### The Trap — Directions (`scheduler_procedural.py`)

```python
def schedule_team(meeting):
    room = find_room(meeting.size)
    reserve(room)
    notify_team(meeting)

def schedule_one_on_one(meeting):
    room = find_room(2)
    reserve(room)
    notify_individuals(meeting)
```

Two functions. Same shape. Slight variation. Clear and it works — but there is no model, no relationships, no place for behavior to live. This is procedural thinking: directions, not a map.

**The signal:** repeated steps with subtle variation. That's where a pattern is hiding.

---

### The Structural Move — Map (`scheduler_oop.py`)

```python
class SchedulingStrategy(ABC):
    @abstractmethod
    def schedule(self, meeting): ...

class TeamMeetingStrategy(SchedulingStrategy):
    def schedule(self, meeting):
        room = find_room(meeting.size)
        reserve(room)
        notify_team(meeting)

class Scheduler:
    def schedule(self, meeting, strategy):
        strategy.schedule(meeting)
```

Behavior now lives in objects. The `Scheduler` doesn't care what kind of meeting it schedules — it just calls `strategy.schedule()`. The variation is isolated. This is the **Strategy pattern** emerging naturally from the structure of the problem.

**The key insight:** the structural move doesn't change behavior. The tests prove it — both versions produce identical output.

---

## Running the Tests

```bash
pip install pytest
pytest test_scheduler.py -v
```

All 11 tests pass. The final test explicitly verifies that the procedural and OOP versions produce the same output — the structural move preserves behavior while changing where behavior lives.

---

## Pattern Signal

```
Repeated processes
Subtle variation
Step-based thinking
```

When you see this signal, ask: **what wants to vary?**

---

## The Three Abstraction Questions

1. **What's the same?** → similarity reveals structure
2. **What's different?** → difference reveals variation
3. **What's the context?** → context defines usefulness

---

## Files

| File | Purpose |
|------|---------|
| `scheduler_procedural.py` | The trap — procedural scheduling, directions not a map |
| `scheduler_oop.py` | The structural move — behavior in objects, Strategy pattern emerges |
| `test_scheduler.py` | 11 tests; proves structural move preserves behavior |
