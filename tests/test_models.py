from megacoocookexcel.models import ShoppingItem


def test_create_shopping_item():
    item = ShoppingItem(
        article="Kartoffeln",
        total_amount=22,
        total_unit="kg",
        recipe_amount=2.2,
        recipe_unit="kg",
        dish="Kartoffelsalat",
        servings=100,
    )

    assert item.article == "Kartoffeln"
    assert item.total_amount == 22
    assert item.total_unit == "kg"
    assert item.recipe_amount == 2.2
    assert item.recipe_unit == "kg"
    assert item.dish == "Kartoffelsalat"
    assert item.servings == 100