def main():
    word = input("Input: ")
    out = shorten(word)
    print("Output:", out)

def shorten(word):
    out = ""

    for letter in word:
        if(letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']):
            continue
        else:
            out += letter

    return out

if __name__ == "__main__":
    main()

