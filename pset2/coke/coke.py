due = 50

while True:
    print("Amount Due:", due)
    x = int(input("Insert Coin: "))

    if x == 5 or x == 10 or x == 25:
        due -= x

    if due <= 0:
        due *= -1
        print("Change Owed:", due)
        break
