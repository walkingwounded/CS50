###pytest for working Lab
import pytest
from working import convert


def main():
    test_convert_format()
    test_convert_str()
    test_convert_min()


def test_convert_format():
    assert convert('9:00 AM to 5:00 PM') == "09:00 to 17:00"
    assert convert('9 AM to 5 PM') == "09:00 to 17:00"
    with pytest.raises(ValueError):
        convert('9 AM - 5 PM')


def test_convert_str():
    with pytest.raises(ValueError):
        convert('cat AM to cat PM')

def test_convert_min():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')

if __name__ == "__main__":
    main()



