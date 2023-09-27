#camel case to snake case lab



def main():
    #cc is variable for camelcase to store
    cc = input("camelCase: ").strip()
    #sc is variable for snake_case to store
    sc = ""
    #for loop to cycle through the lenght of cc/input
    for i in range(len(cc)):
        #if input[current in range] is NOT upper, insert string into sc/output, if it is uppercase insert "_" before string[current in range].lower()
        if cc[i].isupper() == True:
            sc = sc + "_" + cc[i].lower()
        else:
            sc += cc[i]
    print("snake_case: ", sc)
    #checking print (input[range]), turns out without for loop, it will print the last string character.
    #  print (cc[i])








main()