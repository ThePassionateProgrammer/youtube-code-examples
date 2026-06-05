from before_example import (
    EventLog as BeforeEventLog,
    Total,
    PaymentOptions,
    ShippingOptions,
    SubmitButton,
    ReceiptPreview,
    CouponField as BeforeCouponField,
    PaymentField as BeforePaymentField,
)
from after_example import EventLog, CheckoutMediator


def test_before_coupon_field_coordinates_too_many_peers():
    log = BeforeEventLog()
    coupon = BeforeCouponField(
        total=Total(log),
        payment_options=PaymentOptions(log),
        shipping_options=ShippingOptions(log),
        submit_button=SubmitButton(log),
    )

    coupon.changed()

    assert log.events == [
        "total recalculated",
        "payment options refreshed",
        "shipping options updated",
        "submit button validated",
    ]


def test_before_payment_field_has_different_coordination_rules():
    log = BeforeEventLog()
    payment = BeforePaymentField(
        submit_button=SubmitButton(log),
        receipt_preview=ReceiptPreview(log),
    )

    payment.changed()

    assert log.events == [
        "submit button validated",
        "receipt preview updated",
    ]


def test_mediator_coordinates_coupon_change():
    log = EventLog()
    checkout = CheckoutMediator(log)

    checkout.coupon_field.changed()

    assert log.events == [
        "total recalculated",
        "payment options refreshed",
        "shipping options updated",
        "submit button validated",
    ]


def test_mediator_coordinates_payment_change():
    log = EventLog()
    checkout = CheckoutMediator(log)

    checkout.payment_field.changed()

    assert log.events == [
        "submit button validated",
        "receipt preview updated",
    ]


def test_components_only_know_the_mediator():
    log = EventLog()
    checkout = CheckoutMediator(log)

    assert checkout.coupon_field.mediator is checkout
    assert not hasattr(checkout.coupon_field, "total")
    assert not hasattr(checkout.coupon_field, "payment_options")
    assert not hasattr(checkout.coupon_field, "shipping_options")
