def charge(amount, card, processor):
    if processor == "stripe":
        # stripe logic
        pass
    elif processor == "paypal":
        # paypal logic
        pass
# 
class PaymentProcessor:
    def charge(self, amount, card):
        pass

class StripeProcessor(PaymentProcessor):
    def charge(self, amount, card):
        pass

class PaypalProcessor(PaymentProcessor):
    def charge(self, amount, card):
        pass

def charge(amount, card, processor: PaymentProcessor):
    processor.charge(amount, card)
    
    
# Charge
# ├─ Logging?
# ├─ Fraud Check?
# └─ Receipt?
#
## Now becomes:
# Charge
# └─ Stripe
#    ├─ Logging
#    ├─ Fraud
#    └─ Receipt
#
#
# Stable Core
# ──────────────
# PaymentProcessor
# process()
#
#
# Flexible Edge
# ──────────────
# Logging
# FraudCheck
# Receipt
#
#
#
#
#
#

