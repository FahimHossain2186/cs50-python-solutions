import re

def main():
    print(convert(input("Hours: ")))


def to24(hour, meridian):
    if meridian == "AM":
        return 0  if hour == 12 else hour
    else:
        return 12 if hour == 12 else hour + 12


def convert(s):

    time = r"(1[0-2]|0?[1-9])(?::([0-5][0-9]))? (AM|PM) to (1[0-2]|0?[1-9])(?::([0-5][0-9]))? (AM|PM)$"
    match = re.match(time, s.strip())

    if not match:
        raise ValueError("Invalid format")

    (st_hr, st_min, st_meridian,
     fn_hr, fn_min, fn_meridian) = match.groups()

    st_min = st_min or 0
    fn_min = fn_min or 0

    st_hr = to24(int(st_hr), st_meridian)
    fn_hr = to24(int(fn_hr), fn_meridian)

    return f"{st_hr:02}:{st_min:02} to {fn_hr:02}:{fn_min:02}"


if __name__ == "__main__":
    main()
