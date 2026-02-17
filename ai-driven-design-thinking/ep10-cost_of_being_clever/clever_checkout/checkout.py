from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, List

from shared.order import Order

# -------- Strategy (pricing) --------

class PricingStrategy(Protocol):
    def price(self, order: Order) -> float: ...

class BasePriceStrategy:
    def price(self, order: Order) -> float:
        return order.base_price

class VipDiscountStrategy:
    """A strategy variant that applies the VIP discount."""
    def __init__(self, base: PricingStrategy, vip_discount_rate: float = 0.10) -> None:
        self._base = base
        self._vip_discount_rate = vip_discount_rate

    def price(self, order: Order) -> float:
        total = self._base.price(order)
        if order.is_vip:
            total = total * (1.0 - self._vip_discount_rate)
        return total


# -------- Decorator-ish "steps" (optional responsibilities) --------

class TotalDecorator(Protocol):
    def apply(self, order: Order, running_total: float) -> float: ...

class ShippingFeeDecorator:
    def __init__(self, fee: float = 10.0) -> None:
        self._fee = fee

    def apply(self, order: Order, running_total: float) -> float:
        if order.region != "local":
            return running_total + self._fee
        return running_total

class AuditLogDecorator:
    """Looks enterprise. Adds no business value for this episode."""
    def apply(self, order: Order, running_total: float) -> float:
        # Imagine logging, metrics, tracing... (omitted)
        return running_total


# -------- Chain of Responsibility (validation) --------

class ValidationHandler(Protocol):
    def set_next(self, nxt: "ValidationHandler") -> "ValidationHandler": ...
    def handle(self, order: Order) -> None: ...

@dataclass
class _BaseValidationHandler:
    _next: "ValidationHandler | None" = None

    def set_next(self, nxt: "ValidationHandler") -> "ValidationHandler":
        self._next = nxt
        return nxt

    def handle(self, order: Order) -> None:
        if self._next is not None:
            self._next.handle(order)

class PaymentValidHandler(_BaseValidationHandler):
    def handle(self, order: Order) -> None:
        if not order.payment_valid:
            raise ValueError("Invalid payment")
        super().handle(order)

class AlwaysPassHandler(_BaseValidationHandler):
    """Looks like an extension point. Does nothing."""
    def handle(self, order: Order) -> None:
        super().handle(order)


# -------- The "impressive" processor --------

class CheckoutProcessor:
    """
    A composition root would build this.
    It looks like a flexible architecture... for 3 fixed rules.
    """
    def __init__(
        self,
        pricing: PricingStrategy,
        decorators: List[TotalDecorator],
        validation_chain: ValidationHandler,
    ) -> None:
        self._pricing = pricing
        self._decorators = decorators
        self._validation_chain = validation_chain

    def checkout_total(self, order: Order) -> float:
        # validate first
        self._validation_chain.handle(order)

        # price
        total = self._pricing.price(order)

        # apply optional responsibilities
        for d in self._decorators:
            total = d.apply(order, total)

        return total
