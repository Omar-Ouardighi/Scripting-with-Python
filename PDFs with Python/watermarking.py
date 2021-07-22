from re import template
import PyPDF2

watermark = PyPDF2.PdfFileReader(open('watermark.pdf','rb'))
pdf_file = PyPDF2.PdfFileReader(open('superPDF.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()


for i in range(pdf_file.getNumPages()):
    page = pdf_file.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)


with open('waterMarked.pdf','wb') as file:
    output.write(file)