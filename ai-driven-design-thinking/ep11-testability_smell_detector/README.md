# Testability as a Smell Detector — Demo Repo

This repo contains a **BEFORE** version (low cohesion → “bundle tests”) and an **AFTER** version
(cohesive collaborators → atomic unit tests).

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
pip install -U pytest
pytest -q
```

## Code Shot Map (matches the episode script)

**CODE SHOT 1 — Big “bundle” test (multi-assert)**
- `tests/before/test_checkout_bundle_test.py`

**CODE SHOT 2 — Blob method doing many jobs**
- `src/before/checkout_before.py` → `CheckoutService.checkout(...)`

**CODE SHOT 3 — Multiple asserts highlighted**
- Same file as shot 1 (highlight the assertion block)

**CODE SHOT 4 — Refactor plan / new collaborators appear**
- `src/after/` folder tree in VS Code Explorer
- Optional: open `src/after/checkout_service.py` and skim constructor + `checkout(...)`

**CODE SHOT 5 — DiscountPolicy + implementations**
- `src/after/discounts.py`

**CODE SHOT 6 — ShippingCalculator**
- `src/after/shipping.py`

**CODE SHOT 7 — CheckoutService simplified**
- `src/after/checkout_service.py`

**CODE SHOT 8 — Atomic unit test (discount only)**
- `tests/after/test_discount_policy.py`

**CODE SHOT 9 — Atomic unit test (shipping only)**
- `tests/after/test_shipping_calculator.py`

**CODE SHOT 10 — Small orchestration test**
- `tests/after/test_checkout_service_orchestration.py`

## Domain (kept consistent with the playlist)
- Cart items (sku, qty, unit_price)
- Customer (vip flag)
- Environment/config (e.g., `seasonal_discount_enabled`, `free_shipping_threshold`)
- Policies: discount, shipping, tax
