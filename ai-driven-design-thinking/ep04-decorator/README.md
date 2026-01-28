# Episode 04: Decorator Pattern

Composing behavior dynamically without class explosion.

## The Problem

When you need combinations of behaviors (logging + validation, encryption + logging, etc.), creating a class for each combination leads to exponential growth.

## Files

| File | What it shows |
|------|---------------|
| `01_class_explosion.py` | The problem: combinatorial class explosion |
| `02_strategy_only.py` | Strategy approach (still limited) |
| `03_decorator_steps.py` | Decorator steps that can be composed |
| `04_pipeline.py` | Composing decorators into a pipeline |
| `05_pipeline_factory.py` | Factory for creating decorated pipelines |
| `app.py` | Full application demonstrating the pattern |

## Key Concept

**Decorator**: Wraps an object to add behavior without modifying the original class.

Decorators can be stacked: `Logged(Validated(Encrypted(processor)))` — each layer adds its behavior.

## Run

```bash
python app.py
```
