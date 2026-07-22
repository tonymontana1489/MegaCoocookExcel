from pathlib import Path

import typer
from rich.console import Console

from megacoocookexcel.importer import (
    ArticleImporter,
    ArticleRepository,
)
from megacoocookexcel.parser import (
    PDFReader,
    PdfTableExtractor,
)

app = typer.Typer(
    no_args_is_help=True,
)

console = Console()


# -----------------------------------------------------------------------------
# Preview
# -----------------------------------------------------------------------------


def build_preview(pdf_file: str) -> list[str]:
    """
    Build a human-readable preview of the extracted PDF tables.
    """

    output: list[str] = []

    output.append("🏕 Mega Coocook Excel")
    output.append("")
    output.append(f"📄 File: {pdf_file}")
    output.append("")

    reader = PDFReader()
    pdf = reader.read(pdf_file)

    try:

        output.append(f"Pages found: {len(pdf.pages)}")
        output.append("")

        extractor = PdfTableExtractor()
        pages = extractor.extract(pdf)

        for page in pages[:3]:

            output.append("=" * 70)
            output.append(f"Page {page['page']}")
            output.append("=" * 70)

            if not page["tables"]:
                output.append("No tables found")
                output.append("")
                continue

            output.append(f"Tables found: {len(page['tables'])}")
            output.append("")

            for table_number, table in enumerate(
                page["tables"],
                start=1,
            ):

                output.append("-" * 70)
                output.append(f"Table {table_number}")
                output.append("-" * 70)

                output.append(f"Rows: {len(table)}")
                output.append("")

                for row_number, row in enumerate(
                    table[:5],
                    start=1,
                ):

                    output.append(f"Row {row_number}")

                    for column_number, value in enumerate(
                        row,
                        start=1,
                    ):

                        output.append(
                            f"  Column {column_number}: {repr(value)}"
                        )

                    output.append("")

    finally:
        pdf.close()

    return output


def write_preview(
    output: list[str],
) -> Path:
    """
    Write the preview to disk.
    """

    output_directory = Path("output")
    output_directory.mkdir(exist_ok=True)

    output_file = output_directory / "preview.txt"

    output_file.write_text(
        "\n".join(output),
        encoding="utf-8",
    )

    return output_file


# -----------------------------------------------------------------------------
# Commands
# -----------------------------------------------------------------------------


@app.command()
def parse(
    pdf_file: str,
):
    """
    Explore a Coocook PDF and create a preview of the extracted tables.
    """

    output = build_preview(pdf_file)

    output_file = write_preview(output)

    console.print(
        f"[green]✔ Preview written to:[/green] {output_file}"
    )


@app.command("import-articles")
def import_articles(
    pdf_file: str,
):
    """
    Import the Coocook article master data.
    """

    console.print()

    console.print(
        "[bold cyan]Importing article master data...[/bold cyan]"
    )

    importer = ArticleImporter()
    repository = ArticleRepository()

    articles = importer.import_pdf(pdf_file)

    output_file = Path(
        "src/megacoocookexcel/config/articles.json"
    )

    repository.save(
        articles,
        output_file,
    )

    console.print(
        f"[green]✔ Imported {len(articles)} articles[/green]"
    )

    console.print(
        f"[green]✔ Saved to {output_file}[/green]"
    )

    console.print()


if __name__ == "__main__":
    app()