"""Command-line interface for Medium Converter."""

import importlib.metadata
import sys
from typing import Optional, List

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.markdown import Markdown

try:
    __version__ = importlib.metadata.version("medium-converter")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.1.0"  # Default during development

console = Console()


def print_banner():
    """Print a fancy banner for the CLI."""
    banner = """
    ╭─────────────────────────────────────────────────╮
    │                                                 │
    │    [bold cyan]Medium Converter[/bold cyan]                           │
    │    [italic]Convert Medium articles to various formats[/italic]   │
    │                                                 │
    ╰─────────────────────────────────────────────────╯
    """
    console.print(banner)


@click.group(invoke_without_command=True)
@click.option("--version", is_flag=True, help="Show the version and exit.")
@click.pass_context
def main(ctx, version):
    """Convert Medium articles to various formats with LLM enhancement.
    
    Medium Converter allows you to download and convert Medium articles to
    different formats, with optional content enhancement using LLMs.
    """
    # Print version and exit if requested
    if version:
        console.print(f"Medium Converter v{__version__}")
        sys.exit(0)
    
    # Show help if no command provided
    if ctx.invoked_subcommand is None:
        print_banner()
        console.print(ctx.get_help())


@main.command()
@click.argument("url")
@click.option("--format", "-f", default="markdown", 
              type=click.Choice(["markdown", "pdf", "html", "latex", "epub", "docx", "text"], 
                               case_sensitive=False),
              help="Output format")
@click.option("--output", "-o", help="Output file path")
@click.option("--output-dir", "-d", help="Output directory (auto-generates filename)")
@click.option("--enhance/--no-enhance", default=False, help="Use LLM to enhance content")
@click.option("--use-cookies/--no-cookies", default=True, help="Use browser cookies for authentication")
@click.option("--llm-provider", 
              type=click.Choice(["openai", "anthropic", "google", "mistral", "local"], 
                               case_sensitive=False),
              help="LLM provider to use for enhancement")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
def convert(url, format, output, output_dir, enhance, use_cookies, llm_provider, verbose):
    """Convert a Medium article to the specified format.
    
    Examples:
        medium convert https://medium.com/example-article
        medium convert https://medium.com/example-article -f pdf -o article.pdf
        medium convert https://medium.com/example-article --enhance --llm-provider openai
    """
    # Show a fancy panel with the conversion info
    info_table = Table.grid(padding=1)
    info_table.add_column(style="cyan", justify="right")
    info_table.add_column(style="white")
    
    info_table.add_row("URL:", url)
    info_table.add_row("Format:", format.upper())
    if output:
        info_table.add_row("Output:", output)
    if output_dir:
        info_table.add_row("Output Directory:", output_dir)
    if enhance:
        provider = llm_provider or "default"
        info_table.add_row("Enhancement:", f"Enabled ({provider})")
    
    console.print(Panel(info_table, title="[bold green]Medium Converter[/bold green]", subtitle="Converting Article"))
    
    # Show a progress spinner
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        progress.add_task("[green]Fetching article...", total=None)
        # This would be where the actual conversion happens
    
    # Print placeholder for now
    console.print("[italic]Article conversion will be implemented in future versions.[/italic]")


@main.command()
@click.argument("file", type=click.Path(exists=True))
@click.option("--format", "-f", default="markdown", 
              type=click.Choice(["markdown", "pdf", "html", "latex", "epub", "docx", "text"], 
                               case_sensitive=False),
              help="Output format")
@click.option("--output-dir", "-d", required=True, help="Output directory for converted files")
@click.option("--enhance/--no-enhance", default=False, help="Use LLM to enhance content")
@click.option("--concurrent", "-c", default=3, help="Maximum number of concurrent downloads")
@click.option("--use-cookies/--no-cookies", default=True, help="Use browser cookies for authentication")
@click.option("--llm-provider", 
              type=click.Choice(["openai", "anthropic", "google", "mistral", "local"], 
                               case_sensitive=False),
              help="LLM provider to use for enhancement")
def batch(file, format, output_dir, enhance, concurrent, use_cookies, llm_provider):
    """Convert multiple Medium articles listed in a file.
    
    The input file should contain one Medium URL per line.
    
    Examples:
        medium batch articles.txt -f pdf -d ./articles
        medium batch articles.txt -d ./articles --enhance -c 5
    """
    console.print(Panel(f"Batch Processing: {file}", subtitle=f"Output Directory: {output_dir}"))
    
    # Placeholder code to read URLs
    with open(file, "r") as f:
        urls = [line.strip() for line in f if line.strip()]
    
    console.print(f"Found [bold]{len(urls)}[/bold] URLs to process")
    console.print("[italic]Batch conversion will be implemented in future versions.[/italic]")


