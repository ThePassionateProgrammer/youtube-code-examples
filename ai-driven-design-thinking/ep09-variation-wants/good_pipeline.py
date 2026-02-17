"""
GOOD SHAPE (Shift)
Variation is data (a list of steps), not identity (a subclass name).
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Protocol, List


@dataclass
class PaymentContext:
    user_id: str
    amount_cents: int
    currency: str = "USD"
    environment: str = "prod"
    events: List[str] = field(default_factory=list)
    approved: bool = True
    charged: bool = False


class Step(Protocol):
    def process(self, ctx: PaymentContext) -> None: ...


class ValidateAmount:
    def process(self, ctx: PaymentContext) -> None:
        if ctx.amount_cents <= 0:
            ctx.approved = False
            ctx.events.append("rejected:invalid_amount")
        else:
            ctx.events.append("ok:amount")


class FraudCheck:
    def process(self, ctx: PaymentContext) -> None:
        if ctx.amount_cents > 50_000 and ctx.environment == "prod":
            ctx.approved = False
            ctx.events.append("rejected:fraud")
        else:
            ctx.events.append("ok:fraud")


class LogStep:
    def __init__(self, label: str) -> None:
        self._label = label

    def process(self, ctx: PaymentContext) -> None:
        ctx.events.append(f"log:{self._label}")


class ChargeStripe:
    def process(self, ctx: PaymentContext) -> None:
        if not ctx.approved:
            ctx.events.append("skip:charge")
            return
        ctx.charged = True
        ctx.events.append("charged:stripe")


class Pipeline:
    def __init__(self, steps: List[Step]) -> None:
        self._steps = steps

    def run(self, ctx: PaymentContext) -> PaymentContext:
        # <-- SHOT: pipeline is boring on purpose
        for step in self._steps:
            step.process(ctx)
            if not ctx.approved:
                ctx.events.append("bail:not_approved")
                break
        return ctx
