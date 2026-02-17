from domain import Order, User
from factory import PricingPolicyFactory
from checkout import checkout

def demo():
    factory = PricingPolicyFactory()
    samples = [
        (User(is_vip=False), "dev", Order(120)),
        (User(is_vip=True), "prod", Order(120)),
        (User(is_vip=False), "prod", Order(220)),
        (User(is_vip=True), "prod", Order(160)),
    ]
    for user, env, order in samples:
        policy = factory.create(user=user, env=env, order_total=order.total)
        total = checkout(order, policy)
        print(f"user.vip={user.is_vip} env={env} order={order.total} -> total={total:.2f}")

if __name__ == "__main__":
    demo()
