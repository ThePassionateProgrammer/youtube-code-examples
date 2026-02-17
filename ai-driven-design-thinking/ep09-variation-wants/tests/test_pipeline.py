from factory import Policy, run_payment, build_payment_pipeline
from good_pipeline import PaymentContext


def test_pipeline_happy_path_logs_and_charges():
    policy = Policy(enable_logging=True, require_fraud_check=True, environment="prod")
    ctx = run_payment("u1", 1000, policy)
    assert ctx.approved is True
    assert ctx.charged is True
    assert "charged:stripe" in ctx.events
    assert any(e.startswith("log:") for e in ctx.events)


def test_pipeline_rejects_invalid_amount_and_bails():
    policy = Policy(enable_logging=True, require_fraud_check=True, environment="prod")
    ctx = run_payment("u1", 0, policy)
    assert ctx.approved is False
    assert ctx.charged is False
    assert "rejected:invalid_amount" in ctx.events
    assert "bail:not_approved" in ctx.events


def test_pipeline_fraud_rejects_large_amount_in_prod():
    policy = Policy(enable_logging=False, require_fraud_check=True, environment="prod")
    ctx = run_payment("u1", 100_000, policy)
    assert ctx.approved is False
    assert ctx.charged is False
    assert "rejected:fraud" in ctx.events


def test_build_pipeline_runs_in_expected_order():
    policy = Policy(enable_logging=True, require_fraud_check=True, environment="prod")
    pipeline = build_payment_pipeline(policy)
    ctx = PaymentContext(user_id="u1", amount_cents=1000, environment="prod")
    ctx = pipeline.run(ctx)
    assert ctx.events.index("ok:amount") < ctx.events.index("charged:stripe")
