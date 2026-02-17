from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class Order:
    """Tiny domain object used throughout the playlist."""
    base_price: float
    is_vip: bool
    region: str  # e.g. "local" or "remote"
    payment_valid: bool = True
