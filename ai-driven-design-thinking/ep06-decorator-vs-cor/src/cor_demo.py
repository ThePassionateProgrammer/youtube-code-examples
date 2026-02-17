from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Optional

from .domain import PaymentRequest, ValidationContext


class Handler(Protocol):
    def set_next(self, nxt: "Handler") -> "Handler":
        ...

    def validate(self, ctx: ValidationContext) -> ValidationContext:
        ...


@dataclass
class BaseHandler:
    """
    CoR composition lives HERE (the diamond at the abstract/base level).
    This is literally a linked structure: each handler points to the next.
    """
    _next: Optional["BaseHandler"] = None

    def set_next(self, nxt: "BaseHandler") -> "BaseHandler":
        self._next = nxt
        return nxt

    # Two-method shape you called out (6:24):
    def should_handle(self, ctx: ValidationContext) -> bool:
        return True

    def handle(self, ctx: ValidationContext) -> None:
        # Default: do nothing
        return

    def validate(self, ctx: ValidationContext) -> ValidationContext:
        # Local decision lives HERE.
        if self.should_handle(ctx):  # (6:58) zoom on this conditional
            self.handle(ctx)

        # This is where the node decides to continue/bail.
        return self._continue_or_bail(ctx)

    def _continue_or_bail(self, ctx: ValidationContext) -> ValidationContext:
        # Default policy: continue
        if self._next is None:
            return ctx
        return self._next.validate(ctx)


@dataclass
class AmountPositive(BaseHandler):
    def should_handle(self, ctx: ValidationContext) -> bool:
        return True

    def handle(self, ctx: ValidationContext) -> None:
        ctx.trace.append("AmountPositive")
        if ctx.request.amount_cents <= 0:
            ctx.add_error("amount must be positive")


@dataclass
class CountryAllowed(BaseHandler):
    allowed: set[str]

    def should_handle(self, ctx: ValidationContext) -> bool:
        # Conditional is local and context-sensitive (zoom here too if you want)
        return True

    def handle(self, ctx: ValidationContext) -> None:
        ctx.trace.append("CountryAllowed")
        if ctx.request.country not in self.allowed:
            ctx.add_error(f"country not allowed: {ctx.request.country}")


@dataclass
class FraudCheck(BaseHandler):
    def should_handle(self, ctx: ValidationContext) -> bool:
        # (6:58) This is the one you can zoom hard on.
        # Local decision. Could depend on request + prior outcomes.
        return ctx.request.amount_cents >= 5000

    def handle(self, ctx: ValidationContext) -> None:
        ctx.trace.append("FraudCheck")
        # Deterministic demo rule:
        if ctx.request.user_id.startswith("fraud-"):
            ctx.add_error("fraud suspected")


# --- Two policies for 8:02: fail fast vs collect all ---

@dataclass
class FailFastMixin:
    def _continue_or_bail(self, ctx: ValidationContext) -> ValidationContext:
        # Bail early if any error appears
        if not ctx.ok:
            ctx.trace.append("BAIL_EARLY")
            return ctx
        if self._next is None:
            return ctx
        return self._next.validate(ctx)


@dataclass
class CollectAllMixin:
    def _continue_or_bail(self, ctx: ValidationContext) -> ValidationContext:
        # Always continue; collect all errors
        if self._next is None:
            return ctx
        return self._next.validate(ctx)


@dataclass
class FailFastAmountPositive(FailFastMixin, AmountPositive):
    pass


@dataclass
class FailFastCountryAllowed(FailFastMixin, CountryAllowed):
    pass


@dataclass
class FailFastFraudCheck(FailFastMixin, FraudCheck):
    pass


@dataclass
class CollectAllAmountPositive(CollectAllMixin, AmountPositive):
    pass


@dataclass
class CollectAllCountryAllowed(CollectAllMixin, CountryAllowed):
    pass


@dataclass
class CollectAllFraudCheck(CollectAllMixin, FraudCheck):
    pass


class ChainFactory:
    """
    Key narration beat (6:10):
    'CoR factory is intentionally boring—no conditionals—just assembles a sequence.'
    """
    @staticmethod
    def build_fail_fast() -> BaseHandler:
        h1 = FailFastAmountPositive()
        h2 = FailFastCountryAllowed(allowed={"US", "CA"})
        h3 = FailFastFraudCheck()
        h1.set_next(h2).set_next(h3)
        return h1

    @staticmethod
    def build_collect_all() -> BaseHandler:
        h1 = CollectAllAmountPositive()
        h2 = CollectAllCountryAllowed(allowed={"US", "CA"})
        h3 = CollectAllFraudCheck()

        h1.set_next(h2).set_next(h3)
        return h1

def demo_chain_fail_fast(req: PaymentRequest) -> ValidationContext:
    chain = ChainFactory.build_fail_fast()
    ctx = ValidationContext(request=req)
    return chain.validate(ctx)

def demo_chain_collect_all(req: PaymentRequest) -> ValidationContext:
    chain = ChainFactory.build_collect_all()
    ctx = ValidationContext(request=req)
    return chain.validate(ctx)