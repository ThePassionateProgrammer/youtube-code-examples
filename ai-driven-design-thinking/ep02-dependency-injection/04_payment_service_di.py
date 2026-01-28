# CONSTRUCTOR INJECTION (DI):
# Instead of creating the dependency, we receive it.
# This constructor parameter is the seam.

class StripeClient:
    def charge(self, amount: float) -> dict:
        return {"status": "ok", "provider": "stripe", "charged": round(amount, 2)}

class PaymentService:
    def __init__(self, client):
        # ✅ seam: the service accepts a client
        self.client = client

    def charge(self, amount: float) -> dict:
        return self.client.charge(amount)

# Optional "sensible default" variant (still shows DI clearly):
class PaymentClientFactory:
    @staticmethod
    def create_payment_client():
        return StripeClient()

class PaymentServiceWithDefault:
    def __init__(self, client=None):
        # ✅ seam + default wiring at the edge
        self.client = client or PaymentClientFactory.create_payment_client()

    def charge(self, amount: float) -> dict:
        return self.client.charge(amount)