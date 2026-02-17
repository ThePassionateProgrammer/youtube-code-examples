from domain import User
from factory import PricingPolicyFactory
from discounts import VipDiscount, StandardDiscount, SeasonalDiscount
from shipping import ExpressShipping, FlatRateShipping, FreeShipping

def test_vip_gets_vip_discount():
    f = PricingPolicyFactory()
    p = f.create(user=User(is_vip=True), env="dev", order_total=100)
    assert isinstance(p.discount, VipDiscount)

def test_seasonal_discount_in_prod_for_big_orders():
    f = PricingPolicyFactory()
    p = f.create(user=User(is_vip=False), env="prod", order_total=200)
    assert isinstance(p.discount, SeasonalDiscount)

def test_standard_discount_default():
    f = PricingPolicyFactory()
    p = f.create(user=User(is_vip=False), env="dev", order_total=50)
    assert isinstance(p.discount, StandardDiscount)

def test_free_shipping_for_vip_big_orders():
    f = PricingPolicyFactory()
    p = f.create(user=User(is_vip=True), env="prod", order_total=150)
    assert isinstance(p.shipping, FreeShipping)

def test_express_shipping_in_prod():
    f = PricingPolicyFactory()
    p = f.create(user=User(is_vip=False), env="prod", order_total=120)
    assert isinstance(p.shipping, ExpressShipping)

def test_flat_rate_shipping_in_dev():
    f = PricingPolicyFactory()
    p = f.create(user=User(is_vip=False), env="dev", order_total=120)
    assert isinstance(p.shipping, FlatRateShipping)
