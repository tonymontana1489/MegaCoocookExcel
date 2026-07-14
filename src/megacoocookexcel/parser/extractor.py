class TableExtractor:

    def extract(self, pages):

        tables=[]

        for page in pages:

            table=page.extract_table()

            if table:

                tables.append(table)

        return tables