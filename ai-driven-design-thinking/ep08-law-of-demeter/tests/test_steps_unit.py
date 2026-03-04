from app.pipeline import PaymentContext
from app.steps import ValidateAmountStep, FraudCheckStep, LogStep, ChargeCardStep

def test_validate_amount_declines_zero():
    ctx = PaymentContext(amount_cents=0, card_token="tok")
    ValidateAmountStep().run(ctx)
    assert ctx.declined_reason == "INVALID_AMOUNT"

def test_fraud_check_declines_large_non_vip():
    ctx = PaymentContext(amount_cents=8000, card_token="tok", is_vip=False)
    FraudCheckStep().run(ctx)
    assert ctx.declined_reason == "FRAUD_SUSPECTED"

def test_log_step_appends_message():
    ctx = PaymentContext(amount_cents=1000, card_token="tok")
    LogStep("hello").run(ctx)
    assert ctx.logs == ["hello"]

def test_charge_sets_charged_when_not_declined():
    ctx = PaymentContext(amount_cents=1000, card_token="tok")
    ChargeCardStep().run(ctx)
    assert ctx.charged is True
