import typer
from rich.console import Console

from megacoocookexcel.parser import PDFReader, PdfTableExtractor

app = typer.Typer(no_args_is_help=True)
console = Console()


@app.command()
def parse(pdf_file: str):
    """Explore a Coocook PDF."""

    console.print("[bold green]🏕 Mega Coocook Excel[/bold green]")
    console.print()

    reader = PDFReader()
    pdf = reader.read(pdf_file)

    console.print(f"📄 Pages found: {len(pdf.pages)}")
    console.print()

    extractor = PdfTableExtractor()

    tables = extractor.extract(pdf)

    for page in tables:

        console.rule(f"Page {page['page']}")

        console.print(
            f"Tables found: {len(page['tables'])}"
        )

        for index, table in enumerate(page["tables"], start=1):

            console.print(
                f"Table {index}: {len(table)} rows"
            )
            
        if table:
            console.print("[yellow]Preview:[/yellow]")

            for row in table[:5]:
                console.print(row)

        console.print()
    pdf.close()