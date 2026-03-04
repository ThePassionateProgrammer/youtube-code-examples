from __future__ import annotations

from dataclasses import dataclass
from abc import ABC, abstractmethod

from .domain import Order


class DiscountPolicy(ABC):
    @abstractmethod
    def apply(self, subtotal_cents: int, order: Order) -> int:
        """Return discounted subtotal (in cents)."""


class NoDiscount(DiscountPolicy):
    def apply(self, subtotal_cents: int, order: Order) -> int:
        return subtotal_cents


@dataclass(frozen=True)
class BulkDiscount(DiscountPolicy):
    threshold_cents: int = 10_000  # $100
    percent_off: int = 10          # 10%

    def apply(self, subtotal_cents: int, order: Order) -> int:
        if subtotal_cents < self.threshold_cents:
            return subtotal_cents
        return int(subtotal_cents * (100 - self.percent_off) / 100)


@dataclass(frozen=True)
class VipDiscount(DiscountPolicy):
    percent_off: int = 15

    def apply(self, subtotal_cents: int, order: Order) -> int:
        return int(subtotal_cents * (100 - self.percent_off) / 100)


@dataclass(frozen=True)
class HolidayDiscount(DiscountPolicy):
    percent_off: int = 5

    def apply(self, subtotal_cents: int, order: Order) -> int:
        if not order.is_holiday:
            return subtotal_cents
        return int(subtotal_cents * (100 - self.percent_off) / 100)


class ShippingPolicy(ABC):
    @abstractmethod
    def cost(self, discounted_subtotal_cents: int, order: Order) -> int:
        """Return shipping cost (in cents)."""


@dataclass(frozen=True)
class FlatRateShipping(ShippingPolicy):
    cents: int = 799  # $7.99

    def cost(self, discounted_subtotal_cents: int, order: Order) -> int:
        return self.cents


@dataclass(frozen=True)
class FreeShippingOver(ShippingPolicy):
    threshold_cents: int = 10_000  # $100

    def cost(self, discounted_subtotal_cents: int, order: Order) -> int:
        return 0 if discounted_subtotal_cents >= self.threshold_cents else 799


@dataclass(frozen=True)
class InternationalShipping(ShippingPolicy):
    cents: int = 1999  # $19.99

    def cost(self, discounted_subtotal_cents: int, order: Order) -> int:
        return self.cents
