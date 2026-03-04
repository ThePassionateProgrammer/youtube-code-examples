from __future__ import annotations

from ecomm.domain import Customer, CustomerType, Order
from ecomm.checkout_conditional import CheckoutProcessor as ConditionalCheckout
from ecomm.checkout_strategy import CheckoutProcessor as StrategyCheckout
from ecomm.checkout_template import CheckoutProcessor as TemplateCheckout
from ecomm.discount_factory import DiscountFactory, DiscountConfig
from ecomm.discount_template import VipTemplateDiscount


def money(cents: int) -> str:
    return f"${cents/100:.2f}"


def main() -> None:
    order = Order(
        customer=Customer(CustomerType.VIP),
        subtotal_cents=10_00,
        coupon_code="SAVE10",
        seasonal_promo=True,
    )

    cond = ConditionalCheckout().calculate_total(order)

    factory = DiscountFactory(DiscountConfig())
    policy = factory.build_policy(order)
    strat = StrategyCheckout(policy).calculate_total(order)

    tmpl = TemplateCheckout(VipTemplateDiscount()).calculate_total(order)

    print("Order:", order)
    print("--- Conditional (trap) ---")
    print("Subtotal:", money(cond.subtotal_cents), "Discount:", money(cond.discount_cents), "Total:", money(cond.total_cents))
    print("--- Strategy (factory decides) ---")
    print("Subtotal:", money(strat.subtotal_cents), "Discount:", money(strat.discount_cents), "Total:", money(strat.total_cents))
    print("--- Template Method (different force) ---")
    print("Subtotal:", money(tmpl.subtotal_cents), "Discount:", money(tmpl.discount_cents), "Total:", money(tmpl.total_cents))


if __name__ == "__main__":
    main()
