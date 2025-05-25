# Other Export Formats

In addition to [Markdown](markdown.md) and [PDF](pdf.md), Medium Converter supports several other export formats. For a comprehensive overview of all exporters, see the [Exporters Overview](exporters-overview.md) page.

## HTML

### Installation

```bash
pip install medium-converter[html]
```

### Usage

```bash
# Command Line
medium convert https://medium.com/example-article -f html -o article.html

# Python API
await convert_article(
    url="https://medium.com/example-article",
    output_format="html",
    output_path="article.html"
)
```

### Options

| Option | Description | Default |
|--------|-------------|--------|
| `template` | HTML template to use | `"default"` |
| `include_css` | Include CSS in the HTML file | `True` |
| `include_images` | Download and include images | `True` |
| `syntax_highlighting` | Enable syntax highlighting | `True` |
| `make_responsive` | Make the HTML responsive | `True` |

## LaTeX

### Installation

```bash
pip install medium-converter[latex]
```

### Usage

```bash
# Command Line
medium convert https://medium.com/example-article -f latex -o article.tex

# Python API
await convert_article(
    url="https://medium.com/example-article",
    output_format="latex",
    output_path="article.tex"
)
```

### Options

| Option | Description | Default |
|--------|-------------|--------|
| `document_class` | LaTeX document class | `"article"` |
| `include_preamble` | Include LaTeX preamble | `True` |
| `include_packages` | Include required packages | `True` |
| `use_listings` | Use listings package for code | `True` |

## EPUB

### Installation

```bash
pip install medium-converter[epub]
```

### Usage

```bash
# Command Line
medium convert https://medium.com/example-article -f epub -o article.epub

# Python API
await convert_article(
    url="https://medium.com/example-article",
    output_format="epub",
    output_path="article.epub"
)
```

### Options

| Option | Description | Default |
|--------|-------------|--------|
| `cover_image` | Path to cover image | `None` |
| `language` | EPUB language code | `"en"` |
| `publisher` | Publisher name | `"Medium Converter"` |
| `include_toc` | Include table of contents | `True` |

## DOCX (Word)

### Installation

```bash
pip install medium-converter[word]
```

### Usage

```bash
# Command Line
medium convert https://medium.com/example-article -f docx -o article.docx

# Python API
await convert_article(
    url="https://medium.com/example-article",
    output_format="docx",
    output_path="article.docx"
)
```

### Options

| Option | Description | Default |
|--------|-------------|--------|
| `template` | Path to DOCX template | `None` |
| `heading_style` | Style for headings | `"Heading {level}"` |
| `paragraph_style` | Style for paragraphs | `"Normal"` |
| `code_style` | Style for code blocks | `"Code"` |

## Plain Text

### Usage

```bash
# Command Line
medium convert https://medium.com/example-article -f text -o article.txt

# Python API
await convert_article(
    url="https://medium.com/example-article",
    output_format="text",
    output_path="article.txt"
)
```

### Options

| Option | Description | Default |
|--------|-------------|--------|
| `width` | Line width in characters | `80` |
| `include_metadata` | Include article metadata | `True` |
| `indent_code` | Indent code blocks | `True` |

## Custom Formats

You can create custom exporters by extending the `BaseExporter` class:

```python
from medium_converter.exporters.base import BaseExporter
from medium_converter.core.models import Article
from typing import Optional, Union, TextIO, BinaryIO

class MyCustomExporter(BaseExporter):
    def export(self, article: Article, output: Optional[Union[str, TextIO, BinaryIO]] = None) -> str:
        # Implement your custom export logic here
        content = f"Title: {article.title}\nAuthor: {article.author}\n\n"
        
        # Add content blocks
        for item in article.content:
            # Process content based on type
            content += process_item(item) + "\n\n"
        
        # Write to output if specified
        if output:
            if isinstance(output, str):
                with open(output, 'w') as f:
                    f.write(content)
            else:
                output.write(content)
                
        return content
```

Then register your exporter:

```python
from medium_converter.exporters import register_exporter

register_exporter("custom", MyCustomExporter)
```

Now you can use your custom format:

```python
await convert_article(
    url="https://medium.com/example-article",
    output_format="custom",
    output_path="article.custom"
)
```