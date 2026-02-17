from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto


class CustomerType(Enum):
    REGULAR = auto()
    VIP = auto()
    EMPLOYEE = auto()


@dataclass(frozen=True)
class Customer:
    customer_type: CustomerType


@dataclass(frozen=True)
class Order:
    customer: Customer
    subtotal_cents: int
    coupon_code: str | None = None
    seasonal_promo: bool = False
