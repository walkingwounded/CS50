###Testing my Random Gym Workout Challenge Generator


from project import get_user, interpret_bmi, bmi, random_workout, intensity
import pytest


def main():
    test_get_user()
    test_interpret_bmi()
    test_bmi()
    test_random_workout()
    test_intensity()

def test_bmi():
    assert bmi(150, 50) == 22.22

# def test_get_user():
#     assert type(get_user('name',)) == list

def test_interpret_bmi():
    assert interpret_bmi(15) == 'Underweight'
    assert interpret_bmi(23) == 'Healthy Weight'
    assert interpret_bmi(25) == 'Overweight'
    assert interpret_bmi(35) == 'Obese'

def test_intensity():
    assert type(intensity(random_workout(),'M','Obese')) == float



def test_random_workout():
    assert type(random_workout()) == dict
    assert type(random_workout()) != list