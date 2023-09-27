#Adieu, Adieu Lab
import inflect
p = inflect.engine()

my_list = []


while True:
    try:
        i = input("Name: ").title()
        my_list.append(i)


    except (EOFError):
        o = p.join((my_list))
        print("Adieu, adieu, to", o)
        break

