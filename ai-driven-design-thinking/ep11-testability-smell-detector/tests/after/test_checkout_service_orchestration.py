from src.after.models import Cart, Item, Customer
from src.after.discounts import CompositeDiscountPolicy, SeasonalDiscount, VipDiscount, BulkDiscount
from src.after.shipping import ThresholdShipping, VipFreeShipping
from src.after.taxes import TaxCalculator
from src.after.checkout_service import CheckoutService


def test_checkout_orchestrates_without_retesting_policies():
    cart = Cart(items=[Item("BOOK", 2, 30.0), Item("MUG", 1, 15.0)])  # subtotal 75
    customer = Customer("c-123", vip=True)

    discount_policy = CompositeDiscountPolicy(
        policies=(SeasonalDiscount(rate=0.10), VipDiscount(rate=0.05), BulkDiscount(threshold=200.0, amount=15.0))
    )
    svc = CheckoutService(
        discount_policy=discount_policy,
        threshold_shipping=ThresholdShipping(base_shipping=7.99, free_threshold=100.0),
        vip_free_shipping=VipFreeShipping(enabled=True),
        tax_calculator=TaxCalculator(rate=0.08),
    )

    result = svc.checkout(cart, customer)

    assert result.subtotal == 75.0
    assert result.discount == 11.25
    assert result.shipping == 0.0
    assert result.tax == 5.1
    assert result.total == 68.85
