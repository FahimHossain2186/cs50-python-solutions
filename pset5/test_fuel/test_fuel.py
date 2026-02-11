import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("0/1") == 0
    assert convert("1/2") == 50
    assert convert("3/3") == 100

    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("-1/3")
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ValueError):
        convert("4/-6")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(0)     == "E"
    assert gauge(1)     == "E"

    assert gauge(99)    == "F"
    assert gauge(100)   == "F"

    assert gauge(34)    == "34%"
    assert gauge(98)    == "98%"
    assert gauge(21)    == "21%"
    assert gauge(72)    == "72%"
