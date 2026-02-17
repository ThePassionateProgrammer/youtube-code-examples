from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict


@dataclass(frozen=True)
class Item:
    sku: str
    qty: int
    unit_price: float


@dataclass(frozen=True)
class Customer:
    id: str
    vip: bool = False


@dataclass(frozen=True)
class CheckoutResult:
    subtotal: float
    discount: float
    shipping: float
    tax: float
    total: float
    receipt: str


class CheckoutService:
    """BEFORE: One method owns *many* business decisions.

    This is intentionally "low cohesion" so the test wants to be big.
    """

    def checkout(self, items: List[Item], customer: Customer, env: Dict) -> CheckoutResult:
        # 1) Validate
        if not items:
            raise ValueError("Cart is empty")

        for it in items:
            if it.qty <= 0:
                raise ValueError("Invalid qty")
            if it.unit_price < 0:
                raise ValueError("Invalid price")

        # 2) Subtotal
        subtotal = sum(it.qty * it.unit_price for it in items)

        # 3) Discount (multiple rules, multiple axes)
        discount = 0.0
        if env.get("seasonal_discount_enabled", False):
            discount += 0.10 * subtotal  # 10% seasonal
        if customer.vip:
            discount += 0.05 * subtotal  # +5% VIP
        if subtotal >= env.get("bulk_discount_threshold", 200.0):
            discount += 15.0  # flat bulk discount

        discounted_subtotal = max(0.0, subtotal - discount)

        # 4) Shipping
        shipping = env.get("base_shipping", 7.99)
        if customer.vip and env.get("vip_free_shipping", True):
            shipping = 0.0
        elif discounted_subtotal >= env.get("free_shipping_threshold", 100.0):
            shipping = 0.0

        # 5) Tax
        tax_rate = env.get("tax_rate", 0.08)
        taxable_amount = discounted_subtotal + shipping
        tax = round(tax_rate * taxable_amount, 2)

        # 6) Total + Receipt formatting
        total = round(discounted_subtotal + shipping + tax, 2)
        receipt = (
            f"SUBTOTAL={subtotal:.2f}\n"
            f"DISCOUNT={discount:.2f}\n"
            f"SHIPPING={shipping:.2f}\n"
            f"TAX={tax:.2f}\n"
            f"TOTAL={total:.2f}"
        )

        return CheckoutResult(
            subtotal=subtotal,
            discount=discount,
            shipping=shipping,
            tax=tax,
            total=total,
            receipt=receipt,
        )
