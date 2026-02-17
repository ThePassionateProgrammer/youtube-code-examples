from domain import Order

class FlatRateShipping:
    def cost(self, order: Order) -> float:
        return 5.0

class ExpressShipping:
    def cost(self, order: Order) -> float:
        return 15.0

class FreeShipping:
    def cost(self, order: Order) -> float:
        return 0.0
