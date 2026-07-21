import datetime

from megacoocookexcel.models import ShoppingItem
from megacoocookexcel.parser.column_parser import ColumnParser


class ShoppingItemMapper:
    """
    Maps a single Coocook table row to a ShoppingItem.
    """

    def __init__(self):
        self._column_parser = ColumnParser()

    def map_row(self, row: list[str | None]) -> ShoppingItem | None:

        # Header überspringen
        if row[0] == "Amount":
            return None

        # Fortsetzungszeilen kommen später
        if row[0] is None:
            return None

        total_amount, total_unit = self._split_amount(row[0])

        details = self._column_parser.parse(row[2] or "")

        return ShoppingItem(
            article=row[1],

            total_amount=total_amount,
            total_unit=total_unit,

            recipe_amount=details.recipe_amount,
            recipe_unit=details.recipe_unit,

            dish=details.dish,

            meal=details.meal,
            servings=details.servings,

            date=self._parse_date(row[3]),

            category=None,
        )

    def _split_amount(
        self,
        text: str,
    ) -> tuple[float | None, str | None]:

        parts = text.replace(",", ".").split(maxsplit=1)

        if len(parts) != 2:
            return None, None

        try:
            amount = float(parts[0])
        except ValueError:
            amount = None

        return amount, parts[1]

    def _parse_date(
        self,
        text: str | None,
    ) -> datetime.date | None:

        if not text:
            return None

        try:
            _, date_text = text.split(", ", maxsplit=1)
            return datetime.date.fromisoformat(date_text)

        except Exception:
            return None