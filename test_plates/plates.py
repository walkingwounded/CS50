#vanity plate lab


def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#is_valid check list. check for False till True
def is_valid(s):
#str length check
    if len(s) > 6 or len(s) < 2:
        return False
#check for digit in first 2 character
    if s[0:2].isalpha() == False:
        return False
#check for space and non-alphanumeric
    for op in s:
        if op in ('.','_','-','!','?',' '):
            return False
#check for first digit if it is a "0"
    first_zero = 0
    while first_zero < len(s):
        if s[first_zero].isalpha() == False:
            if s[first_zero] == '0':
                return False
            else:
                break
        first_zero += 1
#check for any digit in between alphabets.
## run in range of input > if variable is digit check next character onwards if they are also digit.
# If check returns false (not digit) -> return false
    for middle in range(len(s)):
        if s[middle].isdigit():
            if s[middle:].isdigit() == False:
                return False
    return True


if __name__ == "__main__":
    main()




##############backup for week2
# def main():
#     plate = input("Plate: ").upper()
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")

# #is_valid check list. check for False till True
# def is_valid(s):
# #str length check
#     if len(s) > 6 or len(s) < 2:
#         return False
# #check for digit in first 2 character
#     if s[0:2].isalpha() == False:
#         return False
# #check for space and non-alphanumeric
#     for op in s:
#         if op in ('.','_','-','!','?',' '):
#             return False
# #check for first digit if it is a "0"
#     first_zero = 0
#     while first_zero < len(s):
#         if s[first_zero].isalpha() == False:
#             if s[first_zero] == '0':
#                 return False
#             else:
#                 break
#         first_zero += 1
# #check for any digit in between alphabets.
# ## run in range of input > if variable is digit check next character onwards if they are also digit.
# # If check returns false (not digit) -> return false
#     for middle in range(len(s)):
#         if s[middle].isdigit():
#             if s[middle:].isdigit() == False:
#                 return False
#     return True


# main()

#below rest my 3 days of my agony
    # else:
    #     for x in s:
    #         if len(s)==6 and  and s[5:6].isdigit() == True:
    #             return True
    #         elif len(s)==5 and s[0:2].isalpha() and s[4:5].isdigit() == True:
    #             return True
    #         elif len(s)==4 and s[0:2].isalpha() and s[3:4].isdigit() == True:
    #             return True
    #         elif len(s)==3 and s[0:2].isalpha() and s[2:3].isdigit() == True:
    #             return True
    #         elif len(s)==2 and s[0:2].isalpha() and s[1:2].isdigit() == True:
    #             return True
    #         else:
    #             return False



    # if s[0:2].isalpha():
    #     return True
    # elif s[4:6].isnumeric():
    #     return True
    # elif 2 > len(s) <6:
    #     return False

    # else:
    #     return True
    # else:
        # return True
        # if s.isalnum():
        #     return True
        # else:
        #     return False




