from pathlib import Path
import pdfplumber
from pdfplumber.pdf import PDF


class PDFReader:

    def read(self, file_path: str) -> PDF:

        file = Path(file_path)

        if not file.exists():
            raise FileNotFoundError(file)

        return pdfplumber.open(file)