# Video 5 Production Package — Factory for Testability

## Purpose
This package supports the testability-driven version of Video 5.

It demonstrates:
- why object creation inside callers makes testing harder
- how a factory isolates construction
- how a fake factory can return a fake dependency in tests
- how separating construction from usage improves control

## Files
- `before_no_factory.py` — caller directly controls instantiation
- `after_factory.py` — factory-based refactor with fake factory examples
- `test_video_5.py` — runnable pytest tests
- `UML_before_after.md` — conceptual diagrams
- `shot_list.md` — screen capture plan and suggested effects
- `test_output.txt` — pytest output

## Run in VS Code

```bash
pytest -q
```

## Capture Notes
- Use VS Code dark theme
- Zoom so code is approximately 30–34px equivalent
- No scrolling during a shot
- Prefer static screenshots or frozen code clips
- Hold 2 seconds before/after each shot
- For emphasis, highlight constructor lines before factory extraction
