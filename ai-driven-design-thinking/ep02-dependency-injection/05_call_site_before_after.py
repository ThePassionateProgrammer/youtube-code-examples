# Call site BEFORE (sealed):
#
#   service = PaymentService()
#   service.charge(50.00)
#
# The service decides it must use StripeClient.

# Call site AFTER (DI seam):
#
#   service = PaymentService(StripeClient())
#   service.charge(50.00)
#
# The service no longer creates StripeClient — it receives a payment client.

class StripeClient:
    def charge(self, amount: float) -> dict:
        return {"status": "ok", "provider": "stripe", "charged": round(amount, 2)}

class PaymentService:
    def __init__(self, client):
        self.client = client

    def charge(self, amount: float) -> dict:
        return self.client.charge(amount)

# ✅ Production wiring:
service = PaymentService(StripeClient())
result = service.charge(50.00)