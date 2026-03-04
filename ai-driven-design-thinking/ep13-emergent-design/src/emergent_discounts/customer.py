from dataclasses import dataclass

@dataclass(frozen=True)
class Customer:
    id: str
    is_vip: bool = False
    is_employee: bool = False
