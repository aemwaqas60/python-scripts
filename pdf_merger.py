import sys
import PyPDF2

inputs = sys.argv[1:]


def pdf_combiner(pdfList):
    pdfMerger = PyPDF2.PdfMerger()
    for file in pdfList:
        print(file)
        pdfMerger.append(file)
    pdfMerger.write('./files/unity-system.pdf')


pdf_combiner(inputs)
