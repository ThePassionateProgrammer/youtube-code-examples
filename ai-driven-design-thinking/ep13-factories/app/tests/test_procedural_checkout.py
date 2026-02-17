from checkout_procedural import checkout, Order, User

def test_procedural_checkout_vip_prod():
    total = checkout(Order(100), User(is_vip=True), env="prod")
    assert total == 0.90 * 100 + 15.0
