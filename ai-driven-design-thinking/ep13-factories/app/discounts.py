class StandardDiscount:
    def apply(self, total: float) -> float:
        return total

class VipDiscount:
    def apply(self, total: float) -> float:
        return total * 0.90

class SeasonalDiscount:
    def apply(self, total: float) -> float:
        return total * 0.95
