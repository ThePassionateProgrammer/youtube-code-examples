# Episode 10 — Mediator Pattern Production Package

## Video
**Why Your Code Feels Like a Mess — and How to Fix It**  
Pattern focus: Mediator Pattern

## Demo intent
Show how object-to-object coordination becomes scattered, then introduce a Mediator as a collaboration boundary.

## Run the tests

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Files
```text
episode_10_mediator_pattern/
  src/
    before_example.py
    after_example.py
    adapter_example.py
    facade_example.py
    state_example.py
  tests/
    test_mediator_pattern.py
  uml/
    mediator_canonical_uml.png
    checkout_mediator_uml.png
    adapter_uml.png
    facade_uml.png
    state_uml.png
    mediator_vs_patterns.png
    relationship_graph_before.png
    relationship_graph_after.png
  concept_cards/
    mediator_pattern_signal_card.md
  shot_list.md
  README.md
```

## Production notes
Use the `before_example.py` for the opening “relationship graph” pain.  
Use `after_example.py` for the structural move, mediator, side-by-side, and tests.  
Use the PNG UML files when comparing Mediator with Adapter, Facade, and State.
