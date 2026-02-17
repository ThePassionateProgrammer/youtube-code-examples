from checkout_bad import CreditCard, Account, Customer, Order, charge_order_bad
from checkout_good import CreditCard as GCreditCard, Account as GAccount, Customer as GCustomer, Order as GOrder

class ConsoleGateway:
    def charge(self, card_number: str, amount_cents: int) -> str:
        print(f"[gateway] charging {card_number} for {amount_cents} cents")
        return "ok"

def run():
    gw = ConsoleGateway()

    bad_order = Order(customer=Customer(account=Account(credit_card=CreditCard(number="4111"))), total_cents=500)
    print("BAD :", charge_order_bad(bad_order, gw))

    good_order = GOrder(_customer=GCustomer(_account=GAccount(_credit_card=GCreditCard(number="4111"))), total_cents=500)
    print("GOOD:", good_order.charge(gw))

if __name__ == "__main__":
    run()
