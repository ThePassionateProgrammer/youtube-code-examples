# UML / Diagram References

Generated diagrams are in `diagrams/` as SVG and PNG.

## State Pattern UML
- `diagrams/state_pattern_uml.svg`
- `diagrams/state_pattern_uml.png`

## Before / After Comparison
- `diagrams/before_after_comparison.svg`
- `diagrams/before_after_comparison.png`

## Flyweight With State Objects
- `diagrams/flyweight_state_objects.svg`
- `diagrams/flyweight_state_objects.png`

## Mermaid source: State Pattern

```mermaid
classDiagram
    class ATMSession {
      ATMState state
      pin
      amount
      balance
      enter_number(value)
      press_ok()
      select_withdraw()
      select_deposit()
    }
    class ATMState {
      <<interface>>
      enter_number(session, value)
      press_ok(session)
      press_cancel(session)
      select_withdraw(session)
      select_deposit(session)
    }
    class WelcomeState
    class AuthenticatedState
    class WithdrawState
    class DepositState
    ATMSession --> ATMState : delegates to
    ATMState <|.. WelcomeState
    ATMState <|.. AuthenticatedState
    ATMState <|.. WithdrawState
    ATMState <|.. DepositState
```

## Mermaid source: Flyweight framing

```mermaid
classDiagram
    class ATMSession {
      state
      pin
      amount
      balance
      extrinsic context
    }
    class SharedStateObjects {
      WELCOME
      AUTHENTICATED
      WITHDRAW
      DEPOSIT
      intrinsic behavior
    }
    ATMSession --> SharedStateObjects : references
```
