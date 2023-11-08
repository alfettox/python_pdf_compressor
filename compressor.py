from tkinter import Tk, Label, Button, filedialog
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def compress_pdf(input_file, output_file):
    # Create a PDF canvas to generate a minimal PDF
    c = canvas.Canvas(output_file)
    c.showPage()
    c.save()

    # Open the minimal PDF using PyPDF2
    pdf_writer = PdfFileWriter()

    # Merge the pages from the original PDF
    with open(input_file, 'rb') as input_pdf:
        pdf_reader = PdfFileReader(input_pdf)
        for page_num in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page_num))

    # Write the merged PDF to the output file
    with open(output_file, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

def select_input_pdf():
    input_file = filedialog.askopenfilename(title="Select PDF File to Compress", filetypes=[("PDF files", "*.pdf")])
    if input_file:
        output_file = input_file.replace(".pdf", "_compressed.pdf")
        compress_pdf(input_file, output_file)
        status_label.config(text=f"File compressed and saved as {output_file}")

app = Tk()
app.title("PDF Compressor")

select_button = Button(app, text="Select PDF File", command=select_input_pdf)
status_label = Label(app, text="", wraplength=300)

select_button.pack(pady=20)
status_label.pack()

app.mainloop()
