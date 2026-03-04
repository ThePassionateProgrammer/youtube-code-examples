from __future__ import annotations

import pytest

from ecomm.domain import Customer, CustomerType, Order
from ecomm.checkout_conditional import CheckoutProcessor as ConditionalCheckout
from ecomm.checkout_strategy import CheckoutProcessor as StrategyCheckout
from ecomm.checkout_template import CheckoutProcessor as TemplateCheckout
from ecomm.discount_factory import DiscountFactory, DiscountConfig
from ecomm.discount_template import (
    VipTemplateDiscount,
    EmployeeTemplateDiscount,
    Coupon10TemplateDiscount,
    SeasonalPromoTemplateDiscount,
)


@pytest.mark.parametrize(
    "order, template",
    [
        (Order(Customer(CustomerType.VIP), 10_00, coupon_code="SAVE10", seasonal_promo=True), VipTemplateDiscount()),
        (Order(Customer(CustomerType.EMPLOYEE), 10_00, coupon_code=None, seasonal_promo=False), EmployeeTemplateDiscount()),
        (Order(Customer(CustomerType.REGULAR), 10_00, coupon_code="SAVE10", seasonal_promo=False), Coupon10TemplateDiscount()),
        (Order(Customer(CustomerType.REGULAR), 10_00, coupon_code=None, seasonal_promo=True), SeasonalPromoTemplateDiscount()),
    ],
)
def test_all_versions_produce_valid_totals(order: Order, template) -> None:
    cond = ConditionalCheckout().calculate_total(order)

    factory = DiscountFactory(DiscountConfig())
    policy = factory.build_policy(order)
    strat = StrategyCheckout(policy).calculate_total(order)

    tmpl = TemplateCheckout(template).calculate_total(order)

    for res in (cond, strat, tmpl):
        assert 0 <= res.discount_cents <= res.subtotal_cents
        assert res.total_cents == res.subtotal_cents - res.discount_cents


def test_strategy_matches_conditional_for_same_config() -> None:
    order = Order(Customer(CustomerType.VIP), 10_00, coupon_code="SAVE10", seasonal_promo=True)

    cond = ConditionalCheckout().calculate_total(order)

    factory = DiscountFactory(DiscountConfig())
    policy = factory.build_policy(order)
    strat = StrategyCheckout(policy).calculate_total(order)

    assert strat.total_cents == cond.total_cents


def test_green_bar_does_not_mean_good_design() -> None:
    order = Order(Customer(CustomerType.REGULAR), 10_00, coupon_code=None, seasonal_promo=False)

    cond = ConditionalCheckout().calculate_total(order)
    factory = DiscountFactory(DiscountConfig())
    policy = factory.build_policy(order)
    strat = StrategyCheckout(policy).calculate_total(order)

    assert strat.total_cents == cond.total_cents == 10_00
