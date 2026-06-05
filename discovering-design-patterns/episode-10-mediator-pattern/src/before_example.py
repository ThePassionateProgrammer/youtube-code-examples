"""Before: relationship coordination is scattered across UI components.

This intentionally shows the smell: fields know too much about peers.
Run: python src/before_example.py
"""

from dataclasses import dataclass, field


@dataclass
class EventLog:
    events: list[str] = field(default_factory=list)

    def record(self, message: str) -> None:
        self.events.append(message)


class Total:
    def __init__(self, log: EventLog):
        self.log = log

    def recalculate(self) -> None:
        self.log.record("total recalculated")


class PaymentOptions:
    def __init__(self, log: EventLog):
        self.log = log

    def refresh(self) -> None:
        self.log.record("payment options refreshed")


class ShippingOptions:
    def __init__(self, log: EventLog):
        self.log = log

    def update(self) -> None:
        self.log.record("shipping options updated")


class SubmitButton:
    def __init__(self, log: EventLog):
        self.log = log

    def validate(self) -> None:
        self.log.record("submit button validated")


class ReceiptPreview:
    def __init__(self, log: EventLog):
        self.log = log

    def update(self) -> None:
        self.log.record("receipt preview updated")

class CouponField:
    def __init__(
        self,
        total: Total,
        payment_options: PaymentOptions,
        shipping_options: ShippingOptions,
        submit_button: SubmitButton,
    ):
        self.total = total
        self.payment_options = payment_options
        self.shipping_options = shipping_options
        self.submit_button = submit_button

    def changed(self) -> None:
        self.total.recalculate()
        self.payment_options.refresh()
        self.shipping_options.update()
        self.submit_button.validate()

class ShippingField:
    def __init__(
        self,
        total: Total,
        payment_options: PaymentOptions,
        submit_button: SubmitButton,
    ):
        self.total = total
        self.payment_options = payment_options
        self.submit_button = submit_button

    def changed(self) -> None:
        self.total.recalculate()
        self.payment_options.refresh()
        self.submit_button.validate()


class PaymentField:
    def __init__(self, submit_button: SubmitButton, receipt_preview: ReceiptPreview):
        self.submit_button = submit_button
        self.receipt_preview = receipt_preview

    def changed(self) -> None:
        self.submit_button.validate()
        self.receipt_preview.update()


if __name__ == "__main__":
    log = EventLog()
    total = Total(log)
    payment = PaymentOptions(log)
    shipping = ShippingOptions(log)
    submit = SubmitButton(log)
    receipt = ReceiptPreview(log)

    coupon = CouponField(total, payment, shipping, submit)
    coupon.changed()

    print("\n".join(log.events))
