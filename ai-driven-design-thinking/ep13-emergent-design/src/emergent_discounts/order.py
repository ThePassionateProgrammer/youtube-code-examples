from dataclasses import dataclass
from .customer import Customer

@dataclass(frozen=True)
class Order:
    customer: Customer
    subtotal_cents: int
    is_seasonal_promo: bool = False
