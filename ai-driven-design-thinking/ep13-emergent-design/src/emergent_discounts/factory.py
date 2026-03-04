from .order import Order
from .strategies import DiscountStrategy, VipDiscount, EmployeeDiscount, SeasonalDiscount

class DiscountStrategyFactory:
    # Rule 1: factories instantiate objects but NEVER call their methods.
    def create(self, order: Order) -> DiscountStrategy:
        if order.customer.is_employee:
            return EmployeeDiscount()
        if order.customer.is_vip:
            return VipDiscount()
        if order.is_seasonal_promo:
            return SeasonalDiscount()
        return _NoDiscount()

class _NoDiscount(DiscountStrategy):
    def process(self, order: Order) -> int:
        return 0
