# Episode 06: Decision Ownership

Validation chains and responsibility assignment using Chain of Responsibility pattern.

## The Problem

Validation logic often becomes a tangled mess of if/else statements. Who validates what? When does validation stop?

## Files

| File | What it shows |
|------|---------------|
| `validation_chain.py` | Chain of Responsibility for validation |
| `validation_decorator.py` | Decorator approach to validation |
| `diagram1.md` | Visual diagram of the pattern |

## Key Concept

**Chain of Responsibility**: Each handler decides whether to process the request or pass it to the next handler.

```python
chain = RequiredFieldHandler(
    EmailHandler()
)
errors = chain.handle(request)
```

Each handler owns one validation decision. The chain composes them.

## Run

```bash
python validation_chain.py
python validation_decorator.py
```
