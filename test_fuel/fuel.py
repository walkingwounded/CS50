#fuel gauge lab
import math


def main():
    while True:
        try:
            fraction = input("Fraction: ")
            # fraction_s = fraction.split("/")
            # if int(fraction_s[1]) == 0:
            #     raise ZeroDivisionError
            # elif int(fraction_s[0]) > int(fraction_s[1]):
            #     raise ValueError
    ##check for higher numerator
            percentage = convert(fraction)
            if percentage is None:
                pass
            else:
                break
        except (AttributeError, ValueError, ZeroDivisionError, IndexError):
            pass
    #print(percentage)
    o = gauge(percentage)
    if o.isnumeric() == True:
        print(o, "%",sep="")
    else:
        print(o)


def convert(fraction):
    while True:
        try:
            fraction = fraction.split("/")
            print(fraction)
            if len(fraction) > 2:
                raise IndexError()
            elif int(fraction[1]) == 0:
                raise ZeroDivisionError()
            elif int(fraction[0]) > int(fraction[1]):
                raise ValueError()
            elif fraction[0].isdigit() == False:
                raise ValueError()

            else:
                numerator = int(fraction[0])
                denominator = int(fraction[1])
                fraction = round(numerator/denominator*100)
                return fraction
        except (ZeroDivisionError,ValueError, IndexError):
            raise

def gauge(percentage):
    if percentage <= 1:
        percentage = "E"
        return percentage
    elif percentage >= 99:
        percentage = "F"
        return percentage
    else:
        return str(percentage)

    #capture valueerror, zde, and index error, man my coding is bad



if __name__ == "__main__":
    main()

######################## backup for week 3, problem set 3

# def main():
#     #keep doing until hit error
#     while True:
#         try:
#             i = input("Fraction: ")
#             i = i.split("/")
#             ##check for higher numerator
#             if int(i[0]) > int(i[1]):
#                 i = "a"
#             else:
#                 numerator = int(i[0])
#                 denominator = int(i[1])
#                 o = round(numerator/denominator*100)
#                 if o <= 1:
#                     o = "E"
#                     print(o)
#                 elif o >= 99:
#                     o = "F"
#                     print(o)
#                 else:
#                     print(int(o), "%",sep="")
#                 break
#         #capture valueerror, zde, and index error, man my coding is bad
#         except (ValueError, ZeroDivisionError, IndexError):
#             pass


# ### RIP 30mins
# # #def get_fraction(prompt):
# #     while True:
# #         try:
# #             input(prompt)
# #             prompt = prompt.strip("/")
# #             return int(prompt)
# #         except ValueError:
# #             pass



# main()