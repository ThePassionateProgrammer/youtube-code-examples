from checkout_bad import CreditCard, Account, Customer, Order, charge_order_bad
from checkout_good import CreditCard as GCreditCard, Account as GAccount, Customer as GCustomer, Order as GOrder
from test_doubles import SpyGateway

def test_bad_charge_navigates_graph_and_calls_gateway():
    gateway = SpyGateway()
    order = Order(customer=Customer(account=Account(credit_card=CreditCard(number="4111"))), total_cents=500)
    result = charge_order_bad(order, gateway)  # type: ignore[arg-type]
    assert result == "ok"
    assert gateway.calls == [("4111", 500)]

def test_good_charge_hides_graph_traversal_inside_objects():
    gateway = SpyGateway()
    order = GOrder(_customer=GCustomer(_account=GAccount(_credit_card=GCreditCard(number="4111"))), total_cents=500)
    result = order.charge(gateway)
    assert result == "ok"
    assert gateway.calls == [("4111", 500)]

def test_demeter_makes_change_local():
    """Change payment details without rewriting callers."""
    gateway = SpyGateway()

    acct = GAccount(_credit_card=GCreditCard(number="4242"))
    order = GOrder(_customer=GCustomer(_account=acct), total_cents=1200)

    order.charge(gateway)
    assert gateway.calls == [("4242", 1200)]
