from domain import Order, PricingPolicy

def checkout(order: Order, pricing_policy: PricingPolicy) -> float:
    """Rule 2: behavior-only. No instantiation in production code."""
    return pricing_policy.total(order)
