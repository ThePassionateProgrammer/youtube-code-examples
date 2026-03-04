from __future__ import annotations
from dataclasses import dataclass

from ecomm.domain import Order, CustomerType


@dataclass(frozen=True)
class PricingResult:
    subtotal_cents: int
    discount_cents: int
    total_cents: int


class CheckoutProcessor:
    """TRAP VERSION: identity coupling + growing conditionals."""

    def calculate_total(self, order: Order) -> PricingResult:
        discount = 0

        # --- Identity coupling lives here ---
        if order.customer.customer_type == CustomerType.VIP:
            discount += int(order.subtotal_cents * 0.20)
        elif order.customer.customer_type == CustomerType.EMPLOYEE:
            discount += int(order.subtotal_cents * 0.30)

        if order.coupon_code == "SAVE10":
            discount += int(order.subtotal_cents * 0.10)

        if order.seasonal_promo:
            discount += 500  # $5 off

        discount = min(discount, order.subtotal_cents)
        total = order.subtotal_cents - discount
        return PricingResult(order.subtotal_cents, discount, total)
