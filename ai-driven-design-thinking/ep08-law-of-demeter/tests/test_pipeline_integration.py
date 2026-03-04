from app.factory import PaymentConfig, run_payment

def test_pipeline_charges_small_amount():
    cfg = PaymentConfig(enable_logging=False, enable_fraud_check=True, enable_retry=False)
    ctx = run_payment(1200, is_vip=False, config=cfg)
    assert ctx.charged is True
    assert ctx.declined_reason is None

def test_pipeline_declines_large_amount_for_non_vip():
    cfg = PaymentConfig(enable_logging=True, enable_fraud_check=True, enable_retry=False)
    ctx = run_payment(9900, is_vip=False, config=cfg)
    assert ctx.charged is False
    assert ctx.declined_reason == "FRAUD_SUSPECTED"
