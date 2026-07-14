from megacoocookexcel.parser.reader import PDFReader


def test_reader_exists():

    reader = PDFReader()

    assert reader is not None