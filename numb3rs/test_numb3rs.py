### test numb3rs
import pytest
from numb3rs import validate


def main():
    test_validate_int()
    test_validate_str()


def test_validate_str():
    assert validate('dog') == False
    assert validate('1.') == False
    assert validate('1.1.') == False
    assert validate('1.1.1.') == False

def test_validate_int():
    assert validate('1.1.1.1') == True
    assert validate('255.255.255.255') == True
    assert validate('11.11.11.11') == True
    assert validate('256.256.256.256') == False
    assert validate('255.256.256.256') == False
    assert validate('255.255.999.999') == False
    assert validate('1.1.1.999') == False


if __name__ == "__main__":
    main()