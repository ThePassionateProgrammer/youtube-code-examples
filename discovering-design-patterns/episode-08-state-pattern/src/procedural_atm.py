"""Procedural ATM example for Episode 8: State Pattern.

This version works, but every input handler must ask:
"What mode am I in?"
"""
from dataclasses import dataclass


@dataclass
class ATMSession:
    mode: str = "welcome"
    pin: str | None = None
    amount: int | None = None
    balance: int = 500
    deposits: list[int] | None = None
    messages: list[str] | None = None

    def __post_init__(self) -> None:
        self.deposits = [] if self.deposits is None else self.deposits
        self.messages = [] if self.messages is None else self.messages


def enter_number(session: ATMSession, value: int | str) -> None:
    """Same input, different meaning depending on mode."""
    if session.mode == "welcome":
        session.pin = str(value)
        session.messages.append("PIN entered")
    elif session.mode == "withdraw":
        session.amount = int(value)
        session.messages.append(f"Withdraw amount entered: {value}")
    elif session.mode == "deposit":
        session.amount = int(value)
        session.messages.append(f"Deposit amount entered: {value}")
    else:
        session.messages.append(f"Number ignored in mode: {session.mode}")


def press_ok(session: ATMSession) -> None:
    if session.mode == "welcome":
        if session.pin == "1234":
            session.mode = "authenticated"
            session.messages.append("Authenticated")
        else:
            session.messages.append("Invalid PIN")
    elif session.mode == "withdraw":
        if session.amount is None:
            session.messages.append("Enter amount first")
        elif session.amount <= session.balance:
            session.balance -= session.amount
            session.messages.append(f"Withdrew {session.amount}")
            session.amount = None
            session.mode = "authenticated"
        else:
            session.messages.append("Insufficient funds")
    elif session.mode == "deposit":
        if session.amount is None:
            session.messages.append("Enter amount first")
        else:
            session.balance += session.amount
            session.deposits.append(session.amount)
            session.messages.append(f"Deposited {session.amount}")
            session.amount = None
            session.mode = "authenticated"


def select_withdraw(session: ATMSession) -> None:
    if session.mode == "authenticated":
        session.mode = "withdraw"
        session.messages.append("Withdraw selected")
    else:
        session.messages.append("Withdraw unavailable")


def select_deposit(session: ATMSession) -> None:
    if session.mode == "authenticated":
        session.mode = "deposit"
        session.messages.append("Deposit selected")
    else:
        session.messages.append("Deposit unavailable")


def press_cancel(session: ATMSession) -> None:
    if session.mode == "welcome":
        session.messages.append("Already at welcome")
    else:
        session.amount = None
        session.mode = "authenticated" if session.pin == "1234" else "welcome"
        session.messages.append("Cancelled")
