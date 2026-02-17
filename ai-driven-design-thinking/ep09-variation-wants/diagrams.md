# Episode 9 Diagrams

## 2^n class explosion (ASCII)
```
Optional behaviors (axes): Logging, FraudCheck, Retries, Audit, Metrics ...

Each new optional behavior doubles combinations.

n=1 → 2
n=2 → 4
n=3 → 8
n=4 → 16
n=5 → 32
```

## Pipeline as “variation = data” (Mermaid)
```mermaid
classDiagram
    class Pipeline {
      -steps: List~Step~
      +run(ctx): PaymentContext
    }
    class Step {
      <<interface>>
      +process(ctx): void
    }
    class ValidateAmount {
      +process(ctx): void
    }
    class FraudCheck {
      +process(ctx): void
    }
    class LogStep {
      +process(ctx): void
    }
    class ChargeStripe {
      +process(ctx): void
    }

    Pipeline o-- Step : steps (data)
    Step <|.. ValidateAmount
    Step <|.. FraudCheck
    Step <|.. LogStep
    Step <|.. ChargeStripe
```
