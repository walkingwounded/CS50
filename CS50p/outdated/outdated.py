### Lab for outdated date


month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
#YYYY-MM-DD
def main():
    #while True Loop
    while True:
        try:
            ##check for "," and "/" in input. I admit I've bandaid this code ontop 😂 poor coding
            i = input("Date: ")
            if "," not in i:
                if "/" not in i:
                    raise(ValueError)
                else:
                    pass
            ##check for "/" and incorrect format. I admit I've bandaid this code ontop 😂 poor coding
            if "/" in i:
                i_check = i.split("/")
                if i_check[0] in month_list:
                    raise(ValueError)
                else:
                    pass
            ##take input and replace , and / with " "
            i = i.title().replace("/"," ")
            i = i.title().replace(",", "")
            i = i.split()
            ###check if it there is a string, convert str("month") name into int()
            if i[0] in month_list:
                YYYY = i[2]
                DD = i[1]
                MM = month_list.index(i[0]) +1
                MM = MM
            else:
                YYYY = i[2]
                DD = i[1]
                MM = i[0]
            ####validate MM and DD
            if int(MM) >12:
                pass
            elif int(DD) > 31:
                pass
            #####print date
            else:
                if len(str(MM)) <2 and len(str(DD)) <2:
                    print(YYYY,"-0",MM,"-0",DD,sep="")
                    break
                elif len(str(DD)) <2:
                    print(YYYY,"-",MM,"-0",DD,sep="")
                    break
                elif len(str(MM)) <2:
                    print(YYYY,"-0",MM,"-",DD,sep="")
                    break
                else:
                    print(YYYY,"-",MM,"-",DD,sep="")
                    break
        except(ValueError):
            pass
        # except (EOFError):
        #     print("end")



main()



##
# def checkforinput(i):
#     if i.isnumeric():
#         i.split('/')
#     else:
#         i.rstrip(',')
#         i.split()
#     return i