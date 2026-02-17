"""
BAD SHAPE (Trap)
Variation encoded in identity (types) creates class explosion.
"""

from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class PaymentRequest:
    user_id: str
    amount_cents: int
    currency: str = "USD"
    environment: str = "prod"  # "prod" | "staging"
    require_fraud_check: bool = True
    enable_logging: bool = True
    retries: int = 0


class PaymentProcessor:
    """Base role: process a payment request."""
    def process(self, req: PaymentRequest) -> str:
        raise NotImplementedError


class StripeProcessor(PaymentProcessor):
    def process(self, req: PaymentRequest) -> str:
        return f"charged:{req.amount_cents}:{req.currency}:stripe"


# --- Optional behaviors (the "features") ---

class StripeWithLogging(StripeProcessor):
    def process(self, req: PaymentRequest) -> str:
        # log(req)  # pretend
        return super().process(req)


class StripeWithFraudCheck(StripeProcessor):
    def process(self, req: PaymentRequest) -> str:
        # fraud_check(req)  # pretend
        return super().process(req)


class StripeWithRetries(StripeProcessor):
    def process(self, req: PaymentRequest) -> str:
        last = None
        for _ in range(max(1, req.retries + 1)):
            last = super().process(req)
        return last or super().process(req)


# --- Combinations arrive (2^n) ---

class StripeWithLoggingAndFraud(StripeProcessor):
    def process(self, req: PaymentRequest) -> str:
        # log(req)
        # fraud_check(req)
        return super().process(req)


class StripeWithLoggingAndRetries(StripeWithRetries):
    def process(self, req: PaymentRequest) -> str:
        # log(req)
        return super().process(req)


class StripeWithFraudAndRetries(StripeWithRetries):
    def process(self, req: PaymentRequest) -> str:
        # fraud_check(req)
        return super().process(req)


class StripeWithLoggingFraudAndRetries(StripeWithRetries):
    def process(self, req: PaymentRequest) -> str:
        # log(req)
        # fraud_check(req)
        return super().process(req)


# <-- SHOT: this is your “2^n” moment
#
# Each new optional behavior doubles combinations:
# n=1 → 2
# n=2 → 4
# n=3 → 8
# n=4 → 16
# n=5 → 32
#


def pick_processor_bad(req: PaymentRequest) -> PaymentProcessor:
    """
    Even if you try to centralize selection,
    you end up selecting among a growing set of *types*.
    """
    # <-- SHOT: identity decisions keep growing here
    if req.enable_logging and req.require_fraud_check and req.retries > 0:
        return StripeWithLoggingFraudAndRetries()
    if req.enable_logging and req.require_fraud_check:
        return StripeWithLoggingAndFraud()
    if req.enable_logging and req.retries > 0:
        return StripeWithLoggingAndRetries()
    if req.require_fraud_check and req.retries > 0:
        return StripeWithFraudAndRetries()
    if req.enable_logging:
        return StripeWithLogging()
    if req.require_fraud_check:
        return StripeWithFraudCheck()
    if req.retries > 0:
        return StripeWithRetries()
    return StripeProcessor()
