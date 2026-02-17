from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class PaymentRequest:
    user_id: str
    amount_cents: int
    currency: str = "USD"
    country: str = "US"
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class PaymentResult:
    ok: bool
    message: str
    trace: list[str] = field(default_factory=list)


@dataclass
class ValidationContext:
    request: PaymentRequest
    errors: list[str] = field(default_factory=list)
    trace: list[str] = field(default_factory=list)

    def add_error(self, msg: str) -> None:
        self.errors.append(msg)

    @property
    def ok(self) -> bool:
        return len(self.errors) == 0