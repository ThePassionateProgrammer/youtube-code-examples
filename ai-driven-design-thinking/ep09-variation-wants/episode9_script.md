# 🎥 Episode 9 — Variation Wants to Be Data, Not Types
**Series:** AI‑Driven Design Thinking  
**Target length:** 8–12 minutes  
**Style:** Studio vibe (relaxed, spacious), but code-forward (≈60% screen / 40% camera)

---

## Quick Promise (what they get)
By the end, the viewer can:
- **Spot** when “variation is being encoded in identity” (class explosion)
- **Refactor** from a growing subclass web into a **data-driven pipeline**
- **Understand** why this makes code easier for *humans* and safer for *AI* to extend

---

## HOOK — 3 Options (pick 1)

### Hook A — Code‑First Cold Open (recommended)
**[SCREEN | Shot H1: tests / scenario matrix]**  
**VO (calm, one sentence):**  
“This is what class explosion looks like in real life: every new option doubles your code *and* your tests.”

**[SCREEN | Shot H2: `bad_hierarchy.py` — the subclasses list / tree comment]**  
**VO:**  
“This isn’t sloppy code. It’s a *logical* model — and that’s why it’s so dangerous.”

**[CAMERA]**  
“Today I’ll show you the move that fixes it: **variation wants to be data, not types**.”

---

### Hook B — Verbal Reframe (mobile-safe)
**[CAMERA]**  
“Most systems don’t have an *if/else* problem. They have an *identity* problem.  
They keep turning options into new types… until the design explodes.”

**[SCREEN | Shot H2]**  
“And once you see it, you can fix it in minutes.”

---

### Hook C — Claude cameo (quick)
**[CAMERA]**  
“I asked Claude to ‘add a feature’ to this design… and it did exactly what most teams do: it added another subclass.”

**[SCREEN | Shot H2]**  
“Claude didn’t fail. The design *forced* that move. Let’s fix the design.”

---

# LINE 1 — “Why do hierarchies explode?”
## The Question
**[CAMERA]**  
“Why does a clean little inheritance tree turn into a jungle?”

## The Trap (naive solution)
**[CAMERA]**  
“The naive move — and honestly the move AI will often take — is:  
‘Just make a subclass for the new behavior.’”

### Talking points (ad‑lib bullets — keep it roomy)
- It feels neat: *one new requirement → one new class*
- It feels “OO”: specialization, reuse, clean names
- It keeps existing code untouched… *at first*
- The first dimension of variation is fine
- The second is tolerable
- The third is when teams start saying: “don’t touch it”

## Freeze & Diagnose
**[CAMERA | pause]**  
“Let’s look at the **shape of this friction**.”

### Talking points
- The hidden math: **combinations**
- Each optional behavior creates a branch
- Branches multiply, they don’t add

## Show the Move (visual beat)
**[SCREEN | Shot 1: class explosion tree / list]**  
**Scripted walkthrough (read this):**  
“Here’s the problem in code.  
We have a base payment flow… and then we start layering optional behaviors: logging, fraud checks, retries, extra validation.  
Each one seems innocent — but now the number of *possible* processors isn’t four.  
It’s **two to the N**.”

### Payoff
**[CAMERA]**  
“So class explosion isn’t a mistake.  
It’s a *signal* that variation is being encoded in identity.”

**Transition to Line 2 (scripted):**  
“Now we can name the real culprit — and it’s not inheritance. It’s what we’re asking inheritance to do.”

---

# LINE 2 — “What are we encoding in identity?”
## The Question
**[CAMERA]**  
“What exactly is going wrong when we create ‘this plus a little more’ types?”

## The Trap
**[CAMERA]**  
“We confuse two different uses of inheritance.”

### Talking points (ad‑lib)
- Inheritance can be fine for **classification**
- But we use it for “specialization” of behavior
- And behavior isn’t one thing — it varies across dimensions

## The Insight (Claude saves the day)
**[CAMERA]**  
“I was explaining this to Claude, and it gave me the line that made it click.”

**Claude cameo (you say, calmly):**  
> “Classes are about who I am. Methods are about what I do.” — Claude

**Your follow-up:**  
“Yes. And class explosion happens when we keep encoding **what I do** into **who I am**.”

### Talking points (cap at 3 before screen)
- Concrete subclassing = *identity coupling*
- Abstract roles = *does‑ness* (behavior behind an interface)
- When variation lives in identity, every new combination becomes a new *type*

## Show the move (visual beat)
**[SCREEN | Shot 2: highlight “options became identity” lines]**  
**Scripted walkthrough:**  
“Notice what’s happening: we’re not just saying ‘this is a PaymentProcessor.’  
We’re saying: ‘this is a PaymentProcessorWithLoggingAndFraudAndRetries…’  
The *options* became the *identity*.”

