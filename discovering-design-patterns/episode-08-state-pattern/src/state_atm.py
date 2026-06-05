"""Object-oriented ATM example using the State Pattern.

The same input methods exist in every state, but their meaning is state-specific.
State objects are stateless and shared, while ATMSession carries the changing context.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Protocol


class ATMState(Protocol):
    name: str

    def enter_number(self, session: "ATMSession", value: int | str) -> None: ...
    def press_ok(self, session: "ATMSession") -> None: ...
    def press_cancel(self, session: "ATMSession") -> None: ...
    def select_withdraw(self, session: "ATMSession") -> None: ...
    def select_deposit(self, session: "ATMSession") -> None: ...


class BaseState:
    name = "base"

    def enter_number(self, session: "ATMSession", value: int | str) -> None:
        session.messages.append(f"Number ignored in {self.name}")

    def press_ok(self, session: "ATMSession") -> None:
        session.messages.append(f"OK ignored in {self.name}")

    def press_cancel(self, session: "ATMSession") -> None:
        session.amount = None
        session.state = AUTHENTICATED if session.pin == "1234" else WELCOME
        session.messages.append("Cancelled")

    def select_withdraw(self, session: "ATMSession") -> None:
        session.messages.append(f"Withdraw unavailable in {self.name}")

    def select_deposit(self, session: "ATMSession") -> None:
        session.messages.append(f"Deposit unavailable in {self.name}")


class WelcomeState(BaseState):
    name = "welcome"

    def enter_number(self, session: "ATMSession", value: int | str) -> None:
        session.pin = str(value)
        session.messages.append("PIN entered")

    def press_ok(self, session: "ATMSession") -> None:
        if session.pin == "1234":
            session.state = AUTHENTICATED
            session.messages.append("Authenticated")
        else:
            session.messages.append("Invalid PIN")

    def press_cancel(self, session: "ATMSession") -> None:
        session.pin = None
        session.messages.append("Cleared PIN")


class AuthenticatedState(BaseState):
    name = "authenticated"

    def select_withdraw(self, session: "ATMSession") -> None:
        session.state = WITHDRAW
        session.messages.append("Withdraw selected")

    def select_deposit(self, session: "ATMSession") -> None:
        session.state = DEPOSIT
        session.messages.append("Deposit selected")


class WithdrawState(BaseState):
    name = "withdraw"

    def enter_number(self, session: "ATMSession", value: int | str) -> None:
        session.amount = int(value)
        session.messages.append(f"Withdraw amount entered: {value}")

    def press_ok(self, session: "ATMSession") -> None:
        if session.amount is None:
            session.messages.append("Enter amount first")
        elif session.amount <= session.balance:
            session.balance -= session.amount
            session.messages.append(f"Withdrew {session.amount}")
            session.amount = None
            session.state = AUTHENTICATED
        else:
            session.messages.append("Insufficient funds")


class DepositState(BaseState):
    name = "deposit"

    def enter_number(self, session: "ATMSession", value: int | str) -> None:
        session.amount = int(value)
        session.messages.append(f"Deposit amount entered: {value}")

    def press_ok(self, session: "ATMSession") -> None:
        if session.amount is None:
            session.messages.append("Enter amount first")
        else:
            session.balance += session.amount
            session.deposits.append(session.amount)
            session.messages.append(f"Deposited {session.amount}")
            session.amount = None
            session.state = AUTHENTICATED


# Shared stateless state objects: the Flyweight idea.
WELCOME = WelcomeState()
AUTHENTICATED = AuthenticatedState()
WITHDRAW = WithdrawState()
DEPOSIT = DepositState()


@dataclass
class ATMSession:
    state: ATMState = WELCOME
    pin: str | None = None
    amount: int | None = None
    balance: int = 500
    deposits: list[int] = field(default_factory=list)
    messages: list[str] = field(default_factory=list)

    @property
    def state_name(self) -> str:
        return self.state.name

    def enter_number(self, value: int | str) -> None:
        self.state.enter_number(self, value)

    def press_ok(self) -> None:
        self.state.press_ok(self)

    def press_cancel(self) -> None:
        self.state.press_cancel(self)

    def select_withdraw(self) -> None:
        self.state.select_withdraw(self)

    def select_deposit(self) -> None:
        self.state.select_deposit(self)
