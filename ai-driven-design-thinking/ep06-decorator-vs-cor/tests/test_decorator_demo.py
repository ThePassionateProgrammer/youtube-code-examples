from src.decorator_demo import DecoratorConfig, demo_decorator


def test_decorator_factory_builds_predictable_stack():
    config = DecoratorConfig(
        env="prod",
        enable_logging=True,
        enable_metrics=True,
        enable_retry=True,
        user_tier="pro",
    )
    result = demo_decorator(config)

    assert result.ok is True
    # Predictable: every layer participates once built.
    # Order here reflects how we wrapped (outermost inserts first).
    assert result.trace[0].startswith("retry:")
    assert result.trace[1] == "log:begin" or result.trace[1] == "metrics:start"
    assert "stripe_charge(1200 USD)" in result.trace
    assert result.trace[-1] in {"log:end", "metrics:stop"}