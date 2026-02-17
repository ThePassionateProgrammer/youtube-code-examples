from __future__ import annotations
from dataclasses import dataclass

from ecomm.domain import Order
from ecomm.discount_template import DiscountTemplate


@dataclass(frozen=True)
class PricingResult:
    subtotal_cents: int
    discount_cents: int
    total_cents: int


class CheckoutProcessor:
    def __init__(self, template: DiscountTemplate):
        self._template = template

    def calculate_total(self, order: Order) -> PricingResult:
        discount = self._template.discount_cents(order)
        discount = min(discount, order.subtotal_cents)
        total = order.subtotal_cents - discount
        return PricingResult(order.subtotal_cents, discount, total)
