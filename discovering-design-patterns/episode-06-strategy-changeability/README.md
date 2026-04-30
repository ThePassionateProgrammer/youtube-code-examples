# Video 6 Production Package — Variation Across Patterns

## Episode
- Focus: Strategy, Template Method, Proxy, Bridge, and testability
- Domain: Meeting scheduling

## Demo intent
Show that these patterns all deal with variation, but not the same kind of variation:
- Strategy varies the whole behavior.
- Template Method varies steps inside a stable algorithm.
- Proxy varies interaction, sequence, access, or cardinality.
- Bridge handles independent dimensions of variation.
- Strategy testability separates structure, behavior, and factory selection.

## Run in VS Code
```bash
pytest -q
```

## Files
- `strategy_example.py`
- `template_method_example.py`
- `proxy_example.py`
- `bridge_example.py`
- `factory_and_tests_example.py`
- `test_video6_patterns.py`
- `UML_patterns.md`
- `shot_list.md`
- `test_output.txt`
