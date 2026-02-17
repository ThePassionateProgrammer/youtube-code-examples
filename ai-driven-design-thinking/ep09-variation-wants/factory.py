"""
Factory = where identity coupling belongs.
It chooses which steps to assemble for a given policy/environment.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List

from good_pipeline import (
    Pipeline, Step, PaymentContext,
    ValidateAmount, FraudCheck, LogStep, ChargeStripe,
)


@dataclass(frozen=True)
class Policy:
    enable_logging: bool = True
    require_fraud_check: bool = True
    environment: str = "prod"


def build_payment_pipeline(policy: Policy) -> Pipeline:
    steps: List[Step] = []

    # <-- SHOT: variation as data — list assembly
    steps.append(ValidateAmount())

    if policy.enable_logging:
        steps.append(LogStep("before_fraud"))

    if policy.require_fraud_check:
        steps.append(FraudCheck())

    if policy.enable_logging:
        steps.append(LogStep("before_charge"))

    steps.append(ChargeStripe())

    if policy.enable_logging:
        steps.append(LogStep("after_charge"))

    return Pipeline(steps)


def run_payment(user_id: str, amount_cents: int, policy: Policy) -> PaymentContext:
    ctx = PaymentContext(
        user_id=user_id,
        amount_cents=amount_cents,
        environment=policy.environment,
    )
    pipeline = build_payment_pipeline(policy)
    return pipeline.run(ctx)
