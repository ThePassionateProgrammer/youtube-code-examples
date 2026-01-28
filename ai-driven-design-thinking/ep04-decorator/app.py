"""
EP4 — Decorator (real example app, screenshot-ready)

Goal:
- Show WHY inheritance explodes (specialization)
- Show Strategy relocates conditionals into a factory (selection vs action)
- Show Decorator as a pipeline: vary sequence + cardinality + optional steps
- Show PipelineFactory as the cohesive decision point

This file is labeled with [SHOT-x] markers so you can scroll + screenshot fast.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol, List


# ============================================================
# Domain
# ============================================================

@dataclass
class PaymentRequest:
    amount: float
    processor: str   # "stripe" | "acmepay"
    mode: str        # "basic" | "secure" | "observed"


@dataclass
class PaymentResult:
    approved: bool
    message: str
    log: List[str]


# ============================================================
# [SHOT-1] Inheritance-as-Specialization (class explosion seed)
# ============================================================

class BasePaymentService:
    def pay(self, req: PaymentRequest) -> PaymentResult:
        raise NotImplementedError


class StripeService(BasePaymentService):
    def pay(self, req: PaymentRequest) -> PaymentResult:
        return PaymentResult(True, f"Stripe charged {req.amount}", log=["CHARGE:stripe"])


# Optional behaviors become subclasses… then combinations become MORE subclasses.
class StripeWithLogging(StripeService):
    def pay(self, req: PaymentRequest) -> PaymentResult:
        r = super().pay(req)
        r.log.append("LOG: paid")
        return r


class StripeWithFraudCheck(StripeService):
    def pay(self, req: PaymentRequest) -> PaymentResult:
        if req.amount > 10_000:
            return PaymentResult(False, "Declined (fraud)", log=["FRAUD:declined"])
        r = super().pay(req)
        r.log.append("FRAUD: ok")
        return r


class StripeWithLoggingAndFraudCheck(StripeService):
    def pay(self, req: PaymentRequest) -> PaymentResult:
        # Combining behaviors pushes you toward new subclasses.
        if req.amount > 10_000:
            return PaymentResult(False, "Declined (fraud)", log=["FRAUD:declined"])
        r = super().pay(req)
        r.log.append("FRAUD: ok")
        r.log.append("LOG: paid")
        return r


# ============================================================
# Strategy + Factory
# Strategy does NOT remove conditionals. It relocates them into a cohesive factory.
# Selection (factory) is separated from action (service/client).
# ============================================================

class PaymentClient(Protocol):
    def charge(self, amount: float) -> str: ...


class StripeClient:
    def charge(self, amount: float) -> str:
        return f"Stripe API: charged {amount}"


class AcmePayClient:
    def charge(self, amount: float) -> str:
        return f"AcmePay API: charged {amount}"


# ============================================================
# [SHOT-2] Strategy selection lives here (conditionals belong here)
# ============================================================

class PaymentClientFactory:
    @staticmethod
    def create(processor: str) -> PaymentClient:
        if processor == "stripe":
            return StripeClient()
        if processor == "acmepay":
            return AcmePayClient()
        raise ValueError(f"Unknown processor: {processor}")


# ============================================================
# [SHOT-3] Action lives here (no selection conditionals)
# ============================================================

class StrategyBasedPaymentService:
    def __init__(self, client: PaymentClient) -> None:
        self._client = client

    def pay(self, req: PaymentRequest) -> PaymentResult:
        msg = self._client.charge(req.amount)
        return PaymentResult(True, msg, log=["SERVICE:strategy"])


# ============================================================
# Decorator-as-Pipeline (sequence + cardinality + optional steps)
# ============================================================

@dataclass
class PaymentContext:
    req: PaymentRequest
    result: PaymentResult


# ============================================================
# [SHOT-4] The polymorphic seam (all steps share this)
# ============================================================

class Step(Protocol):
    def process(self, ctx: PaymentContext) -> None: ...


# ============================================================
# [SHOT-5] Concrete steps (small, composable responsibilities)
# ============================================================

class ValidateStep:
    def process(self, ctx: PaymentContext) -> None:
        if ctx.req.amount <= 0:
            ctx.result.approved = False
            ctx.result.message = "Invalid amount"
        ctx.result.log.append("STEP:validate")


class FraudCheckStep:
    def process(self, ctx: PaymentContext) -> None:
        if ctx.req.amount > 10_000:
            ctx.result.approved = False
            ctx.result.message = "Declined (fraud)"
        ctx.result.log.append("STEP:fraud_check")


class EncryptAuditStep:
    def process(self, ctx: PaymentContext) -> None:
        ctx.result.log.append("STEP:encrypt_audit")


class LogStep:
    def process(self, ctx: PaymentContext) -> None:
        ctx.result.log.append(f"STEP:log({ctx.req.processor},{ctx.req.mode})")


class ChargeStep:
    # Strategy is hidden inside the step.
    def __init__(self, client: PaymentClient) -> None:
        self._client = client

    def process(self, ctx: PaymentContext) -> None:
        if not ctx.result.approved:
            ctx.result.log.append("STEP:charge(skipped)")
            return
        ctx.result.message = self._client.charge(ctx.req.amount)
        ctx.result.log.append("STEP:charge(executed)")


# ============================================================
# [SHOT-6] The boring core (the power is that it stays boring)
# ============================================================

class PaymentPipeline:
    def __init__(self, steps: List[Step]) -> None:
        self._steps = steps

    def run(self, req: PaymentRequest) -> PaymentResult:
        result = PaymentResult(True, "pending", log=[])
        ctx = PaymentContext(req=req, result=result)

        for step in self._steps:
            step.process(ctx)

        return ctx.result


# ============================================================
# [SHOT-7] Policy + constraints live here (factories decide; clients act)
# ============================================================

class PipelineFactory:
    @staticmethod
    def create(req: PaymentRequest) -> PaymentPipeline:
        client = PaymentClientFactory.create(req.processor)

        steps: List[Step] = [ValidateStep()]

        # Conditionals belong here: selection, ordering, cardinality.
        if req.mode == "secure":
            steps += [FraudCheckStep(), EncryptAuditStep()]
        elif req.mode == "observed":
            steps += [LogStep()]

        steps.append(ChargeStep(client))

        if req.mode in ("secure", "observed"):
            steps.append(LogStep())

        return PaymentPipeline(steps)


# ============================================================
# [SHOT-8] Real call site (looks like a real program)
# ============================================================

def main() -> None:
    req = PaymentRequest(amount=200.0, processor="acmepay", mode="secure")
    pipeline = PipelineFactory.create(req)
    result = pipeline.run(req)
    print(result.approved, result.message, result.log)


if __name__ == "__main__":
    main()