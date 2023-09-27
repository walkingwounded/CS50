#bank comedy


def main():
    greeting = str(input("Greeting: "))
    print("$"+str(value(greeting)))

def value(greeting):
    greeting = str(greeting).lower().strip()
    if greeting.startswith("hello") == True:
        return 0
    elif greeting.startswith("h") == True:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()


## backup for Problem Set 1
# def main():
#     g = str(input("Greeting: ")).lower().strip()
#     if g.startswith("hello") == True:
#         print("$0")
#     elif g.startswith("h") == True:
#         print("$20")
#     else:
#         print("$100")
#    print(g.startswith("hello"))


# main()
