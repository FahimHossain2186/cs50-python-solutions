import sys
import csv

def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        file_name = sys.argv[1]


    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)
            pizzas = [
                {
                    "name": row[reader.fieldnames[0]],
                    "small": row[reader.fieldnames[1]],
                    "large": row[reader.fieldnames[2]],
                }
                for row in reader
            ]

            first_row_length = len(reader.fieldnames[0])+3

            horizontal_line(first_row_length)
            print(f"| {reader.fieldnames[0]:<{first_row_length}}| {reader.fieldnames[1]}   | {reader.fieldnames[2]}   |")
            horizontal_line(first_row_length, 2)

            for pizza in pizzas:
                print(f"| {pizza["name"]:<{first_row_length}}| {pizza["small"]}  | {pizza["large"]}  |")
                horizontal_line(first_row_length)


    except FileNotFoundError:
        sys.exit("File does not exist")


def horizontal_line(n, m = 1):
    n += 1
    print("+", end="")
    if(m == 1):
        for i in range(n):
            print("-", end="")
        print("+---------+---------+")
    else:
        for i in range(n):
            print("=", end="")
        print("+=========+=========+")


if __name__ == "__main__":
    main()
