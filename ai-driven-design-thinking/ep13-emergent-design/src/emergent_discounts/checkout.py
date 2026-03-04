from .order import Order
from .factory import DiscountStrategyFactory

class CheckoutService:
    def __init__(self, discount_factory: DiscountStrategyFactory) -> None:
        self._discount_factory = discount_factory

    # Rule 2: the rest of your code can call methods, but must NEVER instantiate.
    def total_after_discount_cents(self, order: Order) -> int:
        strategy = self._discount_factory.create(order)
        discount = strategy.process(order)
        return max(0, order.subtotal_cents - discount)
