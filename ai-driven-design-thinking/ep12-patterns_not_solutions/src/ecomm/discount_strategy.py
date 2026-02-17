from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol

from ecomm.domain import Order, CustomerType


class DiscountPolicy(Protocol):
    def discount_cents(self, order: Order) -> int:
        ...


@dataclass(frozen=True)
class NoDiscount:
    def discount_cents(self, order: Order) -> int:
        return 0


@dataclass(frozen=True)
class VipDiscount:
    def discount_cents(self, order: Order) -> int:
        if order.customer.customer_type == CustomerType.VIP:
            return int(order.subtotal_cents * 0.20)
        return 0


@dataclass(frozen=True)
class EmployeeDiscount:
    def discount_cents(self, order: Order) -> int:
        if order.customer.customer_type == CustomerType.EMPLOYEE:
            return int(order.subtotal_cents * 0.30)
        return 0


@dataclass(frozen=True)
class Coupon10Discount:
    def discount_cents(self, order: Order) -> int:
        if order.coupon_code == "SAVE10":
            return int(order.subtotal_cents * 0.10)
        return 0


@dataclass(frozen=True)
class SeasonalPromoDiscount:
    def discount_cents(self, order: Order) -> int:
        return 500 if order.seasonal_promo else 0


@dataclass(frozen=True)
class CombinedDiscount:
    policies: tuple[DiscountPolicy, ...]

    def discount_cents(self, order: Order) -> int:
        return sum(p.discount_cents(order) for p in self.policies)
