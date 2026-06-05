"""Facade comparison: provides one simple entry point into a subsystem."""


class CheckoutFacade:
    def __init__(self, inventory, payment, shipping, email):
        self.inventory = inventory
        self.payment = payment
        self.shipping = shipping
        self.email = email

    def complete_order(self, cart, payment_details) -> None:
        self.inventory.reserve(cart)
        self.payment.charge(payment_details)
        self.shipping.schedule(cart)
        self.email.send_confirmation()
