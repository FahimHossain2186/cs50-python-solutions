import sys
import csv

def main():

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        file_read = sys.argv[1]
        file_write = sys.argv[2]

    try:
        with open(file_read, "r") as file:
            reader = csv.DictReader(file)
            wizards = [
                {
                    "first": row["name"].split(", ")[1],
                    "last" : row["name"].split(", ")[0],
                    "house": row["house"]
                }
                for row in reader
            ]

    except FileNotFoundError:
        sys.exit(f"Could not read {file_read}")

    try:
        with open(file_write, "w", newline="") as file:
            writer = csv.DictWriter(file,
                                    fieldnames = ["first", "last", "house"])
            writer.writeheader()
            writer.writerows(wizards)

    except FileNotFoundError:
        sys.exit(f"Could not read {file_write}")



if __name__ == "__main__":
    main()
