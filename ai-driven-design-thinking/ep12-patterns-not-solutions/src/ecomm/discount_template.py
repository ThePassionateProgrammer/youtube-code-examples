from __future__ import annotations
from dataclasses import dataclass

from ecomm.domain import Order


@dataclass(frozen=True)
class DiscountTemplate:
    """TEMPLATE METHOD: stable skeleton; variation inside steps."""

    def discount_cents(self, order: Order) -> int:
        if not self.eligible(order):
            return 0
        return self.compute_discount(order)

    def eligible(self, order: Order) -> bool:
        raise NotImplementedError

    def compute_discount(self, order: Order) -> int:
        raise NotImplementedError


@dataclass(frozen=True)
class VipTemplateDiscount(DiscountTemplate):
    def eligible(self, order: Order) -> bool:
        return order.customer.customer_type.name == "VIP"

    def compute_discount(self, order: Order) -> int:
        return int(order.subtotal_cents * 0.20)


@dataclass(frozen=True)
class EmployeeTemplateDiscount(DiscountTemplate):
    def eligible(self, order: Order) -> bool:
        return order.customer.customer_type.name == "EMPLOYEE"

    def compute_discount(self, order: Order) -> int:
        return int(order.subtotal_cents * 0.30)


@dataclass(frozen=True)
class Coupon10TemplateDiscount(DiscountTemplate):
    def eligible(self, order: Order) -> bool:
        return order.coupon_code == "SAVE10"

    def compute_discount(self, order: Order) -> int:
        return int(order.subtotal_cents * 0.10)


@dataclass(frozen=True)
class SeasonalPromoTemplateDiscount(DiscountTemplate):
    def eligible(self, order: Order) -> bool:
        return bool(order.seasonal_promo)

    def compute_discount(self, order: Order) -> int:
        return 500
