# Patterns Are Not Solutions — Demo App (Python + Tests)

This repo supports the episode **“Patterns Are Not Solutions (And Never Were)”** using a single e-commerce example.

You get **three implementations** of the same discount behavior:

1. **Conditional (the trap)** — decisions and behavior entangled.
2. **Strategy (the force appears)** — independent variation becomes swappable.
3. **Template Method (force changes again)** — variation becomes *sets of steps*, not single policies.

All three end in a **green bar** and produce the same totals. The point is **design consequence**, not just correctness.

---

## Quick start

### 1) Create a venv + install pytest
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate  # Windows PowerShell
python -m pip install -U pip pytest
```

### 2) Run tests (should be green)
```bash
pytest -q
```

### 3) Run the tiny CLI demo (prints before/after totals)
```bash
python -m demo.run_all
```

---

## Folder layout

- `src/ecomm/` — domain + implementations
- `src/demo/` — runnable entry points for screen capture
- `tests/` — unit tests proving behavior (and showing why “green” ≠ “good design”)

---

## Screen-capture production plan (no scrolling, low cognitive load)

**Global capture settings**
- VS Code: **Minimap OFF**
- Font: **16–18**
- Use **split editor** (left/right) for comparisons
- No scrolling during a shot:
  - open the exact file + fold sections if needed
  - keep each shot to one screen

### Shot 1 — “The Trap” (conditional)
Open:
- `src/ecomm/checkout_conditional.py`

Highlight (cursor on the `if/elif` chain) and narrate:
- “Here’s what most people write… the checkout knows every discount type.”
- “That’s identity coupling. It grows.”

Suggested capture:
- 8–12 seconds static with cursor emphasis.

### Shot 2 — “The Force Appears” (Strategy)
Open side-by-side:
- Left: `src/ecomm/checkout_conditional.py`
- Right: `src/ecomm/checkout_strategy.py`

Highlight:
- the `DiscountPolicy` protocol
- the `CheckoutProcessor` constructor accepting a policy
- the factory in `src/ecomm/discount_factory.py`

Narration focus:
- “The variation is independent… now Strategy makes sense.”
- “We centralize identity decisions in the factory.”

### Shot 3 — “Template Method is different”
Open:
- `src/ecomm/discount_template.py`

Highlight:
- `DiscountTemplate.discount_cents()` (skeleton)
- subclass overrides: `eligible()` and `compute_discount()`

Narration focus:
- “Same overall algorithm. Variation is inside steps.”

### Shot 4 — “Replace, don’t stack”
Open side-by-side:
- Left: `src/ecomm/checkout_strategy.py`
- Right: `src/ecomm/checkout_template.py`

Narration focus:
- “Notice we delete, simplify, realign to the force.”

### Shot 5 — “Green bar doesn’t mean right design”
Run tests in terminal:
```bash
pytest -q
```
Capture the green output for 5–7 seconds.

Narration focus:
- “Tests tell you behavior. Patterns tell you structure.”

### Shot 6 — Tiny runnable outputs (optional)
Run:
```bash
python -m demo.run_all
```
Capture the printed totals.

Narration focus:
- “Same behavior. Different stability.”

---

## Suggested overlay cues
- “Trap: identity coupling”
- “Signal: independent variation”
- “Force changed: sets of steps”
- “Green bar ≠ good design”
