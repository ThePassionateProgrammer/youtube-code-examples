from emergent_discounts.customer import Customer
from emergent_discounts.order import Order
from emergent_discounts.factory import DiscountStrategyFactory
from emergent_discounts.checkout import CheckoutService

def test_step3_total_after_discount():
    checkout = CheckoutService(DiscountStrategyFactory())

    vip = Order(customer=Customer(id="c1", is_vip=True), subtotal_cents=10_00)
    assert checkout.total_after_discount_cents(vip) == 800

    employee = Order(customer=Customer(id="c2", is_employee=True), subtotal_cents=10_00)
    assert checkout.total_after_discount_cents(employee) == 700

    seasonal = Order(customer=Customer(id="c3"), subtotal_cents=10_00, is_seasonal_promo=True)
    assert checkout.total_after_discount_cents(seasonal) == 900

    none = Order(customer=Customer(id="c4"), subtotal_cents=10_00)
    assert checkout.total_after_discount_cents(none) == 1000
