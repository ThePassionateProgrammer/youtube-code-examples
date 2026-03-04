# Production Notes — “Patterns Are Not Solutions (And Never Were)”

Designed for:
- 40% camera (key points)
- 60% screen (code + tests + before/after)

No tables. No scrolling. Short files.

---

## Capture checklist
- VS Code: minimap OFF
- Font: 16–18
- Split view for comparisons
- Cursor as a pointer (slow, deliberate)

---

## “You say” lines for the key shots

### Shot 1 — Conditional Trap (`checkout_conditional.py`)
You say:
- “Here’s what most people write.”
- “It works. It passes tests.”
- “But checkout now knows every discount identity.”
- “That coupling lives right here in the if/elif chain.”

Cursor:
- land on the `if order.customer.customer_type ...` chain
- pause 2 beats

---

### Shot 2 — Strategy Shift (`checkout_strategy.py` + `discount_factory.py`)
You say:
- “Now the force appears: discounts vary independently.”
- “So we move behavior behind an interface.”
- “And we move identity decisions into one place: the factory.”
- “This isolates identity coupling from the rest of the system.”

Cursor sequence:
1) `DiscountPolicy` protocol (in `discount_strategy.py`)
2) `CheckoutProcessor.__init__` (in `checkout_strategy.py`)
3) `DiscountFactory.build_policy` (in `discount_factory.py`) — pause on nested decisions

---

### Shot 3 — Template Method (force changed) (`discount_template.py`)
You say:
- “Template Method is not Strategy.”
- “The signal is different.”
- “The overall algorithm is stable… but steps vary.”
- “Eligibility and computation are the extension points.”

Cursor:
- `DiscountTemplate.discount_cents`
- then `eligible` / `compute_discount`

---

### Shot 4 — Replace, don’t stack (split view)
You say:
- “The advanced anti-pattern is clinging to a pattern.”
- “When the force changes, you replace.”
- “You delete.”
- “You simplify.”
- “You realign.”

Visual:
- split view: `checkout_strategy.py` vs `checkout_template.py`

---

### Shot 5 — Green bar
You say:
- “Both versions pass.”
- “Green bar is necessary… but it’s not sufficient.”
- “Tests tell you behavior.”
- “Patterns tell you structure.”

Capture:
- terminal `pytest -q` output

---

### Optional Shot 6 — `python -m demo.run_all`
You say:
- “Same totals.”
- “Different stability when the next requirement lands.”
