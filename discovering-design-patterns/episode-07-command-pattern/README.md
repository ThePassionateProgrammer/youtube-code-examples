# Episode 07 — Command Pattern Production Package

## Episode
- **Title:** Why Treating Actions as Objects Changes EVERYTHING
- **Runtime target:** 8–10 minutes
- **Domain:** document actions / catalog system
- **Pattern focus:** Command Pattern; comparison with Proxy, Adapter, Decorator, and Mocks

## Demo intent
Show how a function map solves dispatch but strips away identity. Then show how Command turns behavior into a representable artifact that can be queued, logged, replayed, inspected, validated, undone, and tested.

## Run in VS Code
```bash
cd episode_07_command_pattern
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
pytest
python src/before_example.py
python src/after_example.py
```

## Files
```text
episode_07_command_pattern/
  src/
    before_example.py
    after_example.py
  tests/
    test_command_pattern.py
  uml/
    command_pattern.svg
    proxy_pattern.svg
    adapter_pattern.svg
    decorator_pattern.svg
    mock_object.svg
    uml_diagrams.md
  concept_cards/
    command_pattern_signal_card.md
  shot_list.md
  README.md
  requirements.txt
  pytest.ini
```

## Tests included
- Behavior test: command executes the receiver.
- Structure test: queue can execute commands and log results.
- Selection test: factory creates the command that represents user intent.
- Boundary test: invalid action rejected at selection boundary.
