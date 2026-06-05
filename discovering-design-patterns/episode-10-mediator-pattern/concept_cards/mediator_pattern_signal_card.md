# Mediator Pattern Signal Card

Use Mediator when:

- Objects coordinate too many peers
- Relationship logic is scattered
- Changes ripple through the object graph
- Tests require too many collaborators
- The interaction has one clear context
- The relationship graph is more complex than the objects

Core insight:

> Mediator does not eliminate complexity.  
> It relocates coordination so objects can stay focused.

Shadow side:

> A Mediator can become a God object if it coordinates too many unrelated conversations.
