months = {
            "January"   : 1,
            "February"  : 2,
            "March"     : 3,
            "April"     : 4,
            "May"       : 5,
            "June"      : 6,
            "July"      : 7,
            "August"    : 8,
            "September" : 9,
            "October"   : 10,
            "November"  : 11,
            "December"  : 12
        }

while True:
    try:
        date = input("Date: ").strip()

        #Month
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            if not(12>= month >= 1):
                raise ValueError

        else:
            month, day_year = date.split(" ", 1)
            month = months[month.capitalize()]
            day, year = day_year.split(", ")

        #Day
        if 31 >= int(day) >= 1:
            day = int(day)
        else:
            raise ValueError

        year = int(year)

        print(f"{year}-{month:02}-{day:02}")
        break

    except (ValueError, KeyError):
        pass