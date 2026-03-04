from emergent_discounts.customer import Customer
from emergent_discounts.order import Order
from steps.step1_hardcoded import discount_cents

def test_step1_vip_gets_20_percent_off():
    order = Order(customer=Customer(id="c1", is_vip=True), subtotal_cents=10_00)
    assert discount_cents(order) == 200

def test_step1_non_vip_gets_no_discount():
    order = Order(customer=Customer(id="c2"), subtotal_cents=10_00)
    assert discount_cents(order) == 0
