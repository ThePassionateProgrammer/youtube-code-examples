# Episode 10 — Factories: Where Should Decisions Live in Code?
This folder contains a runnable Python mini-app + pytest tests that match the transcript beats.

## Quick start
1) Open this folder in VS Code.
2) Create/activate a venv (optional but recommended).
3) Install deps:
   pip install -r requirements.txt
4) Run tests:
   pytest -q
5) Run the tiny demo:
   python -m app.run_demo

## Folder map
- app/
  - domain.py              (Order + config)
  - policies.py            (discount + shipping policies)
  - trap_checkout.py       (BEFORE: construction+usage tangled)
  - factory_checkout.py    (AFTER: decisions migrated to a factory)
  - factories.py           (the factory: create/connect/return)
  - run_demo.py            (prints a couple scenarios)
- tests/
  - test_trap_checkout.py
  - test_factory_checkout.py
  - test_factories.py

## Screen-capture shot list (match to transcript timecodes)
Use *Screen Only* or *PiP* scenes. Each capture clip ~8–12s so you can add zooms/arrows in post.

### 0:36 — “construction and usage together”
File: app/trap_checkout.py
Show: `checkout_trap(...)` and highlight the three phases mixed together:
- identity decisions (if/else)
- construction (new Discount/Shipping objects)
- usage (calling `.apply()` / `.cost()`)

Zoom targets:
- the `if config.customer == ...` discount selection
- the `shipping_policy = ...` selection
- the final `discount.apply(...)` and `shipping.cost(...)` calls

No scrolling. If needed, increase font size so the whole function fits.

### 1:00 — “add one more discount rule”
Same file: app/trap_checkout.py
Show: the *new* “VIP + holiday” branch added to the discount selection.
Zoom target:
- `if config.customer == CustomerType.VIP and order.is_holiday: ...`

(Optional) Quick red circle/arrow on how the function grows.

### 1:30 — “show the decision in a factory”
File: app/factories.py
Show: `CheckoutFactory.build(config, order)` and point out:
- identity coupling lives here (conditionals are allowed here)

Zoom target:
- the discount selection block
- the shipping selection block

### 1:52 — “factory: create, connect, return”
Same file: app/factories.py
Show: the *three verbs* (you can literally point at them):
- Create: instantiate policy objects
- Connect: wire the composite `PricingEngine(discount, shipping)`
- Return: return the engine — **no `.apply()` calls here**

Zoom target:
- `engine = PricingEngine(discount=discount, shipping=shipping)`
- `return engine`

### 3:25 — Payoff: “add new discount type in factory”
File: app/policies.py + app/factories.py
Show:
1) `HolidayDiscount` class exists (small and cohesive)
2) Only the factory changed to start using it (call out OCP payoff)

Zoom target:
- `class HolidayDiscount(DiscountPolicy): ...`
- the factory branch that returns `HolidayDiscount(...)`

## Editing notes
- When you say “Factories instantiate objects but never call methods,” hold on the factory file and keep the cursor still.
- When you say “the rest of the system uses objects but never instantiates them,” cut to app/factory_checkout.py and highlight the line:
  `engine = CheckoutFactory.build(config, order)` then the line `return engine.checkout(order)`

Have fun — this package is designed for calm, friction-free walkthroughs.
