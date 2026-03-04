from __future__ import annotations

from app.domain import CheckoutConfig, CustomerType, Destination, Order
from app.factories import CheckoutFactory, PricingEngine
from app.policies import HolidayDiscount, InternationalShipping, VipDiscount, FreeShippingOver


def test_factory_build_returns_engine():
    order = Order(subtotal_cents=5000)
    config = CheckoutConfig(customer=CustomerType.REGULAR, destination=Destination.US)
    engine = CheckoutFactory.build(config=config, order=order)
    assert isinstance(engine, PricingEngine)


def test_factory_selects_vip_holiday_discount():
    order = Order(subtotal_cents=5000, is_holiday=True)
    config = CheckoutConfig(customer=CustomerType.VIP, destination=Destination.US)
    engine = CheckoutFactory.build(config=config, order=order)
    assert isinstance(engine.discount, VipDiscount)
    assert engine.discount.percent_off == 20


def test_factory_selects_holiday_discount_for_regular_holiday():
    order = Order(subtotal_cents=5000, is_holiday=True)
    config = CheckoutConfig(customer=CustomerType.REGULAR, destination=Destination.US)
    engine = CheckoutFactory.build(config=config, order=order)
    assert isinstance(engine.discount, HolidayDiscount)


def test_factory_selects_international_shipping():
    order = Order(subtotal_cents=5000)
    config = CheckoutConfig(customer=CustomerType.REGULAR, destination=Destination.INTERNATIONAL)
    engine = CheckoutFactory.build(config=config, order=order)
    assert isinstance(engine.shipping, InternationalShipping)


def test_factory_selects_us_shipping():
    order = Order(subtotal_cents=5000)
    config = CheckoutConfig(customer=CustomerType.REGULAR, destination=Destination.US)
    engine = CheckoutFactory.build(config=config, order=order)
    assert isinstance(engine.shipping, FreeShippingOver)
