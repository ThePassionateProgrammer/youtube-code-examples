# Episode 9 Demo — Variation Wants to Be Data, Not Types

This demo includes:
- `bad_hierarchy.py` — the *trap*: class explosion when variation is encoded in identity
- `good_pipeline.py` — the *shift*: variation as data (a list of steps)
- `factory.py` — centralizes “which steps?” decisions
- `tests/` — unit tests proving the payoff

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Quick run (optional)
```bash
python -m demo_run
```

## Capture rules
- Font ≥ 16, minimap off
- One file per shot
- No scrolling during a shot
- Zoom/highlight only after you’ve frozen the frame
- Use the comments marked `# <-- SHOT` as your zoom targets
