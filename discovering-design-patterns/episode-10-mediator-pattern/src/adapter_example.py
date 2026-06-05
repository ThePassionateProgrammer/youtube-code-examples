"""Adapter comparison: translates an incompatible interface."""


class StripeApi:
    def create_payment_intent(self, cents: int) -> str:
        return f"stripe_intent:{cents}"


class PaymentGatewayAdapter:
    def __init__(self, stripe_api: StripeApi):
        self.stripe_api = stripe_api

    def charge(self, dollars: float) -> str:
        cents = int(dollars * 100)
        return self.stripe_api.create_payment_intent(cents)
