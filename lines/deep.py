#deep thought program


def main():
    # input convert to string and strip() and lowercase
    i = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")).strip().lower()
    #if elseif else statement
    if i == "42":
        print ("Yes")
    elif i == "forty-two":
        print("Yes")
    elif i == "forty two":
        print("Yes")
    else:
        print ("No")

main()
