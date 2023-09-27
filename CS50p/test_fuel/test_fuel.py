## Lab for Unit Test. It's refuel time!
from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_convert_value()
    test_convert_zero()
    test_gauge()



def test_convert():
    assert convert('1/2') == 50
    assert convert('1/1') == 100

def test_convert_zero():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_convert_value():
    with pytest.raises(ValueError):
        convert('cat/dog')

def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(2) == '2%'
    assert gauge(99) == 'F'


if __name__ == "__main__":
    main()