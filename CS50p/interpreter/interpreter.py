#python interpreter


def main():
    i = str(input("Expression: ")).strip()
    x, y, z = i.split(" ")
    x = float(x)
    z = float(z)
    if y == "+":
        print (x + z)
    elif y == "-":
        print (x - z)
    elif y == "*":
        print (x * z)
    elif y == "/":
        print (x / z)
    else:
        print("Error")

main()