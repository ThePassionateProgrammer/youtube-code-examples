from __future__ import annotations

from dataclasses import dataclass

from .domain import CheckoutConfig, CustomerType, Destination, Order
from .policies import (
    BulkDiscount,
    DiscountPolicy,
    FreeShippingOver,
    HolidayDiscount,
    InternationalShipping,
    ShippingPolicy,
    VipDiscount,
)


@dataclass(frozen=True)
class PricingEngine:
    discount: DiscountPolicy
    shipping: ShippingPolicy

    def checkout(self, order: Order) -> int:
        discounted = self.discount.apply(order.subtotal_cents, order)
        shipping_cost = self.shipping.cost(discounted, order)
        return discounted + shipping_cost


class CheckoutFactory:
    """Where identity decisions are allowed to live.

    Rule #1: Factories may instantiate objects, but must NEVER call methods on them.
    Rule #2: The rest of the system may call methods, but must NEVER instantiate them.
    """

    @staticmethod
    def build(config: CheckoutConfig, order: Order) -> PricingEngine:
        # --- Create (instantiate) ---
        discount = CheckoutFactory._select_discount(config=config, order=order)
        shipping = CheckoutFactory._select_shipping(config=config)

        # --- Connect (wire object graph) ---
        engine = PricingEngine(discount=discount, shipping=shipping)

        # --- Return (no behavior calls here) ---
        return engine

    @staticmethod
    def _select_discount(config: CheckoutConfig, order: Order) -> DiscountPolicy:
        # Decisions are centralized here (identity coupling is contained)
        if config.customer == CustomerType.VIP and order.is_holiday:
            return VipDiscount(percent_off=20)  # VIP holiday
        if config.customer == CustomerType.VIP:
            return VipDiscount()
        if order.is_holiday:
            # 3:25 payoff: add a new discount type without touching callers
            return HolidayDiscount(percent_off=5)
        return BulkDiscount()

    @staticmethod
    def _select_shipping(config: CheckoutConfig) -> ShippingPolicy:
        if config.destination == Destination.INTERNATIONAL:
            return InternationalShipping()
        return FreeShippingOver()
