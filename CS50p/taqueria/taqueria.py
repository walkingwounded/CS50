###Taqueria menu lab

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

food = menu.keys()
price = menu.values()

def main():
    n = 0
    while n>=0:
        try:
            item = input("Item: ").title()
            o = price.mapping[item]
            n += o
            print('$','{:.2f}'.format(n),sep="")

        except (EOFError):
            break
        except (KeyError):
            pass



main()