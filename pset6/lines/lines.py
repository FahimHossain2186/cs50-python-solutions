import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
else:
    file_name = sys.argv[1]


try:
    with open(file_name, "r") as file:
        code_length = 0
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            code_length += 1
        print(code_length)


except FileNotFoundError:
    sys.exit("File does not exist")
