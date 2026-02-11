import random
import sys

x = 0
while True:
    try:
        level = int(input("Level: "))

        if(level < 1):
            raise ValueError
        else:
            break

    except ValueError:
        pass

n = random.randint(1, level)

while(x != n):

    try:
        x = int(input("Guess: "))

        if(x < 1):
            raise ValueError

        if(x < n):
            print("Too small!")
        elif(x > n):
            print("Too large!")
        else:
            print("Just right!")
            sys.exit()

    except ValueError:
        pass
