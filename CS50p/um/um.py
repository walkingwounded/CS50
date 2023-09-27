### lab um... lets.. um... do..it!! um..
import re
import sys



def main():
    print(count(input("Text: ")))


def count(s):
    um_count = 0
    ##according to documentation \b means match start and end of a str
    um_list = re.findall(r'\bum\b', s, re.IGNORECASE)
    um_count = len(um_list)
    return(um_count)



if __name__ == "__main__":
    main()