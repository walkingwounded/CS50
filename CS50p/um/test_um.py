###pytest um.. for um... lab
import pytest
from um import count


def main():
    test_count_type()
    test_count_sentence()
    test_count_na()


def test_count_type():
    assert count('um') == 1
    assert count('um.') == 1
    assert count('Um') == 1
    assert count('UM') == 1
    assert count('UMM') == 0


def test_count_sentence():
    assert count('hello, um, world, um') == 2
    assert count('Um.. How are you?') == 1
    assert count('Yummy!') == 0
    assert count('Um.. Umi means "Sea" in Japanese') == 1

def test_count_na():
    assert count('123um456') == 0


if __name__ == "__main__":
    main()



