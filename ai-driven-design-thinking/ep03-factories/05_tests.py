from _02_pipeline_v1_strategy_only import PaymentPipelineV1
from _04_pipeline_v2_factory_only import PaymentPipelineV2
from _01_strategies import (
    StripeFeeStrategy, PaypalChargeStrategy, AcmePayReceiptStrategy
)
from _03_factories import StripeComponentsFactory, PaypalComponentsFactory, AcmePayComponentsFactory


def test_v1_allows_invalid_combinations():
    pipeline = PaymentPipelineV1(
        fee=StripeFeeStrategy(),
        charger=PaypalChargeStrategy(),    # nonsense mix
        receipt=AcmePayReceiptStrategy(),  # nonsense mix
    )
    result = pipeline.process(100.0)
    assert result.charge_result["status"] in ("ok", "declined")


def test_v2_stripe_family_is_coherent():
    pipeline = PaymentPipelineV2(StripeComponentsFactory())
    result = pipeline.process(100.0)
    assert result.charge_result["provider"] == "stripe"
    assert "Stripe receipt" in result.receipt


def test_add_acmepay_family_by_adding_factory():
    pipeline = PaymentPipelineV2(AcmePayComponentsFactory())
    ok = pipeline.process(200.0)
    assert ok.charge_result["status"] == "ok"
    assert ok.charge_result["provider"] == "acmepay"
