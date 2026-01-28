# GOOD: factory owns identity/type coupling (instantiation).
# PaymentService owns representational coupling (method calls).
# This separates two different reasons-to-change.

class StripeClient:
    def charge(self, amount: float) -> dict:
        return {"status": "ok", "provider": "stripe", "charged": round(amount, 2)}

class PaymentClientFactory:
    @staticmethod
    def create_payment_client():
        # ✅ identity/type coupling is here (wired at the edges)
        return StripeClient()

class PaymentService:
    def __init__(self):
        # ✅ service delegates creation
        self.client = PaymentClientFactory.create_payment_client()

    def charge(self, amount: float) -> dict:
        # ✅ service uses the dependency (representation coupling)
        return self.client.charge(amount)