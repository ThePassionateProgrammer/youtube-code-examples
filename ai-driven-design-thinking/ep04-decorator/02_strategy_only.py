class PaymentStrategy:
    def pay(self, ctx): pass

class StripePayment(PaymentStrategy): ...
class PaypalPayment(PaymentStrategy): ...

class PaymentFactory:
    def create(self, kind):
        if kind == "stripe":
            return StripePayment()