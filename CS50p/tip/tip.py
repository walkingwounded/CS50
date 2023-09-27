#Wizard tip calculator


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    #remove $ from input
    d = d.replace("$", "")
    #return d as float
    return float(d)


def percent_to_float(p):
    # TODO
    #remove % from input
    p = p.replace("%", "")
    #return p as percentage and float
    return float(p)/100


main()