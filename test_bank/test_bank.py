#### Lab: unit test for bank, dubbed Bacck to the Bank (>.<)"
from bank import value

def main():
    test_greeting_0()
    test_greeting_20()
    test_greeting_100()
    test_greeting_blank()

def test_greeting_0():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0

def test_greeting_20():
    assert value("happy") == 20
    assert value("Happy") == 20
    assert value("HAPPY ") == 20

def test_greeting_100():
    assert value("What's up!") == 100
    assert value("WHADDA") == 100

def test_greeting_blank():
    assert value('') == 100

if __name__ == "__main__":
    main()