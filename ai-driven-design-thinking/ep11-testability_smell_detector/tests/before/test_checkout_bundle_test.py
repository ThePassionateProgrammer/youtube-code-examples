import pytest

from src.before.checkout_before import CheckoutService, Item, Customer


def test_checkout_bundle_test_many_asserts():
    """Intentionally NOT a unit test: many reasons to fail."""
    svc = CheckoutService()
    env = {
        "seasonal_discount_enabled": True,
        "bulk_discount_threshold": 200.0,
        "free_shipping_threshold": 100.0,
        "vip_free_shipping": True,
        "tax_rate": 0.08,
        "base_shipping": 7.99,
    }

    items = [
        Item(sku="BOOK", qty=2, unit_price=30.0),   # 60
        Item(sku="MUG", qty=1, unit_price=15.0),    # 15  subtotal=75
    ]
    customer = Customer(id="c-123", vip=True)

    result = svc.checkout(items, customer, env)

    # Many asserts = many reasons to fail
    assert result.subtotal == 75.0
    assert result.discount == pytest.approx(0.10 * 75.0 + 0.05 * 75.0)  # seasonal + VIP
    assert result.shipping == 0.0  # VIP free shipping
    assert result.tax == pytest.approx(round(0.08 * (75.0 - result.discount + result.shipping), 2))
    assert result.total == pytest.approx(round((75.0 - result.discount + result.shipping + result.tax), 2))
    assert "SUBTOTAL=75.00" in result.receipt
    assert "DISCOUNT=" in result.receipt
    assert "TOTAL=" in result.receipt


def test_empty_cart_raises():
    svc = CheckoutService()
    with pytest.raises(ValueError):
        svc.checkout([], Customer(id="c-0"), {})
