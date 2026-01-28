# BAD: no seam. PaymentService news up its dependency.
# This is "sealed design" — you can't substitute StripeClient in a unit test.

class StripeClient:
    def charge(self, amount: float) -> dict:
        # Imagine: real network call to Stripe here.
        # Your unit test would accidentally hit the network.
        return {"status": "ok", "provider": "stripe", "charged": round(amount, 2)}

class PaymentService:
    def __init__(self):
        # ❌ PROBLEM: creation is inside the service
        self.client = StripeClient()

    def charge(self, amount: float) -> dict:
        return self.client.charge(amount)