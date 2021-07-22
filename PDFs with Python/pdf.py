import sys
import PyPDF2

inputs = sys.argv[1:]

def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('superPDF.pdf')

pdf_merger(inputs)

