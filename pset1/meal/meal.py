def main():
    time = input("What time is it? ")
    meal_time = convert(time)

    if 8 >= meal_time >= 7:
        print("breakfast time")
    elif 13 >= meal_time >= 12:
        print("lunch time")
    elif 19 >= meal_time >= 18:
        print("dinner time")


def convert(time):
    hr, min = time.split(":")
    hr = int(hr)
    min = int(min)

    return hr + min / 60


if __name__ == "__main__":
    main()
