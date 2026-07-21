import re
from dataclasses import dataclass


@dataclass(slots=True)
class ColumnData:
    """
    Parsed information from the third Coocook table column.
    """

    recipe_amount: float | None = None
    recipe_unit: str | None = None

    dish: str | None = None

    servings: int | None = None

    meal: str | None = None


class ColumnParser:
    """
    Parses the third column of a Coocook shopping list.

    Example input:

        1.12 Liter
        Salatsoße Buttermilch-Zitrone
        1
        Tag 1 (Sonntag)
    """

    _amount_pattern = re.compile(
        r"^(\d+(?:[.,]\d+)?)\s+(.+)$"
    )

    _servings_pattern = re.compile(r"^\d+$")

    def parse(self, text: str) -> ColumnData:

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        data = ColumnData()

        if not lines:
            return data

        # ---- amount -------------------------------------------------

        match = self._amount_pattern.match(lines[0])

        if match:
            amount = match.group(1).replace(",", ".")

            data.recipe_amount = float(amount)
            data.recipe_unit = match.group(2)

        # ---- servings / meal ----------------------------------------

        if len(lines) >= 2:

            for line in lines[1:]:

                if self._servings_pattern.match(line):

                    data.servings = int(line)

                elif line.startswith("Tag "):

                    data.meal = line

                else:

                    if data.dish is None:
                        data.dish = line
                    else:
                        data.dish += " " + line

        return data