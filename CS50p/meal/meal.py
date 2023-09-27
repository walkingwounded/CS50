#meal time lab


def main():
    i = convert(input("What time is it? ").strip())
    if 7 <= i <= 8:
        print("breakfast time")
    elif 12 <= i <= 13:
        print("lunch time")
    elif 18 <= i <= 19:
        print("dinner time")



def convert(time):
    #challenge accepted for input #:## p.m.
    if time.endswith("p.m.") == True:
        time = time.strip(" p.m.")
        hours, minutes = time.split(":")
        hours = float(hours)
        minutes = float(minutes)
        time = (hours+12) + (minutes/60)
        return float(time)
    #challenge accepted for #:## a.m.
    elif time.endswith("a.m.") == True:
        time = time.strip(" a.m.")
        hours, minutes = time.split(":")
        hours = float(hours)
        minutes = float(minutes)
        time = (hours) + (minutes/60)
        return float(time)
    else:
        hours, minutes = time.split(":")
        hours = float(hours)
        minutes = float(minutes)
        time = hours + minutes/60
        return float(time)

if __name__ == "__main__":
    main()