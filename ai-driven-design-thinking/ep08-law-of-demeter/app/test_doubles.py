class SpyGateway:
    """Test double that records calls."""
    def __init__(self) -> None:
        self.calls: list[tuple[str,int]] = []

    def charge(self, card_number: str, amount_cents: int) -> str:
        self.calls.append((card_number, amount_cents))
        return "ok"
