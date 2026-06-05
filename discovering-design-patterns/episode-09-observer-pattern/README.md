# Episode 09 — Observer Pattern Production Package

## Purpose
This package is designed to make the screen capture match the narration exactly.

The first visible code should be `wait_for_new_issue()` from `src/before_polling.py` because it literally shows:

1. check for change
2. wait
3. check again
4. download when available

## Run in VS Code

```bash
cd episode_09_observer_pattern_revised
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Files

- `src/before_polling.py` — polling trap and spreading polling examples
- `src/after_observer.py` — Observer implementation
- `src/syntax_examples.py` — Python, Java, JavaScript syntax examples
- `tests/test_observer_pattern.py` — pytest tests
- `uml/observer_pattern.md` — Mermaid UML class diagram
- `uml/polling_vs_observer.md` — polling vs Observer diagram
- `shot_list.md` — transcript-aligned production shot list

## Capture priority

1. Hook: `wait_for_new_issue()`
2. Pain: `poll_all_collaborators()` and concrete polling collaborators
3. Move: `MagazinePublisher.subscribe()` and `publish()`
4. Observers: `EmailSubscriber`, `AnalyticsSubscriber`, `MobileSubscriber`
5. Test: `test_publisher_notifies_a_subscriber_without_polling()`
6. UML: `observer_pattern.md`
```
