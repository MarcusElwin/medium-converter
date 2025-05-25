# Exporters Overview

Medium Converter provides a variety of exporters to convert articles into different formats. Each exporter is specialized for a specific output format and has its own features and requirements.

## Available Exporters

| Format | Description | File Extension | Dependencies | Package Extra |
|--------|-------------|----------------|--------------|---------------|
| Markdown | Plain text format with lightweight markup | .md | None (built-in) | - |
| PDF | Portable Document Format for high-quality prints | .pdf | reportlab | pdf |
| DOCX | Microsoft Word document | .docx | python-docx | word |
| HTML | Web page format with styling | .html | jinja2 | html |
| LaTeX | Professional typesetting system | .tex | jinja2 | latex |
| EPUB | Electronic publication for e-readers | .epub | ebooklib | epub |
| Text | Plain text without formatting | .txt | None (built-in) | - |

## Installing Dependencies

To use a specific exporter, you need to install the required dependencies. You can do this using the package extras:

```bash
# For a single format
pip install medium-converter[pdf]
pip install medium-converter[word]

# For multiple formats
pip install medium-converter[pdf,word,html]

# For all exporters
pip install medium-converter[all-formats]

# For all features (including LLM)
pip install medium-converter[all]
```

## Using Exporters

### Command Line

```bash
# Convert using a specific format
medium convert https://medium.com/example-article -f markdown
medium convert https://medium.com/example-article -f pdf -o article.pdf
medium convert https://medium.com/example-article -f docx -o article.docx
```

### Python API

```python
import asyncio
from medium_converter import convert_article

async def main():
    # Convert to Markdown
    await convert_article(
        url="https://medium.com/example-article",
        output_format="markdown",
        output_path="article.md"
    )
    
    # Convert to PDF
    await convert_article(
        url="https://medium.com/example-article",
        output_format="pdf",
        output_path="article.pdf"
    )
    
    # Convert to DOCX
    await convert_article(
        url="https://medium.com/example-article",
        output_format="docx",
        output_path="article.docx"
    )

if __name__ == "__main__":
    asyncio.run(main())
```

## Creating Custom Exporters

You can create your own exporters by extending the `BaseExporter` class:

```python
from medium_converter.exporters.base import BaseExporter
from medium_converter.core.models import Article

class CustomExporter(BaseExporter):
    """A custom exporter."""
    
    def export(self, article: Article, output=None):
        """Export article to a custom format."""
        # Your implementation here
        content = f"Title: {article.title}\nAuthor: {article.author}\n\n"
        
        # Add content
        # ...
        
        # Handle output
        if output:
            if isinstance(output, str):
                with open(output, 'w') as f:
                    f.write(content)
            else:
                output.write(content)
                
        return content
```

## Common Features

All exporters support:

- Article metadata (title, author, date)
- Content formatting (headings, paragraphs, etc.)
- File output (to a file path or file-like object)
- Customizable output

## Format-Specific Features

Each format offers unique advantages:

- **Markdown**: Lightweight, readable plain text
- **PDF**: Professional printing quality with precise layout control
- **DOCX**: Compatible with Microsoft Office and other word processors
- **HTML**: Web compatibility with CSS styling
- **LaTeX**: Academic publications with mathematical typesetting
- **EPUB**: E-reader compatibility for digital books
- **Text**: Maximum compatibility with any text editor

See the individual format pages for more detailed information about each exporter.