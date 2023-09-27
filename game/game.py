###Guessing Game Lab.
#for random functions
import random
#for sys.exit
import sys

def main():
    levelcheck = 0
    guesscheck = 0

    #Level input
    while levelcheck <1:
        try:
            level = int(input("Level: "))
            if level <0:
                pass
            else:
                levelcheck = +1
        except(ValueError):
            pass
    #answer input
    answer = random.randint(1, int(level)+1)

    #guess input and checking against answer
    while guesscheck <1:
        try:
            guess = int(input("Guess: "))
            if guess <0:
                pass
            else:
                if guess < answer:
                    print("Too small!")
                    pass
                elif guess > answer:
                    print("Too large!")
                    pass
                elif guess == answer:
                    sys.exit("Just right!")
        except(ValueError):
            pass


main()