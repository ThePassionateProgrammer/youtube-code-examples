# Episode 13 — Evolving Patterns with Emergent Design (Production Package)

This package is designed for **A-roll narration + B-roll screen capture**.

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
pytest -q
```

## Folder layout
- `script/episode13_performance_script.md` — performance script (no tables)
- `shots/shot_map.md` — step-by-step b-roll capture plan (what to show + what you say)
- `steps/` — Step 1→2 code (to illustrate evolution)
- `src/emergent_discounts/` — Step 3 runnable app (Strategy + Factory)
- `tests/` — unit tests (Step 1→3)
- `diagrams/` — Mermaid + PlantUML class diagrams

## Rendering diagrams
### Mermaid
Open `diagrams/step3_mermaid.md` in a Mermaid-capable Markdown viewer.

### PlantUML
Use a free VS Code extension (“PlantUML” by jebbs) and export PNG/SVG, or run PlantUML locally.
