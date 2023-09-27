###Week8.3 - Shirtificate! Can't wait for the CS50p-Certificate!
from fpdf import FPDF
import sys

class PDF(FPDF):
    def shirt(self):
        self.add_page()
        self.image("shirtificate.png", x=10, y=75, w=pdf.epw, h=pdf.epw)


    def text(self):
        self.set_font("helvetica", style='B', size=40)
        name = input("Name: ")
        name_text = name+' took CS50'
        self.cell(w = 0, h = 50, align='C' ,txt='CS50 Shirtificate')
        self.set_font("helvetica", style='', size=25)
        self.set_text_color(255,255,255)
        self.ln(h=130)
        self.cell(w = 0, h = 0, align='C' ,txt=name_text)


pdf = PDF()
pdf.shirt()
pdf.text()
pdf.output("shirtificate.pdf")





####second try

# ###get user name

# ###open shirt image
# pdf = FPDF(orientation="portrait", unit='mm', format="A4")
# pdf.set_font("helvetica", style='B', size=40)
# pdf.add_page()
# pdf.image("/workspaces/90247552/CS50p/shirtificate/shirtificate.png", x=10, y=75, w=pdf.epw, h=pdf.epw)

# ###design shirt
# text = 'CS50 Shirtificate'
# name = input("Name: ")
# name_text = name+' took CS50'
# pdf.cell(w = 0, h = 50, align='C' ,txt=text)

# ###insert user name
# pdf.set_font("helvetica", style='', size=25)
# pdf.set_text_color(255,255,255)
# pdf.ln(h=130)
# pdf.cell(w = 0, h = 0, align='C' ,txt=name_text)

# ###print shirt
# pdf.output("shirtificate.pdf")