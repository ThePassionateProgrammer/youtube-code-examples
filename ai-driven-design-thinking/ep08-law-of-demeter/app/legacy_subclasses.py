from __future__ import annotations
from dataclasses import dataclass

@dataclass
class PaymentContext:
    amount_cents: int
    card_token: str
    is_vip: bool = False
    attempts: int = 0
    log: list[str] | None = None

class BasePaymentFlow:
    def process(self, ctx: PaymentContext) -> str:
        return f"CHARGED:{ctx.amount_cents}"

class PaymentFlowWithLogging(BasePaymentFlow):
    def process(self, ctx: PaymentContext) -> str:
        ctx.log = (ctx.log or [])
        ctx.log.append("log: start")
        result = super().process(ctx)
        ctx.log.append("log: end")
        return result

class PaymentFlowWithFraudCheck(BasePaymentFlow):
    def process(self, ctx: PaymentContext) -> str:
        if ctx.amount_cents > 50_00 and not ctx.is_vip:
            return "DECLINED:FRAUD"
        return super().process(ctx)

class PaymentFlowWithRetry(BasePaymentFlow):
    def process(self, ctx: PaymentContext) -> str:
        ctx.attempts += 1
        if ctx.attempts == 1:
            return "RETRY"
        return super().process(ctx)

# Now imagine combinations: PaymentFlowWithLoggingAndFraudAndRetry ... (2^n)
