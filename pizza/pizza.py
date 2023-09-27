## Pizza lab, hungry for pizza XD
import csv
from tabulate import tabulate
import sys

def main():
    try:
        if len(sys.argv) == 1:
            sys.exit('Too few command-line arguments')
        elif len(sys.argv) >2:
            sys.exit('Too many command-line arguments')
        elif (sys.argv[1]).endswith('.csv') == False:
            sys.exit('Not a CSV file')
        else:
            menu(sys.argv[1])
    except(FileNotFoundError):
        sys.exit('File does not exist')

def menu(i):
    with open(i) as file:
        r_table = csv.reader(file)
        print(tabulate(r_table, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()



###junks that I wrote
# def sicilian_menu():
#     with open("scicilian.csv") as file:
#         s_table = csv.reader(file)
#         print(tabulate(s_table, headers="firstrow", tablefmt="pretty"))
