import pytest



def test_receive_input():
    import histogram_maker_01 as histogram
    hx, hy, vx, vy = 140, 190, 1, 8
    result = histogram.set_table_bounds(hx, hy, vx, vy)
    assert isinstance(result, object)
