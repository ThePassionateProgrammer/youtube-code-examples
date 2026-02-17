# 🎬 Episode: Where Should Decisions Live in Code?
**Series:** AI-Driven Design Thinking  
**Runtime target:** 8–12 min  
**Ratio:** ~60% code walkthrough (VO over screen), ~40% camera (key points)  
**Core move:** *Decision Migration* → move identity decisions into factories.

---

## Quick Production Plan (What you do)
1. **Open the project** (folder `app/`) in VS Code.
2. Run tests once: `pytest -q` (record a quick “tests passing” terminal shot).
3. Record **A-roll**: read only the **Camera** lines below (leave space to ad-lib).
4. Record **Screen Capture** (silent) using the **Shot List** (no scrolling).
5. In edit: place A-roll, then drop in the screen captures at the referenced timestamps/markers.
6. Add slow zooms/highlights on the indicated lines (minimal arrows).

---

## HOOK OPTIONS (choose ONE)

### Hook A — Code-first cold open (recommended)
| Audio (VO) | Visual |
|---|---|
| “This checkout function *works*… but it hides four business decisions inside it.” | **SHOT 1**: `checkout_procedural.py` (top of file) |
| “And that’s why it gets harder to test and harder to change.” | Hold on same shot, slow zoom to the `if` blocks |

**CAMERA (cut in at ~0:08)**  
“Most software doesn’t have an if/else problem. It has a **decision placement** problem.”

---

### Hook B — Verbal reframe
**CAMERA**  
“Most code isn’t rigid because it’s complex. It’s rigid because decisions are scattered everywhere.”

Then cut to **SHOT 1**.

---

### Hook C — Pain statement
**CAMERA**  
“If your code is hard to test and brittle to change, there’s a good chance decisions are living in the wrong place.”

Then cut to **SHOT 1**.

---

# SCRIPT (Integrated: Camera + VO + Code Walkthrough)

## LINE 1 — The Trap: decisions + construction + behavior all mixed
**CAMERA (short)**  
“Let’s start with the trap. This is how most checkout code begins.”

| Audio (VO) | Visual |
|---|---|
| “Here’s the trap: we’re deciding what objects we need…” | **SHOT 1**: `checkout_procedural.py` full screen |
| “…we’re constructing them…” | Zoom: the `VipDiscount()` / `StandardDiscount()` lines |
| “…and we’re using them, all in one function.” | Zoom: the `total =` lines |
| “That tangles identity decisions with behavior.” | Hold (no scrolling) |

**Transition (CAMERA)**  
“Now watch what happens when requirements change.”

---

## LINE 2 — Why it hurts: change multiplies edits and tests
| Audio (VO) | Visual |
|---|---|
| “Add one more discount rule…” | **SHOT 2**: `checkout_procedural.py` (highlight comment block `# NEW REQUIREMENT`) |
| “Add one more shipping policy…” | Hold; slow pan to shipping `if env` section |
| “Now this function is a crossroads. Every change forces edits here.” | Hold; gentle zoom out to show both `if` blocks |
| “And testing gets harder because each path is wired to real construction.” | **SHOT 3**: `tests/test_procedural_checkout.py` awkward test |

**Transition (CAMERA)**  
“This is where we do the decision migration move.”

---

## LINE 3 — Decision Migration Moment: move identity decisions into a factory
**CAMERA (anchor)**  
“This is the moment everything changes: we move **decisions out of behavior**—and into a factory.”

| Audio (VO) | Visual |
|---|---|
| “A factory is allowed to know identities.” | **SHOT 4**: `factory.py` full screen |
| “It can contain conditionals…” | Zoom: the `if user.is_vip` block |
| “…because that’s where identity coupling belongs.” | Hold |
| “But here’s rule one:” | Still on factory |
| “Factories may instantiate objects, but they must never call methods on them.” | Zoom: show only constructors used, no `.apply()`/`.cost()` |
| “Notice: create, connect, return. No behavior calls.” | Hold |

**Transition (CAMERA)**  
“Now the rest of the system gets to be boring. Boring is good.”

---

## LINE 4 — Client becomes boring: behavior only, no construction
| Audio (VO) | Visual |
|---|---|
| “Checkout now receives a policy.” | **SHOT 5**: `checkout.py` full screen |
| “It doesn’t decide what to use.” | Zoom: function signature `checkout(order, pricing_policy)` |
| “It just uses behavior.” | Zoom: `return pricing_policy.total(order)` |
| “This is rule two:” | Hold |
| “The rest of your code can call methods, but it must never instantiate.” | Hold |

**Transition (CAMERA)**  
“And now testing becomes straightforward.”

---

## LINE 5 — Testing factories: input rules, assert identity outputs
| Audio (VO) | Visual |
|---|---|
| “Testing factories is easy.” | **SHOT 6**: `tests/test_factory.py` full screen |
| “Give it business rules…” | Zoom: `factory.create(user=..., env=...)` |
| “…and verify you got the right objects back.” | Zoom: `isinstance(...)` asserts |
| “Identity coupling is contained.” | Hold |

**(Subscribe moment — ~2/3 through)**  
**CAMERA (natural, calm)**  
“If this is clicking, subscribe. This series is a set of design lenses—one per episode—and they stack.”

---

## LINE 6 — The payoff: extensibility without caller breakage
| Audio (VO) | Visual |
|---|---|
| “Now we can add a new discount type…” | **SHOT 7**: `discounts.py` (`SeasonalDiscount`) |
| “…by changing the factory, not every caller.” | **SHOT 4**: back to `factory.py` (new branch) |
| “The client stays closed for modification.” | **SHOT 5**: `checkout.py` (unchanged) |
| “That’s Open/Closed in the real world.” | Hold |

**Transition (CAMERA)**  
“Claude gave me a helpful way to phrase what’s happening here.”

---

## Claude cameo (short)
**CAMERA**  
“When I was working with Claude, it said: ‘Factories are where your system admits what it *believes* about identities.’  
And that’s exactly right. It’s the belief layer.”

---

## SINKER OPTIONS (choose ONE)

### Sinker A — Open loop (recommended)
**CAMERA**  
“Now that decisions are centralized, a new risk appears: we can get *too clever* with factories.  
That’s the next episode: **The Cost of Being Clever**.”

### Sinker B — Direct watch-next
**CAMERA**  
“Watch **The Cost of Being Clever** next. We’ll see how factories go wrong—and how to keep them clean.”

### Sinker C — Playlist frame
**CAMERA**  
“If you want the full mental model, start at the beginning of the playlist. Each episode adds one new shape.”

---

# Shot List (No scrolling, 8–12 seconds each)
1. `checkout_procedural.py` — the trap (both `if` blocks visible)
2. `checkout_procedural.py` — “new requirement” comment section
3. `tests/test_procedural_checkout.py` — awkward test / friction
4. `factory.py` — decisions live here (conditionals)
5. `checkout.py` — boring client (no instantiation)
6. `tests/test_factory.py` — factory tests (identity assertions)
7. `discounts.py` — adding a new implementation
8. Terminal — `pytest -q` passing (optional payoff beat)

---

# Commands
```bash
cd app
python -m pip install -r requirements.txt
pytest -q
python main.py
```
