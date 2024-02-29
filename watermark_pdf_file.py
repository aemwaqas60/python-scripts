import PyPDF2

template = PyPDF2.PdfReader(open('./files/super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('./files/wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

with open('./files/watermarked-file.pdf', 'wb') as file:
    output.write(file)
