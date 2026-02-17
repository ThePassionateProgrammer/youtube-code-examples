from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol
class PaymentGateway(Protocol):
    def charge(self, card_number: str, amount_cents: int) -> str: ...
@dataclass(frozen=True)
class CreditCard:
    number: str
@dataclass
class Account:
    _credit_card: CreditCard
    def charge(self, gateway: PaymentGateway, amount_cents: int) -> str:
        # Account owns the detail: which card to use.
        return gateway.charge(self._credit_card.number, amount_cents)
@dataclass
class Customer:
    _account: Account
    def pay_for(self, gateway: PaymentGateway, amount_cents: int) -> str:
        # Customer owns the policy: how the customer pays.
        return self._account.charge(gateway, amount_cents)
@dataclass
class Order:
    _customer: Customer
    total_cents: int
    def charge(self, gateway: PaymentGateway) -> str:
        # Caller asks for the outcome; objects do the work through proper channels.
        return self._customer.pay_for(gateway, self.total_cents)
