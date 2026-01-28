from __future__ import annotations
from abc import ABC, abstractmethod

from _01_strategies import (
    FeeStrategy, ChargeStrategy, ReceiptStrategy,
    StripeFeeStrategy, StripeChargeStrategy, StripeReceiptStrategy,
    PaypalFeeStrategy, PaypalChargeStrategy, PaypalReceiptStrategy,
    AcmePayFeeStrategy, AcmePayChargeStrategy, AcmePayReceiptStrategy,
)


class PaymentComponentsFactory(ABC):
    @abstractmethod
    def create_fee_strategy(self) -> FeeStrategy: ...

    @abstractmethod
    def create_charge_strategy(self) -> ChargeStrategy: ...

    @abstractmethod
    def create_receipt_strategy(self) -> ReceiptStrategy: ...


class StripeComponentsFactory(PaymentComponentsFactory):
    def create_fee_strategy(self) -> FeeStrategy:
        return StripeFeeStrategy()

    def create_charge_strategy(self) -> ChargeStrategy:
        return StripeChargeStrategy()

    def create_receipt_strategy(self) -> ReceiptStrategy:
        return StripeReceiptStrategy()


class PaypalComponentsFactory(PaymentComponentsFactory):
    def create_fee_strategy(self) -> FeeStrategy:
        return PaypalFeeStrategy()

    def create_charge_strategy(self) -> ChargeStrategy:
        return PaypalChargeStrategy()

    def create_receipt_strategy(self) -> ReceiptStrategy:
        return PaypalReceiptStrategy()


class AcmePayComponentsFactory(PaymentComponentsFactory):
    def create_fee_strategy(self) -> FeeStrategy:
        return AcmePayFeeStrategy()

    def create_charge_strategy(self) -> ChargeStrategy:
        return AcmePayChargeStrategy()

    def create_receipt_strategy(self) -> ReceiptStrategy:
        return AcmePayReceiptStrategy()
