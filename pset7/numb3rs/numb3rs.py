import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    try:
        parts = ip.strip().split(".")
        if len(parts) != 4:
            return False

        for part in parts:

            if part == "":
                return False

            if re.fullmatch(r"0[0-9]+", part):
                return False

            if not 0 <= int(part) <= 255:
                return False

        return True

    except ValueError:
        return False

if __name__ == "__main__":
    main()
