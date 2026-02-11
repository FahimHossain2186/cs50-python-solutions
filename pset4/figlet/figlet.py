import random
import pyfiglet
import sys

def main():
    if len(sys.argv) == 1:
        fonting()
    elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
        fonting(sys.argv[2])
    else:
        sys.exit("Invalid usage")

def fonting(font=None):
    if font is None:
        font = random.choice(pyfiglet.FigletFont.getFonts())
    elif font not in(pyfiglet.FigletFont.getFonts()):
        sys.exit("Invalid usage")

    word = input("Input: ")
    f = pyfiglet.figlet_format(word, font=font)
    print(f)

main()
