# Unit test with a FAKE (not a mock framework).
# The fake is simple, controlled, and observable.

class FakePaymentClient:
    def __init__(self):
        self.calls = []

    def charge(self, amount: float) -> dict:
        self.calls.append(amount)
        return {"status": "ok"}

class PaymentService:
    def __init__(self, client):
        self.client = client

    def charge(self, amount: float) -> dict:
        return self.client.charge(amount)

def test_charge_uses_client_and_records_call():
    fake = FakePaymentClient()
    service = PaymentService(fake)

    result = service.charge(50.00)

    assert fake.calls == [50.00]
    assert result["status"] == "ok"