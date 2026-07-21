from megacoocookexcel.parser.column_parser import ColumnParser


def test_parse_column():

    parser = ColumnParser()

    text = """
1.12 Liter
Salatsoße Buttermilch-Zitrone
1
Tag 1 (Sonntag)
"""

    result = parser.parse(text)

    assert result.recipe_amount == 1.12
    assert result.recipe_unit == "Liter"
    assert result.dish == "Salatsoße Buttermilch-Zitrone"
    assert result.servings == 1
    assert result.meal == "Tag 1 (Sonntag)"