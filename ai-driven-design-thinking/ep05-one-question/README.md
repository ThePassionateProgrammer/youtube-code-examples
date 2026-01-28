# Episode 05: One Question

Focused design decisions through constraint.

## The Concept

When faced with complex design decisions, ask **one question at a time**:

- "What varies?" → Strategy pattern
- "What's stable vs. flexible?" → Core vs. edge separation
- "Who creates this?" → Factory pattern

## Files

| File | What it shows |
|------|---------------|
| `payment_service.py` | Evolution from conditionals to polymorphism, stable core vs. flexible edge |

## Key Insight

Separate **stable core** from **flexible edge**:

```
Stable Core          Flexible Edge
──────────────       ──────────────
PaymentProcessor     Logging
process()            FraudCheck
                     Receipt
```

The core defines the contract. The edge implements variations.

## Run

```bash
python payment_service.py
```
