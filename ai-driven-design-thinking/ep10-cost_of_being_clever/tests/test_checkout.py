import pytest

from shared.order import Order

from clever_checkout.factory import checkout_total as clever_total
from simple_checkout.checkout import checkout_total as simple_total


@pytest.mark.parametrize(
    "order, expected",
    [
        (Order(base_price=100.0, is_vip=False, region="local", payment_valid=True), 100.0),
        (Order(base_price=100.0, is_vip=True, region="local", payment_valid=True), 90.0),
        (Order(base_price=100.0, is_vip=False, region="remote", payment_valid=True), 110.0),
        (Order(base_price=100.0, is_vip=True, region="remote", payment_valid=True), 100.0),  # 90 + 10
    ],
)
def test_both_designs_produce_same_totals(order, expected):
    assert simple_total(order) == pytest.approx(expected)
    assert clever_total(order, env="prod", enable_audit=True) == pytest.approx(expected)


def test_both_designs_fail_on_invalid_payment():
    order = Order(base_price=100.0, is_vip=False, region="local", payment_valid=False)
    with pytest.raises(ValueError):
        simple_total(order)
    with pytest.raises(ValueError):
        clever_total(order, env="prod", enable_audit=True)
