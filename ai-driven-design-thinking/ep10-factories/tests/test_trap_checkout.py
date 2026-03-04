from __future__ import annotations

from app.domain import CheckoutConfig, CustomerType, Destination, Order
from app.trap_checkout import checkout_trap


def test_trap_checkout_vip_holiday_us():
    order = Order(subtotal_cents=10000, is_holiday=True)
    config = CheckoutConfig(customer=CustomerType.VIP, destination=Destination.US)
    total = checkout_trap(order, config)
    # VIP holiday 20% off => 8000, free shipping over $100? no (8000 < 10000) => +799
    assert total == 8799
