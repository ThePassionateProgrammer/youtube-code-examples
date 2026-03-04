from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .models import Cart, Customer


class DiscountPolicy(Protocol):
    def discount_for(self, cart: Cart, customer: Customer) -> float:
        ...


@dataclass(frozen=True)
class SeasonalDiscount:
    rate: float = 0.10

    def discount_for(self, cart: Cart, customer: Customer) -> float:
        return self.rate * cart.subtotal()


@dataclass(frozen=True)
class VipDiscount:
    rate: float = 0.05

    def discount_for(self, cart: Cart, customer: Customer) -> float:
        return self.rate * cart.subtotal() if customer.vip else 0.0


@dataclass(frozen=True)
class BulkDiscount:
    threshold: float = 200.0
    amount: float = 15.0

    def discount_for(self, cart: Cart, customer: Customer) -> float:
        return self.amount if cart.subtotal() >= self.threshold else 0.0


@dataclass(frozen=True)
class CompositeDiscountPolicy:
    policies: tuple[DiscountPolicy, ...]

    def discount_for(self, cart: Cart, customer: Customer) -> float:
        return sum(p.discount_for(cart, customer) for p in self.policies)
