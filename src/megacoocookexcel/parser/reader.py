from pathlib import Path

import pdfplumber
from pdfplumber.pdf import PDF


class PDFReader:
    """Loads a PDF document from disk."""

    def read(self, file_path: str) -> PDF:
        """Open a PDF and return the pdfplumber document."""

        file = Path(file_path)

        if not file.exists():
            raise FileNotFoundError(file)

        return pdfplumber.open(file)