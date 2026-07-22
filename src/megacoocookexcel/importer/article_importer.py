from __future__ import annotations

from pathlib import Path

import pdfplumber

from megacoocookexcel.models import Article


class ArticleImporter:
    """
    Imports the Coocook article master data from a PDF.
    """

    HEADER = "name"

    NAME_COLUMN = 0
    COMMENT_COLUMN = 1
    SHOP_COLUMN = 4
    UNIT_COLUMN = 5
    TAG_COLUMN = 6

    def import_pdf(
        self,
        pdf_file: str | Path,
    ) -> list[Article]:
        """
        Import all articles from a Coocook article PDF.
        """

        rows = self._extract_rows(pdf_file)

        return self._create_articles(rows)

    # ------------------------------------------------------------------

    def _extract_rows(
        self,
        pdf_file: str | Path,
    ) -> list[list[str]]:

        rows: list[list[str]] = []

        with pdfplumber.open(pdf_file) as pdf:

            for page in pdf.pages:

                tables = page.extract_tables()

                if not tables:
                    continue

                for table in tables:

                    for row in table:

                        if row:
                            rows.append(row)

        return rows

    # ------------------------------------------------------------------

    def _create_articles(
        self,
        rows: list[list[str]],
    ) -> list[Article]:

        articles: list[Article] = []
        seen: set[str] = set()

        for row in rows:

            #
            # Expected columns:
            #
            # 0 Name
            # 1 Comment
            # 2 Preorder
            # 3 Shelf Life
            # 4 Shop Section
            # 5 Suggested Unit
            # 6 Tags
            # 7 Empty
            #

            if len(row) < 7:
                continue

            name = (row[self.NAME_COLUMN] or "").strip()

            if not name:
                continue

            if name.casefold() == self.HEADER:
                continue

            key = name.casefold()

            if key in seen:
                continue

            seen.add(key)

            comment = (row[self.COMMENT_COLUMN] or "").strip()
            shop = (row[self.SHOP_COLUMN] or "").strip()
            unit = (row[self.UNIT_COLUMN] or "").strip()
            tags = (row[self.TAG_COLUMN] or "").strip()

            articles.append(
                Article(
                    name=name,
                    shop=shop,
                    unit=unit,
                    comment=comment,
                    tags=tags,
                )
            )

        articles.sort(
            key=lambda article: article.name.casefold()
        )

        return articles