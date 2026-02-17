# Episode: The Cost of Being Clever — Demo Package

This repo is designed for **screen-capture walkthroughs**:
- A "clever" design that **looks senior** (multiple patterns, indirection)
- A "simple" design that fits the actual forces
- **Both are correct** (tests pass) — but one is *needlessly expensive to understand*

## Quick start

From the package root:

```bash
python -m venv .venv
source .venv/bin/activate   # mac/linux
# .venv\Scripts\activate  # windows

pip install -r requirements.txt
pytest -q
```

## What to screen-capture

### 1) Both designs go green
- Run: `pytest -q`
- Optional: `pytest -q -k clever`
- Optional: `pytest -q -k simple`

### 2) Clever version walkthrough
Open:
- `clever_checkout/checkout.py`
- `clever_checkout/factory.py`

The "impressive but unnecessary" parts:
- Strategy + Decorators + Validation Chain + Factory wiring
- Distributed decisions for just 3 rules

### 3) Simple version walkthrough
Open:
- `simple_checkout/checkout.py`

The "fits the problem" parts:
- Decisions live where the business rules live
- Low cognitive load
- Still testable and correct

## Domain scenario (same for both)
An e-commerce checkout with only **three rules**:
1. VIP customers get 10% off
2. Non-local region adds a flat shipping fee ($10)
3. Payment must be valid (otherwise fail)

For this episode, we keep the app fixed to those rules to demonstrate the cost of over-design.
