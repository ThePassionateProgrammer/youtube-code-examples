from __future__ import annotations

from .domain import CheckoutConfig, CustomerType, Destination, Order
from .factory_checkout import checkout
from .trap_checkout import checkout_trap


def dollars(cents: int) -> str:
    return f"${cents/100:.2f}"


def main() -> None:
    order = Order(subtotal_cents=12_500, is_holiday=True)
    config = CheckoutConfig(customer=CustomerType.VIP, destination=Destination.US)

    trap_total = checkout_trap(order, config)
    factory_total = checkout(order, config)

    print("TRAP total:   ", dollars(trap_total))
    print("FACTORY total:", dollars(factory_total))


if __name__ == "__main__":
    main()
