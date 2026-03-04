from __future__ import annotations
from abc import ABC, abstractmethod
from .order import Order

class DiscountStrategy(ABC):
    @abstractmethod
    def process(self, order: Order) -> int: ...

class VipDiscount(DiscountStrategy):
    def process(self, order: Order) -> int:
        return int(order.subtotal_cents * 0.20)

class EmployeeDiscount(DiscountStrategy):
    def process(self, order: Order) -> int:
        return int(order.subtotal_cents * 0.30)

class SeasonalDiscount(DiscountStrategy):
    def process(self, order: Order) -> int:
        return int(order.subtotal_cents * 0.10)
