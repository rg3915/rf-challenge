import PyPDF2
import re


WORD = re.compile(r'Médio prazo.*')

pdfFileObj = open('R20160324.pdf', 'rb')  # Abre o arquivo
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  # Lê o arquivo
pageObj = pdfReader.getPage(-1)  # Pega a última página
# print(pageObj.extractText())  # Imprime o texto da página
word = pageObj.extractText()
print(WORD.findall(word))
# lista = []

# for w in word:
#     lista += WORD.findall(w)


# pdfFileObj = open('R20161230.pdf', 'rb')  # Abre o arquivo
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  # Lê o arquivo
# pageObj = pdfReader.getPage(-1)  # Pega a última página
# print(pageObj.extractText())  # Imprime o texto da página
