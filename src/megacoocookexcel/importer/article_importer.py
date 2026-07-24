from __future__ import annotations

from pathlib import Path

import pdfplumber

from megacoocookexcel.models import Article


class ArticleImporter:
    """Import article master data from a Coocook purchase-list PDF."""

    AMOUNT_HEADER = "amount"
    ARTICLE_HEADER = "article"
    NO_SHOP_SECTION = "no shop section"

    def import_pdf(
        self,
        pdf_file: str | Path,
    ) -> list[Article]:
        """Return unique, alphabetically sorted articles from a purchase list."""

        articles: list[Article] = []
        seen: set[str] = set()
        current_shop = ""

        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                current_shop = self._find_shop(page, current_shop)

                for table in page.extract_tables():
                    if not self._is_purchase_table(table):
                        continue

                    for row in table:
                        name = self._extract_article_name(row)

                        if not name:
                            continue

                        key = name.casefold()

                        if key in seen:
                            continue

                        seen.add(key)
                        articles.append(
                            Article(
                                name=name,
                                shop=current_shop,
                                unit="",
                            )
                        )

        return sorted(
            articles,
            key=lambda article: article.name.casefold(),
        )

    # ------------------------------------------------------------------

    def _find_shop(
        self,
        page: pdfplumber.page.Page,
        current_shop: str,
    ) -> str:
        """Return the page's shop heading or keep the previous shop."""

        lines = [
            self._normalize_text(line)
            for line in (page.extract_text() or "").splitlines()
        ]

        for index, line in enumerate(lines):
            if not self._is_table_header_line(line):
                continue

            if index == 0:
                return current_shop

            candidate = lines[index - 1]

            if not self._is_shop_heading(candidate):
                return current_shop

            if candidate.casefold() == self.NO_SHOP_SECTION:
                return ""

            return candidate

        return current_shop

    # ------------------------------------------------------------------

    def _is_purchase_table(
        self,
        table: list[list[str | None]],
    ) -> bool:
        """Return whether a table contains the Coocook purchase-list header."""

        return any(
            row
            and len(row) >= 2
            and self._normalize_text(row[0]).casefold() == self.AMOUNT_HEADER
            and self._normalize_text(row[1]).casefold() == self.ARTICLE_HEADER
            for row in table
        )

    # ------------------------------------------------------------------

    def _extract_article_name(
        self,
        row: list[str | None] | None,
    ) -> str:
        """Return an article name from a data row, or an empty string."""

        if not row or len(row) < 2:
            return ""

        amount = self._normalize_text(row[0])
        name = self._normalize_text(row[1])

        if not amount or not name:
            return ""

        if (
            amount.casefold() == self.AMOUNT_HEADER
            and name.casefold() == self.ARTICLE_HEADER
        ):
            return ""

        return name

    # ------------------------------------------------------------------

    def _is_table_header_line(
        self,
        line: str,
    ) -> bool:
        """Return whether a text line is the purchase-list table header."""

        parts = line.casefold().split()

        return len(parts) >= 2 and parts[0:2] == [
            self.AMOUNT_HEADER,
            self.ARTICLE_HEADER,
        ]

    # ------------------------------------------------------------------

    def _is_shop_heading(
        self,
        line: str,
    ) -> bool:
        """Return whether a line is a shop heading rather than page metadata."""

        if not line:
            return False

        metadata_markers = (
            "coocook",
            "purchase list",
            "http",
        )

        normalized_line = line.casefold()

        return not any(marker in normalized_line for marker in metadata_markers)

    # ------------------------------------------------------------------

    def _normalize_text(
        self,
        value: str | None,
    ) -> str:
        """Collapse PDF line breaks and repeated whitespace into one space."""

        return " ".join((value or "").split())
