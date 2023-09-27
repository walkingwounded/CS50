###Working 9 to 5 ~
import re
import sys


def main():
    print(convert(input("Hours: ").strip().lower()))


def convert(s):
##search and filter and group
    if hours := re.search(r"^([0-9][0-2]?):?([0-5]?[0-9]?)(?: (am|pm)) to ([0-9][0-9]?):?([0-5]?[0-9]?)(?: (pm|am))", s, re.IGNORECASE):

###create variables
        starthr, startmin, endhr, endmin = "","","",""

###check for != "12 PM" by using re.group
        if "pm" in hours.group(3) and hours.group(1) != "12":
            starthr, startmin = hours.group(1), hours.group(2)
            starthr = int(starthr)+12
        else:
            starthr, startmin = hours.group(1), hours.group(2)
            starthr = int(starthr)
        if "pm" in hours.group(6) and hours.group(1) != "12":
            endhr, endmin = hours.group(4), hours.group(5)
            endhr = int(endhr)+12
        else:
            endhr, endmin = hours.group(4), hours.group(5)
            endhr = int(endhr)

###check for == "12 AM" by using re.group
        if "am" in hours.group(3) and hours.group(1) == "12":
            starthr = 0
        if "am" in hours.group(6) and hours.group(4) == "12":
            endhr = 0

###check for minutes
        if startmin == " ":
            startmin = 0
        if endmin == " ":
            endmin = 0

###return value
        return(f"{starthr:02}:{startmin:02} to {endhr:02}:{endmin:02}")

###else-if re.search and does not match, raise ValueError
    else:
        raise ValueError


if __name__ == "__main__":
    main()





### I am terrible at coding, i think there is definitely a better way to code than this 4hrs work....

# def convert(s):
#     # start, end = s.split("to")
#     if hours := re.search(r"^([0-9][0-2]?):?([0-5]?[0-9]?)(?: (am|pm)) to ([0-9][0-9]?):?([0-5]?[0-9]?)(?: (pm|am))", s, re.IGNORECASE):
#     #print(hours)
#         starthr, startmin, endhr, endmin = "","","",""
#         if "pm" in hours.group(3) and hours.group(1) != "12":
#             starthr, startmin = hours.group(1), hours.group(2)
#             starthr = int(starthr)+12
#         else:
#             starthr, startmin = hours.group(1), hours.group(2)
#             starthr = int(starthr)
#         if "pm" in hours.group(6) and hours.group(1) != "12":
#             endhr, endmin = hours.group(4), hours.group(5)
#             endhr = int(endhr)+12
#         else:
#             endhr, endmin = hours.group(4), hours.group(5)
#             endhr = int(endhr)
#         if "am" in hours.group(3) and hours.group(1) == "12":
#             starthr = 0
#         if "am" in hours.group(6) and hours.group(4) == "12":
#             endhr = 0
#         if startmin == " ":
#             startmin = 0
#         # else:
#         #     int(startmin)
#         if endmin == " ":
#             endmin = 0
#         # if starthr == 24:
#         #     starthr = 0
#         # if endhr == 24:
#         #     endhr = 0
#         # else:
#         #     int(endmin)
#         # if int(startmin) > 59 or int(endmin) > 59:
#         #     raise ValueError
#         # if startmin
#         return(f"{starthr:02}:{startmin:02} to {endhr:02}:{endmin:02}")
#         # else:
#         #     starthr, startmin = hours.group(1), hours.group(2)
#         #     print(f"{starthr}:{startmin} to {hours.group(3)}")
#         #     # return(hours.group(1).strip(), hours.group(3).strip())
#     else:
#         raise ValueError
