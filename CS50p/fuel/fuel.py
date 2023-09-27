#fuel gauge lab
import math


def main():
    #keep doing until hit error
    while True:
        try:
            i = input("Fraction: ")
            i = i.split("/")
            ##check for higher numerator
            if int(i[0]) > int(i[1]):
                i = "a"
            else:
                numerator = int(i[0])
                denominator = int(i[1])
                o = round(numerator/denominator*100)
                if o <= 1:
                    o = "E"
                    print(o)
                elif o >= 99:
                    o = "F"
                    print(o)
                else:
                    print(int(o), "%",sep="")
                break
        #capture valueerror, zde, and index error, man my coding is bad
        except (ValueError, ZeroDivisionError, IndexError):
            pass


### RIP 30mins
# #def get_fraction(prompt):
#     while True:
#         try:
#             input(prompt)
#             prompt = prompt.strip("/")
#             return int(prompt)
#         except ValueError:
#             pass



main()