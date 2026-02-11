import sys

def main():
    name_list = []

    while True:
        try:
            name = input("Input: ")
            name_list.append(name)

        except EOFError:
            print()
            adieu(name_list)
            sys.exit()

def adieu(name_list):
    print("Adieu, adieu, to", end = " ")

    if len(name_list) == 1:
        print(name_list[0])
    elif len(name_list) == 2:
        print(f"{name_list[0]} and {name_list[1]}")
    else:
        for name in name_list[:-1]:
            print(name, end = ", ")
        print(f"and {name_list[-1]}")


if __name__ == "__main__":
    main()
