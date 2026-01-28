# Episode 02: Dependency Injection

Breaking tight coupling by injecting dependencies instead of creating them internally.

## The Problem

When a class creates its own dependencies internally, you can't substitute them for testing or different configurations. This is "sealed design."

## Files

| File | What it shows |
|------|---------------|
| `01_bad_no_seam.py` | The problem: PaymentService creates StripeClient internally |
| `02_factory_wiring.py` | Using a factory to wire dependencies |
| `03_bad_test_problem.py` | Why internal creation makes testing hard |
| `04_payment_service_di.py` | The solution: constructor injection |
| `05_call_site_before_after.py` | Before/after comparison at the call site |
| `06_test_with_fake.py` | Testing with a fake/mock client |

## Key Concept

**Seam**: A place where you can alter behavior without editing the code itself.

Constructor injection creates a seam—the dependency is passed in, so you can substitute a test double.

## Run

```bash
python 01_bad_no_seam.py
python 04_payment_service_di.py
```
