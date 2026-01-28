from __future__ import annotations
from dataclasses import dataclass
from _01_strategies import FeeStrategy, ChargeStrategy, ReceiptStrategy


@dataclass(frozen=True)
class PaymentResult:
    charge_result: dict
    receipt: str


class PaymentPipelineV1:
    """
    Strategy-only pipeline:
    - Very flexible
    - But allows invalid combinations
    """
    def __init__(
        self,
        fee: FeeStrategy,
        charger: ChargeStrategy,
        receipt: ReceiptStrategy,
    ):
        self._fee = fee
        self._charger = charger
        self._receipt = receipt

    def process(self, amount: float) -> PaymentResult:
        fee = self._fee.calculate_fee(amount)
        total = amount + fee
        charge_result = self._charger.charge(total)
        receipt = self._receipt.generate_receipt(total)
        return PaymentResult(charge_result=charge_result, receipt=receipt)
