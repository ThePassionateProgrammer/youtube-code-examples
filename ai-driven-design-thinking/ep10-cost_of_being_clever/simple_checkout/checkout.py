from __future__ import annotations

from shared.order import Order

VIP_DISCOUNT_RATE = 0.10
NON_LOCAL_SHIPPING_FEE = 10.0

def checkout_total(order: Order) -> float:
    """
    Fits the real forces:
    - 3 fixed business rules
    - low cognitive load
    - still fully testable
    """
    if not order.payment_valid:
        raise ValueError("Invalid payment")

    total = order.base_price

    if order.is_vip:
        total = total * (1.0 - VIP_DISCOUNT_RATE)

    if order.region != "local":
        total += NON_LOCAL_SHIPPING_FEE

    return total
