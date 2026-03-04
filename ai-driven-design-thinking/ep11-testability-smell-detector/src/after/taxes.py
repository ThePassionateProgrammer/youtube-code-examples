from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TaxCalculator:
    rate: float = 0.08

    def tax_for(self, taxable_amount: float) -> float:
        return round(self.rate * taxable_amount, 2)
