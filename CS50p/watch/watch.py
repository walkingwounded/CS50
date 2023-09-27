###Watch on Youtube CS50P
import re
import sys



def main():
    print(parse(input("HTML: ")))



def parse(s):
    if shortcut := re.search(r"^.*(xvFZjo5PgG0)(?:.*)?(?:\>)$",s):
        return(f"https://youtu.be/"+shortcut.group(1))


if __name__ == "__main__":
    main()