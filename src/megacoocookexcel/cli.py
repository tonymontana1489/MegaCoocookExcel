from pathlib import Path

import typer
from rich.console import Console

from megacoocookexcel.parser import PDFReader, PdfTableExtractor

app = typer.Typer(no_args_is_help=True)
console = Console()


@app.command()
def parse(pdf_file: str):
    """
    Explore a Coocook PDF and create a preview of the extracted tables.
    """

    output = []

    output.append("🏕 Mega Coocook Excel")
    output.append("")
    output.append(f"📄 Pages found: {pdf_file}")
    output.append("")

    reader = PDFReader()
    pdf = reader.read(pdf_file)

    output.append(f"Pages found: {len(pdf.pages)}")
    output.append("")

    extractor = PdfTableExtractor()
    tables = extractor.extract(pdf)

    # Fürs Debuggen erst einmal nur die ersten drei Seiten
    for page in tables[:3]:

        output.append("=" * 60)
        output.append(f"Page {page['page']}")
        output.append("=" * 60)

        if not page["tables"]:
            output.append("No tables found")
            output.append("")
            continue

        output.append(f"Tables found: {len(page['tables'])}")
        output.append("")

        for index, table in enumerate(page["tables"], start=1):

            output.append(f"Table {index}: {len(table)} rows")

            if table:
                output.append("Preview:")

                for row in table[:5]:
                    output.append(str(row))

            output.append("")

    pdf.close()

    Path("output").mkdir(exist_ok=True)

    output_file = Path("output/preview.txt")

    with output_file.open("w", encoding="utf-8") as f:
        f.write("\n".join(output))

    console.print(f"[green]Preview written to {output_file}[/green]")


if __name__ == "__main__":
    app()