@main.command(name="config")
@click.argument("action", type=click.Choice(["show", "set", "get", "reset"]))
@click.argument("key", required=False)
@click.argument("value", required=False)
def config_cmd(action, key, value):
    """Manage configuration settings.
    
    Examples:
        medium config show
        medium config set default_format pdf
        medium config get llm.provider
        medium config reset
    """
    if action == "show":
        # Example configuration table
        config_table = Table(title="Configuration")
        config_table.add_column("Key", style="cyan")
        config_table.add_column("Value", style="green")
        
        # These would be actual configuration values
        config_table.add_row("default_format", "markdown")
        config_table.add_row("output_dir", "~/Documents/medium-articles")
        config_table.add_row("use_browser_cookies", "true")
        config_table.add_row("llm.provider", "openai")
        
        console.print(config_table)
    else:
        console.print("[italic]Configuration management will be implemented in future versions.[/italic]")


@main.command()
def list_formats():
    """List all available export formats with details."""
    formats_table = Table(title="Available Export Formats")
    formats_table.add_column("Format", style="cyan")
    formats_table.add_column("Description", style="white")
    formats_table.add_column("Extension", style="green")
    formats_table.add_column("Dependencies", style="yellow")
    
    formats_table.add_row(
        "Markdown", "Plain text format with lightweight markup", 
        ".md", "None (built-in)"
    )
    formats_table.add_row(
        "PDF", "Portable Document Format for high-quality prints", 
        ".pdf", "reportlab"
    )
    formats_table.add_row(
        "HTML", "Web page format with styling", 
        ".html", "jinja2"
    )
    formats_table.add_row(
        "LaTeX", "Professional typesetting system", 
        ".tex", "jinja2"
    )
    formats_table.add_row(
        "EPUB", "Electronic publication for e-readers", 
        ".epub", "ebooklib"
    )
    formats_table.add_row(
        "DOCX", "Microsoft Word document", 
        ".docx", "python-docx"
    )
    formats_table.add_row(
        "Text", "Plain text without formatting", 
        ".txt", "None (built-in)"
    )
    
    console.print(formats_table)


@main.command()
def list_providers():
    """List all available LLM providers with details."""
    providers_table = Table(title="Available LLM Providers")
    providers_table.add_column("Provider", style="cyan")
    providers_table.add_column("Models", style="white")
    providers_table.add_column("Features", style="green")
    providers_table.add_column("Dependencies", style="yellow")
    
    providers_table.add_row(
        "OpenAI", "GPT-3.5-Turbo, GPT-4", 
        "High quality, widely used", "openai"
    )
    providers_table.add_row(
        "Anthropic", "Claude 3 (Haiku, Sonnet, Opus)", 
        "Long context, high quality", "anthropic"
    )
    providers_table.add_row(
        "Google", "Gemini Pro, Gemini Pro Vision", 
        "Competitive pricing", "google-generativeai"
    )
    providers_table.add_row(
        "Mistral", "Mistral Small, Medium, Large", 
        "Good performance, reasonable cost", "mistralai"
    )
    providers_table.add_row(
        "Local", "Various open-source models via GGUF", 
        "Privacy, no API costs", "llama-cpp-python"
    )
    
    console.print(providers_table)


@main.command()
def info():
    """Display system information and environment details."""
    import platform
    import os
    
    info_table = Table(title="System Information")
    info_table.add_column("Item", style="cyan")
    info_table.add_column("Value", style="green")
    
    info_table.add_row("Medium Converter Version", __version__)
    info_table.add_row("Python Version", platform.python_version())
    info_table.add_row("Operating System", platform.system() + " " + platform.release())
    info_table.add_row("Platform", platform.platform())
    
    # Environment variables
    env_vars = {
        "OPENAI_API_KEY": "✓" if os.environ.get("OPENAI_API_KEY") else "✗",
        "ANTHROPIC_API_KEY": "✓" if os.environ.get("ANTHROPIC_API_KEY") else "✗",
        "GOOGLE_API_KEY": "✓" if os.environ.get("GOOGLE_API_KEY") else "✗",
        "MISTRAL_API_KEY": "✓" if os.environ.get("MISTRAL_API_KEY") else "✗",
    }
    
    for key, value in env_vars.items():
        info_table.add_row(f"ENV: {key}", value)
    
    console.print(info_table)


@main.command()
def examples():
    """Show example usage of Medium Converter."""
    examples_md = """
    # Examples
    
    ## Basic conversion
    ```bash
    medium convert https://medium.com/example-article
    ```
    
    ## Convert to PDF
    ```bash
    medium convert https://medium.com/example-article -f pdf -o article.pdf
    ```
    
    ## Convert with LLM enhancement
    ```bash
    medium convert https://medium.com/example-article --enhance --llm-provider openai
    ```
    
    ## Batch conversion
    ```bash
    medium batch articles.txt -f markdown -d ./articles
    ```
    
    ## Configuration
    ```bash
    medium config set default_format pdf
    ```
    """
    
    console.print(Panel(Markdown(examples_md), title="Example Usage"))


if __name__ == "__main__":
    main()