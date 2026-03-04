# AI-Driven Design Thinking

Code examples exploring design patterns and software architecture through AI-assisted development.

## Episodes

| Episode | Topic | Description |
|---------|-------|-------------|
| [ep02](ep02-dependency-injection/) | Dependency Injection | Breaking tight coupling by injecting dependencies instead of creating them internally |
| [ep03](ep03-factories/) | Factories | Using factory patterns to manage object creation and reduce strategy proliferation |
| [ep04](ep04-decorator/) | Decorator Pattern | Composing behavior dynamically without class explosion |
| [ep05](ep05-one-question/) | One Question | Focused design decisions through constraint |
| [ep06](ep06-decorator-vs-cor/) | Decorator vs Chain of Responsibility | Comparing two structural patterns: when to compose behavior vs. delegate decisions |
| [ep07](ep07-you-must-judge/) | You Must Judge | AI can generate code, but only you can evaluate its design — three versions of the same capability compared |
| [ep08](ep08-law-of-demeter/) | Law of Demeter | How reaching through objects creates fragile coupling — and how a pipeline fixes it |
| [ep09](ep09-variation-wants/) | Variation Wants to Be Data | Why class explosion happens and how to replace subclass hierarchies with data-driven pipelines |
| [ep10](ep10-factories/) | Where Should Decisions Live? | Moving identity decisions out of usage sites and into factories |
| [ep11](ep11-testability-smell-detector/) | Testability as a Smell Detector | Using test difficulty as a signal for low cohesion — before/after refactor with atomic unit tests |
| [ep12](ep12-patterns-not-solutions/) | Patterns Are Not Solutions | Three implementations of the same behavior (Conditional → Strategy → Template Method) showing design consequence |
| [ep13](ep13-emergent-design/) | Emergent Design | How design evolves step by step through TDD — patterns emerge from pressure, not prescription |

## Running the Examples

Most episodes (ep06 onward) include a venv setup and pytest tests:

```bash
cd ep11-testability-smell-detector
python -m venv .venv
source .venv/bin/activate
pip install -U pytest
pytest -q
```

Earlier episodes (ep02–ep05) are self-contained Python files with no external dependencies:

```bash
cd ep02-dependency-injection
python 01_bad_no_seam.py
```

Files are numbered to show progression — start with `01_` and work through in order.

## Learning Path

These episodes build on each other:

1. **Dependency Injection** — The foundation: separating creation from use
2. **Factories** — Managing complexity when you have many strategies
3. **Decorator** — Adding behavior without modifying existing classes
4. **One Question** — Simplifying design decisions
5. **Decorator vs Chain of Responsibility** — Two patterns, same problem space — how forces decide
6. **You Must Judge** — AI generates; you evaluate — three versions of the same design
7. **Law of Demeter** — Stop reaching through objects
8. **Variation Wants to Be Data** — Replace type hierarchies with data pipelines
9. **Where Should Decisions Live?** — Factories as the home for identity coupling
10. **Testability as a Smell Detector** — Hard-to-test code is telling you something
11. **Patterns Are Not Solutions** — Green bar ≠ good design; forces shape structure
12. **Emergent Design** — Design as evolution, not prescription
