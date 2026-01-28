from __future__ import annotations
from abc import ABC, abstractmethod


class FeeStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, amount: float) -> float: ...


class ChargeStrategy(ABC):
    @abstractmethod
    def charge(self, amount: float) -> dict: ...


class ReceiptStrategy(ABC):
    @abstractmethod
    def generate_receipt(self, total: float) -> str: ...


# --- Stripe ---
class StripeFeeStrategy(FeeStrategy):
    def calculate_fee(self, amount: float) -> float:
        return amount * 0.029 + 0.30


class StripeChargeStrategy(ChargeStrategy):
    def charge(self, amount: float) -> dict:
        return {"status": "ok", "provider": "stripe", "charged": round(amount, 2)}


class StripeReceiptStrategy(ReceiptStrategy):
    def generate_receipt(self, total: float) -> str:
        return f"Stripe receipt for {round(total, 2)}"


# --- PayPal ---
class PaypalFeeStrategy(FeeStrategy):
    def calculate_fee(self, amount: float) -> float:
        return amount * 0.03


class PaypalChargeStrategy(ChargeStrategy):
    def charge(self, amount: float) -> dict:
        return {"status": "ok", "provider": "paypal", "charged": round(amount, 2)}


class PaypalReceiptStrategy(ReceiptStrategy):
    def generate_receipt(self, total: float) -> str:
        return f"PayPal receipt for {round(total, 2)}"


# --- AcmePay ---
class AcmePayFeeStrategy(FeeStrategy):
    def calculate_fee(self, amount: float) -> float:
        return amount * (0.015 if amount < 100 else 0.02)


class AcmePayChargeStrategy(ChargeStrategy):
    def charge(self, amount: float) -> dict:
        if amount >= 1000:
            return {"status": "declined", "provider": "acmepay"}
        return {"status": "ok", "provider": "acmepay", "charged": round(amount, 2)}


class AcmePayReceiptStrategy(ReceiptStrategy):
    def generate_receipt(self, total: float) -> str:
        return f"AcmePay receipt for {round(total, 2)} (fraud-screened)"
