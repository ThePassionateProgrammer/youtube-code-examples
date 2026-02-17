from dataclasses import dataclass
@dataclass
class CreditCard:
    number: str
@dataclass
class Account:
    credit_card: CreditCard
@dataclass
class Customer:
    account: Account
@dataclass
class Order:
    customer: Customer
    total_cents: int

class PaymentGateway:
    """Represents an external system (network call)."""
    def charge(self, card_number: str, amount_cents: int) -> str:
        # In real life this would hit Stripe/etc.
        return f"charged:{card_number}:{amount_cents}"

def charge_order_bad(order: Order, gateway: PaymentGateway) -> str:
    """DEMETER VIOLATION: caller navigates a graph (order.customer.account.credit_card.number)."""
    card_number = order.customer.account.credit_card.number  # <-- the 'many dots' smell
    return gateway.charge(card_number, order.total_cents)
