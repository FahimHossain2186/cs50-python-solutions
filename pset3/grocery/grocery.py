def main():
    x = []

    while True:
        try:
            item = input().upper()
            x.append(item)

        except EOFError:
            freq = {}

            for n in x:
                if n in freq:
                    freq[n] += 1
                else:
                    freq[n] = 1

            for m in sorted(freq):
                print(f"{freq[m]} {m}")
            break

main()
