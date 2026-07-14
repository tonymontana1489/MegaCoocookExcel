from pathlib import Path
import pdfplumber


class PDFReader:

    def read(self, file_path: str):

        file = Path(file_path)

        if not file.exists():
            raise FileNotFoundError(file)

        with pdfplumber.open(file) as pdf:
            return list(pdf.pages)