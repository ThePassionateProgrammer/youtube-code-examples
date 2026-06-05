# Episode 8 — State Pattern Production Package

## Episode
- Title: Why Your Code Breaks When State Changes
- Runtime target from transcript: ~4:18
- Domain: ATM interaction/session
- Pattern focus: State Pattern, with Flyweight discussion for shared stateless state objects

## Demo intent
Show that the same input can mean different things depending on the current state. The procedural version keeps asking “what mode am I in?” The object-oriented State Pattern delegates behavior to state objects so each state gives the input its meaning.

## Files
```text
episode_08_state_pattern/
  src/
    procedural_atm.py
    state_atm.py
  tests/
    test_atm_state_pattern.py
  diagrams/
    state_pattern_uml.svg/.png
    before_after_comparison.svg/.png
    flyweight_state_objects.svg/.png
  shot_list.md
  README.md
  pytest.ini
```

## Run tests
From this directory:

```bash
python -m pytest -q
```

Expected result:

```text
4 passed
```

## Suggested recording flow
1. Show `procedural_atm.py`, starting with `enter_number()`.
2. Show the repeated mode checks in multiple handlers.
3. Switch to `state_atm.py`, starting with `ATMSession` delegation methods.
4. Show `WelcomeState`, `WithdrawState`, and `DepositState` side-by-side or sequentially.
5. Show shared state constants: `WELCOME`, `AUTHENTICATED`, `WITHDRAW`, `DEPOSIT`.
6. Show UML diagrams near the pattern explanation.
7. Run tests in terminal.

## Visual emphasis
- Highlight only active lines.
- Avoid scrolling during shots.
- Use split screen for before/after comparison.
- Use the Flyweight diagram when discussing intrinsic behavior vs extrinsic session data.

## Note on terminology
When discussing Flyweight with State Pattern, the most precise wording is: the State objects contain shared intrinsic behavior; each `ATMSession` supplies extrinsic state/context such as PIN, amount, and balance. The Flyweight does not “attach state” to the stateless object; it separates shared behavior from per-session context.
