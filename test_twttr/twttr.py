#twttr app lab


def main():
    word = input("Input: ")
    o = shorten(word)
    print("Output:", o)

def shorten(word):
    if word == 'x':
        exit();
    else:
        word = word;
        vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U");
        for x in word:
            if x in vowels:
                word = word.replace(x,"");
        return word


if __name__ == "__main__":
    main()

#############backup before delving into week5 lab test_twttr
#twttr app lab


# def main():
#     i = input("Input: ")
#     if i == 'x':
#         exit();
#     else:
#         o = i;
#         vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U");
#         for x in i:
#             if x in vowels:
#                 o = o.replace(x,"");
#         print("Output:", o)

# main()

#unsuccessful coding 13/6/2022
# def main():
#     i = str(input("Input: "))
#     ntc = ""

#     for tc in range(len(i)):
#         if i[tc].isalpha == True:
#             ntc = ntc + i[tc].replace("i", "")
#         else:
#             ntc += i[tc]

#     print("Output: ", ntc)
