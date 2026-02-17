from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .domain import PaymentRequest, PaymentResult


class PaymentProcessor(Protocol):
    def process(self, req: PaymentRequest) -> PaymentResult:
        ...


@dataclass
class StripeProcessor:
    """Concrete implementation. (Your narration: 'the thing that actually calls Stripe')"""
    def process(self, req: PaymentRequest) -> PaymentResult:
        # We don't hit the network. This is a deterministic demo.
        trace = [f"stripe_charge({req.amount_cents} {req.currency})"]
        return PaymentResult(ok=True, message="charged", trace=trace)


@dataclass
class ProcessorDecorator:
    """Base Decorator. Composition lives HERE: each decorator *has a* component."""
    wrapped: PaymentProcessor

    def process(self, req: PaymentRequest) -> PaymentResult:
        return self.wrapped.process(req)


@dataclass
class LoggingDecorator(ProcessorDecorator):
    def process(self, req: PaymentRequest) -> PaymentResult:
        result = self.wrapped.process(req)
        result.trace.insert(0, "log:begin")
        result.trace.append("log:end")
        return result


@dataclass
class MetricsDecorator(ProcessorDecorator):
    def process(self, req: PaymentRequest) -> PaymentResult:
        result = self.wrapped.process(req)
        result.trace.insert(0, "metrics:start")
        result.trace.append("metrics:stop")
        return result


@dataclass
class RetryDecorator(ProcessorDecorator):
    retries: int = 1

    def process(self, req: PaymentRequest) -> PaymentResult:
        # Deterministic demo: we "pretend" retry exists without randomness.
        result = self.wrapped.process(req)
        result.trace.insert(0, f"retry:up_to={self.retries}")
        return result


@dataclass(frozen=True)
class DecoratorConfig:
    env: str                 # "dev" | "prod"
    enable_logging: bool
    enable_metrics: bool
    enable_retry: bool
    user_tier: str           # "free" | "pro" | "enterprise"


class DecoratorFactory:
    """
    Key narration beat (5:33):
    'Decorator factory has nested conditions based on config/context/environment.'
    All the decisions happen HERE. Runtime is predictable once built.
    """
    @staticmethod
    def build(config: DecoratorConfig) -> PaymentProcessor:
        # Core "real thing"
        processor: PaymentProcessor = StripeProcessor()

        # --- Nested decisions (show these on screen) ---
        if config.env == "prod":
            if config.enable_metrics:
                processor = MetricsDecorator(processor)

            if config.enable_logging:
                processor = LoggingDecorator(processor)

            if config.enable_retry and config.user_tier in {"pro", "enterprise"}:
                # Another nested condition: multiple factors evaluated up front
                processor = RetryDecorator(processor, retries=2)
        else:
            # dev defaults: keep it simple, but still demonstrate conditional assembly
            if config.enable_logging:
                processor = LoggingDecorator(processor)

        return processor


def demo_decorator(config: DecoratorConfig, amount_cents: int = 1200) -> PaymentResult:
    proc = DecoratorFactory.build(config)
    req = PaymentRequest(user_id="u-123", amount_cents=amount_cents)
    return proc.process(req)