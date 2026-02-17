from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .models import Customer


class ShippingCalculator(Protocol):
    def shipping_for(self, discounted_subtotal: float, customer: Customer) -> float:
        ...


@dataclass(frozen=True)
class ThresholdShipping:
    base_shipping: float = 7.99
    free_threshold: float = 100.0

    def shipping_for(self, discounted_subtotal: float, customer: Customer) -> float:
        if discounted_subtotal >= self.free_threshold:
            return 0.0
        return self.base_shipping


@dataclass(frozen=True)
class VipFreeShipping:
    enabled: bool = True

    def shipping_for(self, discounted_subtotal: float, customer: Customer) -> float:
        if self.enabled and customer.vip:
            return 0.0
        return float("nan")  # sentinel: "no decision"
