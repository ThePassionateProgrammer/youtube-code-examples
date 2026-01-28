# AI-Driven Design Thinking

Code examples exploring design patterns and software architecture through AI-assisted development.

## Episodes

| Episode | Topic | Description |
|---------|-------|-------------|
| [ep02](ep02-dependency-injection/) | Dependency Injection | Breaking tight coupling by injecting dependencies instead of creating them internally |
| [ep03](ep03-factories/) | Factories | Using factory patterns to manage object creation and reduce strategy proliferation |
| [ep04](ep04-decorator/) | Decorator Pattern | Composing behavior dynamically without class explosion |
| [ep05](ep05-one-question/) | One Question | Focused design decisions through constraint |
| [ep06](ep06-decision-ownership/) | Decision Ownership | Validation chains and responsibility assignment |

## Running the Examples

All examples are self-contained Python files with no external dependencies.

```bash
cd ep02-dependency-injection
python 01_bad_no_seam.py
```

Files are numbered to show progression—start with `01_` and work through in order.

## Learning Path

These episodes build on each other:

1. **Dependency Injection** — The foundation: separating creation from use
2. **Factories** — Managing complexity when you have many strategies
3. **Decorator** — Adding behavior without modifying existing classes
4. **One Question** — Simplifying design decisions
5. **Decision Ownership** — Who validates what and when?
