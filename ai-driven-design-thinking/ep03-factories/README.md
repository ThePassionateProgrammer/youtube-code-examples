# Episode 03: Factories

Using factory patterns to manage object creation and reduce strategy proliferation.

## The Problem

When you have multiple interrelated strategies (fee calculation, charging, receipts) for each provider (Stripe, PayPal, AcmePay), manually wiring them becomes error-prone.

## Files

| File | What it shows |
|------|---------------|
| `01_strategies.py` | Strategy interfaces and implementations for each provider |
| `02_pipeline_v1_strategy_only.py` | Pipeline using raw strategies (verbose wiring) |
| `03_factories.py` | Factory pattern to bundle related strategies |
| `04_pipeline_v2_factory_only.py` | Cleaner pipeline using factories |
| `05_tests.py` | Testing the factory-based approach |

## Key Concept

**Factory**: Encapsulates the creation of related objects so the client doesn't need to know the details.

Instead of passing three separate strategies, pass one factory that creates all three.

## Run

```bash
python 01_strategies.py
python 03_factories.py
python 05_tests.py
```
