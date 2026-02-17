from __future__ import annotations

from typing import List

from shared.order import Order
from clever_checkout.checkout import (
    CheckoutProcessor,
    BasePriceStrategy,
    VipDiscountStrategy,
    PricingStrategy,
    TotalDecorator,
    ShippingFeeDecorator,
    AuditLogDecorator,
    PaymentValidHandler,
    AlwaysPassHandler,
)

class CheckoutFactory:
    """
    The 'decision zone' in the clever design.
    It *looks* like we're doing emergent design…
    but we're just encoding 3 fixed rules across 4 abstractions.
    """

    def build(self, *, env: str, enable_audit: bool) -> CheckoutProcessor:
        pricing: PricingStrategy = BasePriceStrategy()
        pricing = VipDiscountStrategy(pricing, vip_discount_rate=0.10)

        decorators: List[TotalDecorator] = []

        # Nested conditions (impressive, but mostly unnecessary for this episode)
        if env in ("prod", "staging"):
            if enable_audit:
                decorators.append(AuditLogDecorator())

        # Still we need shipping
        decorators.append(ShippingFeeDecorator(fee=10.0))

        # Validation chain
        chain = PaymentValidHandler()
        chain.set_next(AlwaysPassHandler())

        return CheckoutProcessor(pricing=pricing, decorators=decorators, validation_chain=chain)

def checkout_total(order: Order, *, env: str = "prod", enable_audit: bool = True) -> float:
    """Convenience function used by tests (keeps call-site stable)."""
    processor = CheckoutFactory().build(env=env, enable_audit=enable_audit)
    return processor.checkout_total(order)
