###Lab for Lines of Code
import sys


def main():
    try:
        if len(sys.argv) == 1:
            sys.exit('Too few command-line arguments')
        elif len(sys.argv) >2:
            sys.exit('Too many command-line arguments')
        elif (sys.argv[1]).endswith('.py') == False:
            sys.exit('Not a Python file')
        else:
            with open(sys.argv[1]) as file:
                    count = 0
                    for line in file:
                        if line.lstrip().startswith(('# ', '#')) == True:
                            count = count
                        elif len(line) == 1 or 0:
                            count = count
                        elif line.isspace():
                            count = count
                        else:
                            count = count+1
                    print(count)
    except(FileNotFoundError):
        sys.exit('File does not exist')

main()