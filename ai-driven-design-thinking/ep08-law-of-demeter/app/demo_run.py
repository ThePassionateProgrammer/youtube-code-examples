from __future__ import annotations
from .factory import PaymentConfig, run_payment

def main() -> None:
    cfg = PaymentConfig(enable_logging=True, enable_fraud_check=True, enable_retry=False)
    ctx = run_payment(6500, is_vip=False, config=cfg)
    print("charged:", ctx.charged, "declined:", ctx.declined_reason, "logs:", ctx.logs)

if __name__ == "__main__":
    main()
