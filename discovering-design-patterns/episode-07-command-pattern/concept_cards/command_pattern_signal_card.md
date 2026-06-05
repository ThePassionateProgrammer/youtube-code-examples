# Command Pattern Signal Card

## Friction
The system can execute behavior, but it cannot represent behavior.

## Signal
You need to queue, log, replay, inspect, validate, schedule, undo, or test actions independently of the caller.

## Abstraction Test
- What is varying? The action itself.
- What stays stable? The caller/invoker asks for execution.
- Where should the decision live? At the boundary where intent is selected.
- What abstraction is missing? A command object that gives behavior identity.

## Anchor Lines
- The function map solved dispatch, but it didn’t model intent.
- Procedural systems execute behavior. Object-oriented systems can model behavior.
- Behavior is no longer transient. Behavior becomes an artifact.
- Patterns are testable by design.
