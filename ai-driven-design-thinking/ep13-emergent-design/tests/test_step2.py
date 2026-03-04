from emergent_discounts.customer import Customer
from emergent_discounts.order import Order
from steps.step2_processor_factory import DiscountFactory

def test_step2_factory_creates_processor():
    processor = DiscountFactory().create()
    assert processor.__class__.__name__ == "DiscountProcessor"

def test_step2_employee_discount_is_30_percent():
    processor = DiscountFactory().create()
    order = Order(customer=Customer(id="c1", is_employee=True), subtotal_cents=10_00)
    assert processor.process(order) == 300

def test_step2_vip_discount_is_20_percent():
    processor = DiscountFactory().create()
    order = Order(customer=Customer(id="c2", is_vip=True), subtotal_cents=10_00)
    assert processor.process(order) == 200
