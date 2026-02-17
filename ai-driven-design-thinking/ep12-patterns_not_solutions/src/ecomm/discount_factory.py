from __future__ import annotations
from dataclasses import dataclass

from ecomm.domain import Order, CustomerType
from ecomm.discount_strategy import (
    DiscountPolicy,
    NoDiscount,
    VipDiscount,
    EmployeeDiscount,
    Coupon10Discount,
    SeasonalPromoDiscount,
    CombinedDiscount,
)


@dataclass(frozen=True)
class DiscountConfig:
    enable_employee_discount: bool = True
    enable_vip_discount: bool = True
    enable_coupons: bool = True
    enable_seasonal_promo: bool = True


class DiscountFactory:
    """Identity coupling is allowed to live here."""

    def __init__(self, config: DiscountConfig):
        self._config = config

    def build_policy(self, order: Order) -> DiscountPolicy:
        policies: list[DiscountPolicy] = []

        if self._config.enable_vip_discount and order.customer.customer_type == CustomerType.VIP:
            policies.append(VipDiscount())

        if self._config.enable_employee_discount and order.customer.customer_type == CustomerType.EMPLOYEE:
            policies.append(EmployeeDiscount())

        if self._config.enable_coupons and order.coupon_code:
            policies.append(Coupon10Discount())

        if self._config.enable_seasonal_promo:
            policies.append(SeasonalPromoDiscount())

        if not policies:
            return NoDiscount()

        if len(policies) == 1:
            return policies[0]

        return CombinedDiscount(tuple(policies))
