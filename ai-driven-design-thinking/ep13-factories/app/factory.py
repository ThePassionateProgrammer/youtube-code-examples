from discounts import VipDiscount, StandardDiscount, SeasonalDiscount
from shipping import ExpressShipping, FlatRateShipping, FreeShipping
from domain import PricingPolicy

class PricingPolicyFactory:
    """Factory holds identity decisions.

    Rule 1: instantiate only — never call behavior methods here.
    """

    def create(self, user, env: str, order_total: float) -> PricingPolicy:
        # Decision: which discount?
        if user.is_vip:
            discount = VipDiscount()
        elif env == "prod" and order_total >= 200:
            discount = SeasonalDiscount()
        else:
            discount = StandardDiscount()

        # Decision: which shipping?
        if user.is_vip and order_total >= 150:
            shipping = FreeShipping()
        elif env == "prod":
            shipping = ExpressShipping()
        else:
            shipping = FlatRateShipping()

        return PricingPolicy(discount=discount, shipping=shipping)
