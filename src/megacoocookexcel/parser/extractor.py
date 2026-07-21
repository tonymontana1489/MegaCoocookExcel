from pdfplumber.pdf import PDF


class PdfTableExtractor:
    """
    Extracts all tables from every page of a PDF.
    """

    def extract(self, pdf: PDF) -> list[dict]:
        """
        Extract all tables from the PDF.

        Returns:
            A list containing one dictionary per page.
        """

        result = []

        for page_number, page in enumerate(pdf.pages, start=1):
            tables = page.extract_tables()

            result.append(
                {
                    "page": page_number,
                    "tables": tables,
                }
            )

        return result