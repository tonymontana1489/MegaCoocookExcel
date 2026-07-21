import datetime

from megacoocookexcel.parser import ShoppingItemMapper


def test_map_row():

    mapper = ShoppingItemMapper()

    row = [
        "1.12 Liter",
        "Buttermilch",
        "1.12 Liter\nSalatsoße Buttermilch-Zitrone\n1\nTag 1 (Sonntag)",
        "Sun, 2026-08-09",
    ]

    item = mapper.map_row(row)

    assert item is not None

    assert item.article == "Buttermilch"

    assert item.total_amount == 1.12
    assert item.total_unit == "Liter"

    assert item.recipe_amount == 1.12
    assert item.recipe_unit == "Liter"

    assert item.dish == "Salatsoße Buttermilch-Zitrone"

    assert item.servings == 1

    assert item.meal == "Tag 1 (Sonntag)"

    assert item.date == datetime.date(2026, 8, 9)