from __future__ import annotations

from .domain import CheckoutConfig, CustomerType, Destination, Order
from .policies import (
    BulkDiscount,
    DiscountPolicy,
    FreeShippingOver,
    HolidayDiscount,
    InternationalShipping,
    NoDiscount,
    ShippingPolicy,
    VipDiscount,
)


def checkout_trap(order: Order, config: CheckoutConfig) -> int:
    """BEFORE: identity decisions + construction + usage all tangled together.
    Returns total charge in cents.
    """

    # --- Discount selection (identity coupling) + construction ---
    discount: DiscountPolicy
    if config.customer == CustomerType.VIP and order.is_holiday:
        # 1:00 beat: “add one more discount rule”
        discount = VipDiscount(percent_off=20)  # VIP holiday special
    elif config.customer == CustomerType.VIP:
        discount = VipDiscount()
    else:
        discount = BulkDiscount()

    # --- Shipping selection (more decisions + construction) ---
    shipping: ShippingPolicy
    if config.destination == Destination.INTERNATIONAL:
        shipping = InternationalShipping()
    else:
        shipping = FreeShippingOver()

    # --- Usage (behavior) ---
    discounted = discount.apply(order.subtotal_cents, order)
    shipping_cost = shipping.cost(discounted, order)

    return discounted + shipping_cost
