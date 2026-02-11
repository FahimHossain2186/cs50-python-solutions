def main():
    word = input("A greeting: ")
    x = value(word)
    print(f"${x}")

def value(greeting):
    greeting = greeting.lower().strip()
    characters_list = list(greeting[0])

    if greeting.startswith("hello"):
        return 0
    elif characters_list[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
