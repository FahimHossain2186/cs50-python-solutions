import random


def main():
    level = get_level()
    correct = 0
    i = 0

    while i < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y

        j = 0
        while(j<3):
            try:
                answer = int(input(f"{x} + {y} ="))
                j += 1

                if(answer == result):
                    correct += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
                j += 1
                continue

        if j == 3:
            print(f"{x} + {y} = {result}")
        i += 1

    print(f"Score: {correct}")

def get_level():

    while True:
        try:
            level = int(input("Level: "))

            if(level == 1 or level == 2 or level == 3):
                return level
            else:
                raise ValueError
        except ValueError:
            pass



def generate_integer(level):

    first_number = pow(10,(level - 1))
    if(level == 1):
        first_number -= 1
    last_number = pow(10,level) - 1
    return random.randint(first_number, last_number)


if __name__ == "__main__":
    main()
