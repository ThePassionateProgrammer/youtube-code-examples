from __future__ import annotations

from .domain import CheckoutConfig, Order
from .factories import CheckoutFactory


def checkout(order: Order, config: CheckoutConfig) -> int:
    """AFTER: behavior uses objects; construction is delegated to a factory."""
    engine = CheckoutFactory.build(config=config, order=order)  # factory instantiates
    return engine.checkout(order)  # business code uses objects, never instantiates
