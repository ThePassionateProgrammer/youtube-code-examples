from src.after.models import Cart, Item, Customer
from src.after.discounts import SeasonalDiscount, VipDiscount, BulkDiscount, CompositeDiscountPolicy


def test_vip_discount_only_affects_vips():
    cart = Cart(items=[Item("BOOK", 2, 30.0)])  # subtotal 60
    policy = VipDiscount(rate=0.05)

    assert policy.discount_for(cart, Customer("c1", vip=False)) == 0.0
    assert policy.discount_for(cart, Customer("c2", vip=True)) == 3.0


def test_seasonal_discount_is_percentage_of_subtotal():
    cart = Cart(items=[Item("MUG", 1, 20.0)])  # subtotal 20
    policy = SeasonalDiscount(rate=0.10)
    assert policy.discount_for(cart, Customer("c", vip=False)) == 2.0


def test_composite_discount_sums_independent_policies():
    cart = Cart(items=[Item("X", 10, 25.0)])  # subtotal 250
    policy = CompositeDiscountPolicy(policies=(SeasonalDiscount(), VipDiscount(), BulkDiscount()))
    assert policy.discount_for(cart, Customer("c", vip=True)) == 52.5