### Payoff
**[CAMERA]**  
“And that’s why you end up tracing code like it’s procedural.  
OO wants layers. Procedural wants linear flow.  
When we encode behavior in identity, we lose the layers.”

**Transition to Line 3:**  
“Okay — so what’s the replacement move? We don’t throw away OO. We relocate the variation.”

---

# LINE 3 — “What does it mean to make variation data?”
## The Question
**[CAMERA]**  
“What does it look like when variation is data instead of types?”

## The Trap
**[CAMERA]**  
“The trap is to think ‘data-driven’ means ‘not OO’ — like we’re giving up polymorphism.”

### Talking points (ad‑lib)
- We keep polymorphism
- We make it **shallow**
- We move the combinations into **a structure**

## Freeze & Diagnose
**[CAMERA]**  
“Here’s the principle:  
**variation wants to be data — not types**.”

### Talking points (cap at 3 before screen)
- One abstraction per step
- A pipeline is just a list of steps
- Order and cardinality become explicit

## Show the Move (visual beats)
**[SCREEN | Shot 3: `good_pipeline.py` — `Step` + `Pipeline.run()`]**  
**Scripted walkthrough:**  
“Here’s the new shape.  
We have one abstraction: a `Step`.  
Each step does one thing: validate, log, check fraud, charge the card.  
And the pipeline is boring on purpose — it just loops.”

**[SCREEN | Shot 4: `factory.py` building `steps = [...]`]**  
**Scripted walkthrough:**  
“And now the variation is here: in a list.  
Not in a subclass name.  
So adding a feature is adding a step — and that’s it.”

### Payoff
**[CAMERA]**  
“This is the Open‑Closed Principle in a form you can *feel*:  
open for extension — add a step — closed for modification — don’t edit the pipeline.”

**Mid‑video subscribe (natural, calm; place here ~2/3):**  
**[CAMERA]**  
“If this is the kind of senior‑level design thinking you want more of — the kind you can actually use tomorrow — subscribe.  
This series is basically ‘how to see the shape’ one episode at a time.”

**Transition to Line 4:**  
“Now here’s the part AI makes more urgent: what does this do to testability and change?”

---

# LINE 4 — “Why does this matter more with AI?”
## The Question
**[CAMERA]**  
“Why does ‘data not types’ matter even more now that AI is writing code?”

## The Trap
**[CAMERA]**  
“The naive AI prompt is: ‘Add feature X.’  
And AI will often add it as a new conditional… or a new subclass… wherever it finds room.”

### Talking points (ad‑lib)
- AI is eager, not wise
- It optimizes locally unless you constrain it
- Your design is the constraint

## The Insight
**[CAMERA]**  
“When variation is data, you give AI a safe move:  
‘Add a step. Write a test. Don’t touch the pipeline.’”

## Show the Payoff (visual beats)
**[SCREEN | Shot 5: tests for steps]**  
**Scripted walkthrough:**  
“Look how testing changes.  
Each step is independently testable.  
So instead of one monster test for every combination… you test small units and you test the assembly once.”

**[SCREEN | Shot 6: run `pytest -q` in terminal]**  
**Scripted walkthrough:**  
“And here’s the confidence: the tests pass.  
That means we can refactor the design safely while behavior stays locked in.”

### Payoff
**[CAMERA]**  
“This is agency.  
Not just for objects — for teams.  
Because now change doesn’t feel like demolition.”

**Transition to close:**  
“One last thing: once variation becomes data… a new question appears.”

---

# SINKER — 3 Options (pick 1)

### Sinker A — Intellectual Open Loop (preferred)
**[CAMERA]**  
“Now that variation is data, the next question is: **where should the decisions live**?  
If everyone assembles pipelines everywhere, you get chaos.  
So next episode we’ll talk about the real job of factories: putting identity decisions in one place — on purpose.”

### Sinker B — Next Episode (specific)
**[CAMERA]**  
“Next episode is **Where Decisions Live** — factories as the home of identity coupling.  
Watch that one next.”

### Sinker C — Playlist framing
**[CAMERA]**  
“If you want the full mental model, start the playlist from the beginning.  
Each episode adds one new shape — and together they make code changeable again.”

---

# Demo Pack (at-a-glance)

## Required shots (Trap → Shift → Payoff)
1. **Trap:** `bad_hierarchy.py` — show how combinations create new subclasses  
2. **Shift:** `factory.py` building a `Pipeline(steps=[...])` from policy  
3. **Payoff:** `pytest -q` passing + show step tests

## Your “shape” line (keep consistent)
“Let’s look at the shape of this friction.”
