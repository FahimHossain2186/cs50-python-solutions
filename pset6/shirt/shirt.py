import sys
from PIL import Image, ImageOps

def main():

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif not sys.argv[1].lower().endswith((".png", ".jpg", ".jpeg")):
        sys.exit("Invalid input")
    elif not sys.argv[2].lower().endswith((".png", ".jpg", ".jpeg")):
        sys.exit("Invalid input")
    elif ((sys.argv[1].lower().split("."))[1] !=
          (sys.argv[2].lower().split("."))[1]):
        sys.exit("Input and output have different extensions")


    try:
        image = Image.open(sys.argv[1])

    except IOError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    fitted_image = ImageOps.fit(image, shirt.size)

    fitted_image.paste(shirt, mask = shirt)
    fitted_image.save(sys.argv[2])

if __name__ == "__main__":
    main()


