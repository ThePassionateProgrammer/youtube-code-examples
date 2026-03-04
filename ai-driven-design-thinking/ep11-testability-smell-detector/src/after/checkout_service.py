from __future__ import annotations

from dataclasses import dataclass

from .models import Cart, Customer, CheckoutResult
from .discounts import DiscountPolicy
from .shipping import ThresholdShipping, VipFreeShipping
from .taxes import TaxCalculator


@dataclass(frozen=True)
class CheckoutService:
    discount_policy: DiscountPolicy
    threshold_shipping: ThresholdShipping
    vip_free_shipping: VipFreeShipping
    tax_calculator: TaxCalculator

    def checkout(self, cart: Cart, customer: Customer) -> CheckoutResult:
        if not cart.items:
            raise ValueError("Cart is empty")

        subtotal = cart.subtotal()

        discount = self.discount_policy.discount_for(cart, customer)
        discounted_subtotal = max(0.0, subtotal - discount)

        vip_decision = self.vip_free_shipping.shipping_for(discounted_subtotal, customer)
        if vip_decision == vip_decision:  # NaN check
            shipping = vip_decision
        else:
            shipping = self.threshold_shipping.shipping_for(discounted_subtotal, customer)

        tax = self.tax_calculator.tax_for(discounted_subtotal + shipping)
        total = round(discounted_subtotal + shipping + tax, 2)

        return CheckoutResult(
            subtotal=subtotal,
            discount=discount,
            shipping=shipping,
            tax=tax,
            total=total,
        )
