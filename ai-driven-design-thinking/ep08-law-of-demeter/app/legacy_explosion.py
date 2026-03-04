from __future__ import annotations
from typing import Iterable, List
# Optional behaviors that tempt subclass explosion
EXAMPLE_OPTIONS = ["LOGGING", "FRAUD_CHECK", "RETRY", "EXTRA_VALIDATION", "VIP_RULES"]

def count_combinations(options: Iterable[str]) -> int:
    # each option can be ON/OFF => 2^n combinations
    options = list(options)
    return 2 ** len(options)

def generate_subclass_names(options: List[str], base: str = "PaymentFlow") -> List[str]:
    names: List[str] = []
    n = len(options)
    for mask in range(2 ** n):
        chosen = [options[i] for i in range(n) if (mask & (1 << i))]
        suffix = "".join([f"_With{opt.title().replace('_', '')}" for opt in chosen]) or "_Plain"
        names.append(f"{base}{suffix}")
    return names

def main() -> None:
    print(f"{len(EXAMPLE_OPTIONS)} options => {count_combinations(EXAMPLE_OPTIONS)} combinations\n")
    for name in generate_subclass_names(EXAMPLE_OPTIONS)[:12]:
        print(name)
    print("...")

if __name__ == "__main__":
    main()
