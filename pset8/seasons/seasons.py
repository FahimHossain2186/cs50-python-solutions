from datetime import date
import sys
import re
import inflect

def to_min(date_of_birth):

    if re.search(r"^\d{4}-\d{2}-\d{2}$", date_of_birth):
        year, month, day = date_of_birth.split("-")

        try:
            birthday = date(int(year), int(month), int(day))
        except ValueError:
            raise ValueError

        today = date.today()
        diff = today - birthday

        return diff.days * 24 * 60

    else:
        raise ValueError


def main():

    date_of_birth = input("Date of Birth: ").strip()

    try:
        #minutes = to_min(date_of_birth)
        #minutes_words = num2words(minutes).capitalize()

        minutes = to_min(date_of_birth)
        p = inflect.engine()
        minutes_words = p.number_to_words(minutes, andword="")

        print(f"{minutes_words.capitalize()} minutes")

    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
