import pdfplumber


class PDFReader:

    def read(self, file_path):

        with pdfplumber.open(file_path) as pdf:

            return pdf.pages