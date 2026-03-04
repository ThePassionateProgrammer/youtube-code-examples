# Episode 9 — B‑Roll + Demo Package (Variation Wants to Be Data, Not Types)

This folder gives you:
1) A runnable Python demo + tests you can show in VS Code (pytest)
2) A **shot-by-shot b‑roll plan** mapped to your transcript timecodes
3) A **“no scrolling” capture workflow**

## Quick start (VS Code)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
python -m app.demo_run
```

## Capture rules (low cognitive load)
- Minimap OFF
- Font 16+ (or 18)
- One file per shot
- No scrolling during a shot (use Cmd+F to jump)
- Highlight active line(s) OR blur/dim unused code

## Shot plan (drop‑in b‑roll)

### Hook (0:00–0:30)
**H1 (0:00–0:09)** `app/legacy_explosion.py` → highlight `count_combinations()` (`2 ** len(options)`).
**H2 (0:00–0:30)** same file → run it (terminal shows generated class names).

### 1:27 Class explosion
`app/legacy_explosion.py` → hover `EXAMPLE_OPTIONS` then point at `count_combinations()`.

### 1:47 Branches multiply
Same file → arrow/callout on `2 ** len(options)` (“Multiply, not add”).

### 2:07 Optional behavior in code
`app/legacy_subclasses.py` → show 3 example subclasses; callout “option → new identity”.

### 2:28 In code (base flow + options)
Same file → highlight `BasePaymentFlow.process()` and one override.

### 6:20 List of steps
`app/pipeline.py` → highlight `Pipeline.run()` (“boring loop”).

### 6:43 Code walkthrough (new shape)
`app/steps.py` → highlight shared `run(ctx)` across 3 steps.

### 7:12 The list (variation becomes data)
`app/factory.py` → highlight `build_payment_pipeline()` returning `list[Step]`.

### 8:35 Show tests
`tests/test_steps_unit.py` → show one atomic test.
Terminal → `pytest -q` green bar.

## Blur everything except one line (fast Premiere trick)
1) Duplicate the code clip (two identical layers).
2) Bottom layer: add **Gaussian Blur**.
3) Top layer: add **Opacity mask** around the 1–2 lines you want sharp (feather 0–5).
Result: background blurred, target line crisp.
