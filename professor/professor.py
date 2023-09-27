### Little Professor Game Lab
import random
import sys

    #main professor game
def main():
    level = get_level()
    round = 0
    score = 0
    ## while loop for 10 rounds
    while round <10:
        int1 = generate_integer(level)
        int2 = generate_integer(level)
        ans = int1 + int2
        qns = str(int1), "+", str(int2), "= "
    ### try input, pass except valueerror
        try:
            i = input(' '.join(qns))
        except(ValueError):
            pass

    ####check ans with input
        if i == str(ans):
            score +=1
            round +=1
        else:
            print("EEE")
            tries = 0
            while tries <2:
                try:
                    i = input(' '.join(qns))
                    if i == str(ans):
                        round +=1
                        break
                    elif tries == 1:
                        print(' '.join(qns),ans)
                        round+=1
                        break
                    elif i != str(ans):
                        print('EEE')
                        tries +=1

                except(ValueError):
                    pass

    ###### gameover!
        if round == 10:
            print("Score:",score)
            sys.exit

####### check leve input
def get_level():
    check = 0
    while check == 0:
        try:
            level = int(input("Level: "))
            if level <=0:
                pass
            elif level >3:
                pass
            else:
                check+1
                return level
        except(ValueError):
            pass

######## generate random integer with level input.
def generate_integer(level):
    try:
        if level == 1:
            i1 = (random.randint(0,9))
            return i1
        elif level == 2:
            i2 = (random.randint(10,99))
            return i2
        elif level == 3:
            i3 = (random.randint(100,999))
            return i3
        else:
            pass
    except(ValueError):
        pass


if __name__ == "__main__":
    main()



################# first draft and failed many 5days of trying
# def main():
#     game = 0
#     score = 0
#     while game <10:
#         random_int1 = random.randint(0, 9)
#         random_int2 = random.randint(0, 9)
#         qns = random_int1 + random_int2
#         str_qns = str(random_int1), "+", str(random_int2)
#         ans = (input(str_qns))
#         if qns == ans:
#             game = +1
#             score = +1
#         else:
#             print("wrong")
#         print("Score: ", score)




# def get_level():
#     l_check = 0
#     while l_check <1:
#         try:
#             l = int(input("Level: "))
#             if l >3:
#                 pass
#             elif l <0:
#                 pass
#             else:
#                 return
#         except (ValueError):
#             pass



# def generate_integer(level):
#         random_int1 = random.randint(0, 9)
#         random_int2 = random.randint(0, 9)
#         level = random_int1 + random_int2
#         answer = (input(random_int1,"+",random_int2, "= "))





