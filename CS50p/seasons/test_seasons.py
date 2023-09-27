#testing seasons week8-1


from seasons import get_birthdate, convert_words
import datetime
import pytest

def main():
    test_get_birthdate()
    test_convert_words()

def test_get_birthdate():
    with pytest.raises(SystemExit):
        get_birthdate('October 21, 1988')
    with pytest.raises(SystemExit):
        get_birthdate('1988-13-01')
    with pytest.raises(SystemExit):
        get_birthdate('1988-01-32')
    assert get_birthdate('1988-10-21') == datetime.date(1988, 10, 21)


def test_convert_words():
    assert convert_words("0") == 'Zero'
    assert convert_words("100") == 'One hundred'



if __name__ == "__main__":
    main()