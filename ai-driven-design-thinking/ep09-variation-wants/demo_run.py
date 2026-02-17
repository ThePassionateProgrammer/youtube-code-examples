from factory import Policy, run_payment

if __name__ == "__main__":
    policy = Policy(enable_logging=True, require_fraud_check=True, environment="prod")
    ctx = run_payment("u1", 12_34, policy)
    print("approved:", ctx.approved)
    print("charged:", ctx.charged)
    print("events:")
    for e in ctx.events:
        print(" -", e)
