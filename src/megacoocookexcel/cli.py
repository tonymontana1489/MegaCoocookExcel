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

    repository.save(articles)

    console.print(
        f"[green]✔ Imported {len(articles)} articles[/green]"
    )

    console.print(
        "[green]✔ Saved to data/articles.json[/green]"
    )

    console.print()