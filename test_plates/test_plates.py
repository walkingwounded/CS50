### Unit test for plates, here we go again!
from plates import is_valid



def main():
    test_plates_ending()
    test_plates_symbols()
    test_plates_starting()
    test_plates_length()
    test_plates_zero()
    test_plates_alphanumeric()

def test_plates_ending():
    assert is_valid('CS50P') == False
    assert is_valid('CS501') == True

def test_plates_symbols():
    assert is_valid('%') == False
    assert is_valid('!') == False
    assert is_valid('@') == False
    assert is_valid('.') == False
    assert is_valid(',') == False
    assert is_valid('CS50,') == False
    assert is_valid('CS.50') == False

def test_plates_starting():
    assert is_valid('0000') == False
    assert is_valid('CS50') == True

def test_plates_length():
    assert is_valid('CS50000') == False

def test_plates_zero():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False

def test_plates_alphanumeric():
    assert is_valid('ABCD') == True
    assert is_valid('A!CD') == False
    assert is_valid('1234') == False
    assert is_valid('C5S0') == False

if __name__ == "__main__":
    main()