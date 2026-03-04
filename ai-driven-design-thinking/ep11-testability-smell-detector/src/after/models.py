from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Item:
    sku: str
    qty: int
    unit_price: float


@dataclass(frozen=True)
class Customer:
    id: str
    vip: bool = False


@dataclass(frozen=True)
class Cart:
    items: List[Item]

    def subtotal(self) -> float:
        return sum(it.qty * it.unit_price for it in self.items)


@dataclass(frozen=True)
class CheckoutResult:
    subtotal: float
    discount: float
    shipping: float
    tax: float
    total: float
