def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    formattedDollars = d.split('$')
    if (formattedDollars[0] == ''):
        return float(formattedDollars[1])
    else:
        return float(formattedDollars[0])


def percent_to_float(p):
    formattedPercentage = p.split('%')
    if (formattedPercentage[0] != ''):
        return float(formattedPercentage[0])/100
    else:
        return float(formattedPercentage[1])/100


main()