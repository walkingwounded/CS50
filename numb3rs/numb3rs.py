#lab for numb3rs

import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))



def validate(ip):
    try:
        ip_check = re.search(r"^([0-9](?:[0-9]?[0-9]?)?)\.([0-9](?:[0-9]?[0-9]?)?)\.([0-9](?:[0-9]?[0-9]?)?)\.([0-9](?:[0-9]?[0-9]?)?)$", ip)
        if int(ip_check.group(1)) <= 255 and int(ip_check.group(2)) <= 255 and int(ip_check.group(3)) <= 255 and int(ip_check.group(4)) <= 255:
            #print(ip_check.group(1), ip_check.group(2),ip_check.group(3),ip_check.group(4))
            return(True)
        else:
            #print(ip_check.group(1), ip_check.group(2),ip_check.group(3),ip_check.group(4))
            return(False)
    except (ValueError, AttributeError):
        return(False)







if __name__ == "__main__":
    main()