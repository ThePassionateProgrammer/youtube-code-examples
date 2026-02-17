from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    is_vip: bool = False

@dataclass(frozen=True)
class Order:
    total: float

class StandardDiscount:
    def apply(self, total: float) -> float:
        return total

class VipDiscount:
    def apply(self, total: float) -> float:
        return total * 0.90

class FlatRateShipping:
    def cost(self, order: Order) -> float:
        return 5.0

class ExpressShipping:
    def cost(self, order: Order) -> float:
        return 15.0

def checkout(order: Order, user: User, env: str) -> float:
    # TRAP: selection + construction + usage all in one place

    if user.is_vip:
        discount = VipDiscount()
    else:
        discount = StandardDiscount()

    if env == "prod":
        shipping = ExpressShipping()
    else:
        shipping = FlatRateShipping()

    total = discount.apply(order.total)
    total += shipping.cost(order)
    return total

# NEW REQUIREMENT (example friction):
# - Add SeasonalDiscount when env == 'prod' and order.total >= 200
# - Add FreeShipping when user.is_vip and order.total >= 150
