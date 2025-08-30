from open_webui.utils.math import cube


def test_cube_positive():
    assert cube(3) == 27


def test_cube_negative():
    assert cube(-2) == -8


def test_cube_zero():
    assert cube(0) == 0
