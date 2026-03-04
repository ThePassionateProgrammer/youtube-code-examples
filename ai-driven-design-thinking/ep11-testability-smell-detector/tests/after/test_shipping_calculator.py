from src.after.shipping import ThresholdShipping, VipFreeShipping
from src.after.models import Customer


def test_threshold_shipping_free_over_threshold():
    ship = ThresholdShipping(base_shipping=7.99, free_threshold=100.0)
    assert ship.shipping_for(99.99, Customer("c", vip=False)) == 7.99
    assert ship.shipping_for(100.00, Customer("c", vip=False)) == 0.0


def test_vip_free_shipping_only_decides_for_vips():
    vip = VipFreeShipping(enabled=True)

    assert vip.shipping_for(10.0, Customer("vip", vip=True)) == 0.0

    result = vip.shipping_for(10.0, Customer("n", vip=False))
    assert result != result  # NaN check
