from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class CustomerType(str, Enum):
    REGULAR = "regular"
    VIP = "vip"


class Destination(str, Enum):
    US = "us"
    INTERNATIONAL = "international"


@dataclass(frozen=True)
class Order:
    subtotal_cents: int
    is_holiday: bool = False


@dataclass(frozen=True)
class CheckoutConfig:
    customer: CustomerType
    destination: Destination
