##testing twttr from week2
from twttr import shorten

def main():
    test_vowel()
    test_upper()
    test_numeric()
    test_punctuation()
    test_none()

def test_vowel():
    assert shorten('test') == 'tst'

def test_upper():
    assert shorten('TEST') == 'TST'

def test_numeric():
    assert shorten('test 123') == 'tst 123'

def test_punctuation():
    assert shorten('test!?') == 'tst!?'

def test_none():
    assert shorten('') == ''

if __name__ == "__main__":
    main()
