from __future__ import annotations
from dataclasses import dataclass
from typing import List, Protocol

class Step(Protocol):
    name: str
    def run(self, ctx: "PaymentContext") -> None: ...

@dataclass
class PaymentContext:
    amount_cents: int
    card_token: str
    is_vip: bool = False
    attempts: int = 0
    logs: list[str] | None = None
    charged: bool = False
    declined_reason: str | None = None

class Pipeline:
    """Boring on purpose: sequencing + cardinality are explicit data."""
    def __init__(self, steps: List[Step]) -> None:
        self.steps = steps

    def run(self, ctx: PaymentContext) -> PaymentContext:
        for step in self.steps:
            step.run(ctx)
            if ctx.declined_reason:
                break
        return ctx
