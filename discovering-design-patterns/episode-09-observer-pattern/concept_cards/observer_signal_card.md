# Observer Pattern Signal Card

Use Observer when:

- One object changes
- Many other objects may need to react
- Polling is spreading through the system
- Timing logic is duplicated
- The publisher should not know concrete subscriber behavior

Core shift:

> Stop asking repeatedly, “Did something happen?”
>
> Let the thing that changes announce the change.

Shadow side:

> Observer reduces direct coupling, but can increase hidden control flow.
```
