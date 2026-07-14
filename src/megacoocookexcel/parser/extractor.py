class PdfTableExtractor:
    """
    Extracts all tables from every page.
    """

    def extract(self, pdf):

        result = []

        for page_number, page in enumerate(pdf.pages, start=1):

            tables = page.extract_tables()

            result.append(
                {
                    "page": page_number,
                    "tables": tables
                }
            )

        return result