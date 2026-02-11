camel = input("camelCase: ")
snake = ""

for letter in camel:
    if(letter == letter.capitalize()):
        snake += "_" + letter.lower()
    else:
        snake += letter

print(snake)