import pytest

from megacoocookexcel.parser.reader import PDFReader


def test_missing_file():

    reader = PDFReader()

    with pytest.raises(FileNotFoundError):
        reader.read("gibt_es_nicht.pdf")