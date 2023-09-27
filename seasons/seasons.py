######Week 8 Lab - seasons of love!
### YYYY-MM-DD

import sys
import re
from datetime import date
from datetime import timedelta
import datetime
import inflect


def main():
    birthdate = get_birthdate(input("Date of Birth: "))
    today = datetime.date.today()
    delta_mins = (today - birthdate) / timedelta(minutes=1)
    print(convert_words(delta_mins),"minutes")


def get_birthdate(dob):
    try:
        dob = date.fromisoformat(dob)
        return dob
    except(ValueError):
            sys.exit("Invalid date")

def convert_words(a):
    a = inflect.engine().number_to_words(int(a), andword="")
    return a.capitalize()


if __name__ == "__main__":
    main()



# def get_birthdate(dob):
#     if birthdate := re.search(r"^([1-2][0-9][0-9][0-9])-([0-1][0-9])-([0-3][0-9])$", dob):
#             if birthdate.group(2) > 12:
#                 sys.exit("Invalid date")
#             elif birthdate.group()
#         else:
#             raise(ValueError)


###### try # 2
# class Birthdays:
#     def __init__(self, dob, delta):
#         try:
#             self.dob = date.fromisoformat(dob)
#             self.delta = delta
#         except(ValueError):
#             sys.exit("Invalid date")

#     def __str__(self):
#         return f"{self.dob},{self.today}"

#     def __sub__(self, today):
#         delta = self.dob - today.dob
#         return Birthdays(difference)

# def main():
#     birthdate = Birthdays(input("Date of Birth: "),date.today(),0)
#     today = date.today()
#     timedelta = birthdate - today
#     print(timedelta)




#### try #3
# class Birthdate:
#     def __init__(self, dob):
#         try:
#             self.dob = str(date.fromisoformat(dob))
#         except(ValueError):
#             sys.exit("Invalid date")

#     def __str__(self):
#         return(self.dob)
#         ##last error. returned non.str
#         ### probably need to do the check somewhere else
#         #### look into setter and getter



#     @property
#     def dob(self):
#         return self._dob

#     @dob.setter
#     def dob(self, dob):
#         if not dob:
#             sys.exit("Invalid date")
#         self._dob = dob

#     @classmethod
#     def get(cls):
#         dob = input("Date of Birth: ")
#         return cls(dob)



# def main():
#     birthdate = Birthdate.get()
#     # today = datetime.date.today
#     timedelta = birthdate - today
#     # # print(timedelta)
#     print(birthdate)

# def __sub__(a, b):