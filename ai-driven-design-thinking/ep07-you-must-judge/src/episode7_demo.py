"""
Episode 7 demo code (The Passionate Programmer)

Theme: "AI can generate code, but only you can judge it."

This module intentionally contains THREE versions of the same capability:

1) Procedural (works, but fights change)
2) "OO-ish" (a class wrapper around procedural logic)
3) OO model (variation lives in objects with agency)

Everything is executable and covered by unit tests.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict


# ============================================================
# 1) PROCEDURAL: "Code that runs" (variation smeared in if/elif)
# ============================================================

def process_payment_procedural(payment_type: str, amount: int) -> str:
    """
    A tiny, plausible-looking function that "works" but encodes variation
    in conditionals. This is the kind of thing AI will happily produce
    by default if you ask for a feature without a model.
    """
    if payment_type == "card":
        # Imagine 4 different business rules creep in here over time...
        return f"CHARGE CARD ${amount}"
    elif payment_type == "paypal":
        return f"CHARGE PAYPAL ${amount}"
    elif payment_type == "bank":
        return f"INITIATE BANK TRANSFER ${amount}"
    else:
        raise ValueError(f"Unsupported payment_type: {payment_type!r}")


# ============================================================
# 2) "OO-ISH": A class statement around procedural logic
#    (directions, not a map)
# ============================================================

@dataclass(frozen=True)
class PaymentProcessorOOish:
    """
    This *looks* OO, but it's still procedural thinking:
    the processor reaches into "payment_type" and decides everything itself.
    """
    def process(self, payment_type: str, amount: int) -> str:
        # Same branching, now hidden inside an object.
        return process_payment_procedural(payment_type, amount)








# ============================================================
# 3) OO MODEL: Objects with agency (variation owned by types)
# ============================================================

class PaymentMethod(ABC):
    """
    Abstract. Doesn't do anything yet. That's the point.
    It expresses intent: "something can charge".
    """
    @abstractmethod
    def charge(self, amount: int) -> str:
        raise NotImplementedError


class CardPayment(PaymentMethod):
    def charge(self, amount: int) -> str:
        return f"CHARGE CARD ${amount}"


class PayPalPayment(PaymentMethod):
    def charge(self, amount: int) -> str:
        return f"CHARGE PAYPAL ${amount}"


class BankTransfer(PaymentMethod):
    def charge(self, amount: int) -> str:
        return f"INITIATE BANK TRANSFER ${amount}"


class PaymentService:
    """
    "PaymentService doesn't care *how* we charge.
    It only knows that *something* can charge."
    """
    def __init__(self, methods: Dict[str, PaymentMethod]) -> None:
        self._methods = dict(methods)

    def process(self, payment_type: str, amount: int) -> str:
        method = self._methods.get(payment_type)
        if method is None:
            raise ValueError(f"Unsupported payment_type: {payment_type!r}")
        return method.charge(amount)


def build_payment_service() -> PaymentService:
    """
    A tiny factory that centralizes wiring.
    Notice: selection is isolated to one place, not smeared across callers.
    """
    return PaymentService(
        methods={
            "card": CardPayment(),
            "paypal": PayPalPayment(),
            "bank": BankTransfer(),
        }
    )


# ============================================================
# CLI entry point (optional for your demo video)
# ============================================================

def main() -> None:
    service = build_payment_service()

    print("PROCEDURAL:", process_payment_procedural("card", 100))
    print("OO-ISH:    ", PaymentProcessorOOish().process("paypal", 100))
    print("OO MODEL:  ", service.process("bank", 100))


if __name__ == "__main__":
    main()
