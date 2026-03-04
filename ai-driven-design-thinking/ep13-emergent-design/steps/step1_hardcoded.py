"""Step 1 — Hard-coded rule (disciplined minimalism)."""
from emergent_discounts.order import Order

def discount_cents(order: Order) -> int:
    if order.customer.is_vip:
        return int(order.subtotal_cents * 0.20)
    return 0
