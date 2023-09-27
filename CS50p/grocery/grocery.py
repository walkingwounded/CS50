## Grocery List Lab

grocery_list = {

}

grocery = grocery_list.keys()
values = grocery_list.values()

def main():
    while True:
        try:
            i = input().upper()
            if i not in grocery_list:
                grocery_list[i] = 1
            elif i in grocery_list:
                grocery_list[i] += 1

        except (EOFError):
            for g in sorted(grocery):
                print(grocery_list[g], g)
            break
        # print(grocery_list)
main()