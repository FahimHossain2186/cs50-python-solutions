from fpdf import FPDF


def pdf_write(name):

    pdf = FPDF(orientation="portrait", unit="mm", format="A4")
    pdf.add_page()

    # Header
    pdf.set_font("helvetica", "B", 45)
    pdf.cell(0, 60, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    # Image --> x = (210 - w) / 2
    pdf.image("shirtificate.png", x=30, y=90, w=150)

    # Text on Shirt
    pdf.set_font("helvetica", "B", 25)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(140)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


def main():
    name = input ("Name: ")
    pdf_write(name)


if __name__ == "__main__":
    main()