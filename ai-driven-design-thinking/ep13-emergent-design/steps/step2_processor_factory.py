"""Step 2 — Hedge your bets with the minimum useful move."""
from emergent_discounts.order import Order

class DiscountProcessor:
    def process(self, order: Order) -> int:
        if order.customer.is_vip:
            return int(order.subtotal_cents * 0.20)
        if order.customer.is_employee:
            return int(order.subtotal_cents * 0.30)
        return 0

class DiscountFactory:
    def create(self) -> DiscountProcessor:
        return DiscountProcessor()
