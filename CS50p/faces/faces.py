# changing old school smiley and sad face to emoji


# print("\U0001F60A \U0001F641")
#isnumeric()

# create a main function
def main():
    #create x variable to store input
    x = str(input())
    #print input while applying function
    print(convert(x))

#create the convert function to replace input
def convert(x):
    return x.replace(":)", "🙂").replace(":(" , "🙁")

#call main
main()