from shared.order import Order
from simple_checkout.checkout import checkout_total as simple_total
from clever_checkout.factory import checkout_total as clever_total

def main():
    orders = [
        Order(base_price=100.0, is_vip=False, region="local", payment_valid=True),
        Order(base_price=100.0, is_vip=True, region="local", payment_valid=True),
        Order(base_price=100.0, is_vip=False, region="remote", payment_valid=True),
        Order(base_price=100.0, is_vip=True, region="remote", payment_valid=True),
    ]
    for o in orders:
        s = simple_total(o)
        c = clever_total(o, env="prod", enable_audit=True)
        print(o, "simple=", s, "clever=", c)

if __name__ == "__main__":
    main()
