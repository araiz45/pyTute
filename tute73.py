import PyPDF2, os

pdffiles = []

for filename in os.listdir('./pdf'):
    if filename.endswith(".pdf"):
        if filename != "merged.pdf":
            pdffiles.append(filename)


pdffiles.sort(key=str.lower)

pdfMerge = PyPDF2.PdfMerger()


for filename in pdffiles:
    pdfFile = open ("./pdf/" + filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    pdfMerge.append(pdfReader)

pdfFile.close()
pdfMerge.write("merged.pdf")