from megacoocookexcel.models import ShoppingItem


def test_create_shopping_item():

    item = ShoppingItem(
        artikel="Kartoffeln",
        menge=22,
        einheit="kg",
        gericht="Kartoffelsalat",
        personen=100,
    )

    assert item.artikel == "Kartoffeln"
    assert item.menge == 22
    assert item.einheit == "kg"
    assert item.personen == 100