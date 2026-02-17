from domain import Order, User
from factory import PricingPolicyFactory
from checkout import checkout

def test_checkout_vip_prod_small_order():
    f = PricingPolicyFactory()
    order = Order(100)
    policy = f.create(user=User(is_vip=True), env="prod", order_total=order.total)
    assert checkout(order, policy) == 0.90 * 100 + 15.0

def test_checkout_vip_prod_big_order_free_shipping():
    f = PricingPolicyFactory()
    order = Order(160)
    policy = f.create(user=User(is_vip=True), env="prod", order_total=order.total)
    assert checkout(order, policy) == 0.90 * 160 + 0.0

def test_checkout_nonvip_prod_big_order_seasonal_discount():
    f = PricingPolicyFactory()
    order = Order(220)
    policy = f.create(user=User(is_vip=False), env="prod", order_total=order.total)
    assert checkout(order, policy) == 0.95 * 220 + 15.0
