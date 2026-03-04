from __future__ import annotations

from dataclasses import dataclass
from .pipeline import PaymentContext

@dataclass(frozen=True)
class ValidateAmountStep:
    name: str = "validate_amount"
    def run(self, ctx: PaymentContext) -> None:
        if ctx.amount_cents <= 0:
            ctx.declined_reason = "INVALID_AMOUNT"

@dataclass(frozen=True)
class FraudCheckStep:
    name: str = "fraud_check"
    def run(self, ctx: PaymentContext) -> None:
        if ctx.is_vip:
            return
        if ctx.amount_cents > 50_00:
            ctx.declined_reason = "FRAUD_SUSPECTED"

@dataclass(frozen=True)
class RetryStep:
    max_attempts: int = 2
    name: str = "retry"
    def run(self, ctx: PaymentContext) -> None:
        ctx.attempts += 1
        if ctx.attempts > self.max_attempts:
            ctx.declined_reason = "TOO_MANY_ATTEMPTS"

@dataclass(frozen=True)
class LogStep:
    message: str
    name: str = "log"
    def run(self, ctx: PaymentContext) -> None:
        ctx.logs = (ctx.logs or [])
        ctx.logs.append(self.message)

@dataclass(frozen=True)
class ChargeCardStep:
    name: str = "charge_card"
    def run(self, ctx: PaymentContext) -> None:
        if ctx.declined_reason:
            return
        ctx.charged = True
