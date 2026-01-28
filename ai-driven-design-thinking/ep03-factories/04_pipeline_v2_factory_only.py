from __future__ import annotations
from dataclasses import dataclass
from _03_factories import PaymentComponentsFactory


@dataclass(frozen=True)
class PaymentResult:
    charge_result: dict
    receipt: str


class PaymentPipelineV2:
    """
    Strategy + Abstract Factory:
    - Still extensible
    - Enforces valid families
    """
    def __init__(self, factory: PaymentComponentsFactory):
        self._fee = factory.create_fee_strategy()
        self._charger = factory.create_charge_strategy()
        self._receipt = factory.create_receipt_strategy()

    def process(self, amount: float) -> PaymentResult:
        fee = self._fee.calculate_fee(amount)
        total = amount + fee
        charge_result = self._charger.charge(total)
        receipt = self._receipt.generate_receipt(total)
        return PaymentResult(charge_result=charge_result, receipt=receipt)