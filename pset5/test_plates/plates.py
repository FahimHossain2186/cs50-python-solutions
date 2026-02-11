import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    digit = False

    for c in s:
        if c.isdigit():
            if c == "0" and not digit:
                return False
            digit = True
        elif c.isalpha() and digit:
            return False
        elif c in string.punctuation or c.isspace():
            return False

    return True

if __name__ == "__main__":
    main()