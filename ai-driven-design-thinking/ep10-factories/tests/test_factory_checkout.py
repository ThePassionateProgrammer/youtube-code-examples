from __future__ import annotations

from app.domain import CheckoutConfig, CustomerType, Destination, Order
from app.factory_checkout import checkout


def test_factory_checkout_matches_expected_total():
    order = Order(subtotal_cents=10000, is_holiday=True)
    config = CheckoutConfig(customer=CustomerType.VIP, destination=Destination.US)
    total = checkout(order, config)
    assert total == 8799
