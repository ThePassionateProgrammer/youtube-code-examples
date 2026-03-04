from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .pipeline import Pipeline, PaymentContext, Step
from .steps import ValidateAmountStep, FraudCheckStep, RetryStep, LogStep, ChargeCardStep

@dataclass(frozen=True)
class PaymentConfig:
    enable_logging: bool = True
    enable_fraud_check: bool = True
    enable_retry: bool = False

def build_payment_pipeline(config: PaymentConfig) -> Pipeline:
    """Variation is HERE (data), not encoded into subclass names."""
    steps: List[Step] = [ValidateAmountStep()]

    if config.enable_logging:
        steps.append(LogStep("log: start"))

    if config.enable_fraud_check:
        steps.append(FraudCheckStep())

    if config.enable_retry:
        steps.append(RetryStep(max_attempts=2))

    steps.append(ChargeCardStep())

    if config.enable_logging:
        steps.append(LogStep("log: end"))

    return Pipeline(steps)

def run_payment(amount_cents: int, *, is_vip: bool, config: PaymentConfig) -> PaymentContext:
    ctx = PaymentContext(amount_cents=amount_cents, card_token="tok_123", is_vip=is_vip)
    return build_payment_pipeline(config).run(ctx)
