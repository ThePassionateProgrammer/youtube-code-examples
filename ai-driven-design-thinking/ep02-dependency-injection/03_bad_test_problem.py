# WHY THIS IS A PROBLEM:
# With no seam, a "unit test" can't isolate PaymentService.
# It would either:
#   - hit Stripe (network),
#   - require global patching/monkeypatching,
#   - or become an integration test.

from 01_bad_no_seam import PaymentService

def test_charge_is_hard_without_a_seam():
    service = PaymentService()

    # ❌ This is not a unit test anymore:
    # service.charge(50.00) would call StripeClient (network)
    #
    # Your choices become:
    #   - don't test it
    #   - patch StripeClient globally
    #   - accept slow/flaky tests
    #
    # The real fix is structural: add a seam.
    assert True