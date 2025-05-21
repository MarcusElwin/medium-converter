"""Command-line interface for Medium Converter."""

import click
from rich.console import Console

console = Console()


@click.group()
def main():
    """Convert Medium articles to various formats with LLM enhancement."""
    pass


@main.command()
@click.argument("url")
@click.option("--format", "-f", default="markdown", help="Output format (markdown, pdf, etc.)")
@click.option("--output", "-o", help="Output file path")
@click.option("--enhance/--no-enhance", default=False, help="Use LLM to enhance content")
def convert(url, format, output, enhance):
    """Convert a Medium article to the specified format."""
    console.print(f"[bold green]Converting[/bold green] {url} to {format}")
    console.print("[italic]This functionality will be implemented soon.[/italic]")


if __name__ == "__main__":
    main()