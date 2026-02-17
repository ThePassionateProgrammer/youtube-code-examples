from dataclasses import dataclass

@dataclass(frozen=True)
class Order:
    total: float

@dataclass(frozen=True)
class User:
    is_vip: bool = False

class PricingPolicy:
    def __init__(self, discount, shipping):
        self.discount = discount
        self.shipping = shipping

    def total(self, order: Order) -> float:
        total = self.discount.apply(order.total)
        total += self.shipping.cost(order)
        return total
