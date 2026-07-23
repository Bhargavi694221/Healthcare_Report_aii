
from tools.pdf_reader import PDFReader
from tools.medical_parser import MedicalParser

text = PDFReader.read_pdf("uploads/old_report.pdf")

data = MedicalParser.parse(text)

print(data)