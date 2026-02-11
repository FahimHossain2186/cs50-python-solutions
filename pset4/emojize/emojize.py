import emoji

x = input("Input: ").strip()
print("Output: " + emoji.emojize(x, language = 'alias'))
