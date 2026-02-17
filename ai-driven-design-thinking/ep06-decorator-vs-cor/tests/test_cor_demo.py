from src.domain import PaymentRequest
from src.cor_demo import demo_chain_fail_fast, demo_chain_collect_all


def test_cor_fail_fast_bails_early():
    req = PaymentRequest(user_id="u-1", amount_cents=-10, country="US")
    ctx = demo_chain_fail_fast(req)

    assert ctx.ok is False
    assert "amount must be positive" in ctx.errors
    # It should bail early before later handlers run
    assert "BAIL_EARLY" in ctx.trace
    assert "CountryAllowed" not in ctx.trace


def test_cor_collect_all_runs_all_handlers():
    req = PaymentRequest(user_id="fraud-7", amount_cents=-10, country="FR")
    ctx = demo_chain_collect_all(req)

    assert ctx.ok is False
    # Collect all: multiple errors
    assert "amount must be positive" in ctx.errors
    assert "country not allowed: FR" in ctx.errors
    # FraudCheck runs only if amount >= 5000, so it should NOT run here:
    assert "FraudCheck" not in ctx.trace


def test_cor_fraud_check_runs_when_threshold_met():
    req = PaymentRequest(user_id="fraud-7", amount_cents=9000, country="US")
    ctx = demo_chain_fail_fast(req)

    assert ctx.ok is False
    assert "fraud suspected" in ctx.errors
    assert "FraudCheck" in ctx.trace