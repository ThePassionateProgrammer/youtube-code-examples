"""After: Mediator concentrates coordination in one collaboration boundary.

Run: python src/after_example.py
"""

from dataclasses import dataclass, field
from typing import Protocol


@dataclass
class EventLog:
    events: list[str] = field(default_factory=list)

    def record(self, message: str) -> None:
        self.events.append(message)

class Component(Protocol):
    def changed(self) -> None:
        ...

class CheckoutComponent:
    def __init__(self, mediator: "CheckoutMediator"):
        self.mediator = mediator

    def changed(self) -> None:
        self.mediator.changed(self)

class CouponField(CheckoutComponent):
    pass

class ShippingField(CheckoutComponent):
    pass

class PaymentField(CheckoutComponent):
    pass

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


class CheckoutMediator:
    def __init__(self, log: EventLog):
        self.total = Total(log)
        self.payment_options = PaymentOptions(log)
        self.shipping_options = ShippingOptions(log)
        self.submit_button = SubmitButton(log)
        self.receipt_preview = ReceiptPreview(log)

        self.coupon_field = CouponField(self)
        self.shipping_field = ShippingField(self)
        self.payment_field = PaymentField(self)

    def changed(self, component: CheckoutComponent) -> None:
        if component is self.coupon_field:
            self._coupon_changed()
        elif component is self.shipping_field:
            self._shipping_changed()
        elif component is self.payment_field:
            self._payment_changed()
        else:
            raise ValueError("Unknown checkout component")

    def _coupon_changed(self) -> None:
        self.total.recalculate()
        self.payment_options.refresh()
        self.shipping_options.update()
        self.submit_button.validate()

    def _shipping_changed(self) -> None:
        self.total.recalculate()
        self.payment_options.refresh()
        self.submit_button.validate()

    def _payment_changed(self) -> None:
        self.submit_button.validate()
        self.receipt_preview.update()

if __name__ == "__main__":
    log = EventLog()
    checkout = CheckoutMediator(log)

    checkout.coupon_field.changed()

    print("\n".join(log.events))
