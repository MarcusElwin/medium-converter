# PDF Export

Medium Converter can export articles to PDF, creating professionally formatted documents that are ready for printing or sharing.

## Installation

PDF export requires additional dependencies:

```bash
pip install medium-converter[pdf]
```

Or if installing everything:

```bash
pip install medium-converter[all]
```

## Basic Usage

### Command Line

```bash
# Convert to PDF
medium convert https://medium.com/example-article -f pdf -o article.pdf
```

### Python API

```python
from medium_converter import convert_article

await convert_article(
    url="https://medium.com/example-article",
    output_format="pdf",
    output_path="article.pdf"
)
```

## Customization Options

PDF export supports various customization options:

| Option | Description | Default |
|--------|-------------|---------|
| `page_size` | Page size (A4, Letter, etc.) | `"A4"` |
| `font_size` | Base font size in points | `11` |
| `font_family` | Font family for text | `"Helvetica"` |
| `margins` | Page margins in inches | `{"top": 1, "right": 1, "bottom": 1, "left": 1}` |
| `include_toc` | Generate table of contents | `True` |
| `include_cover` | Generate cover page | `True` |
| `include_images` | Include images in PDF | `True` |
| `syntax_highlighting` | Enable syntax highlighting for code | `True` |
| `header_text` | Custom header text | `None` |
| `footer_text` | Custom footer text | `None` |
| `page_numbers` | Include page numbers | `True` |

### Command Line

```bash
medium convert https://medium.com/example-article -f pdf \
  --option page_size=Letter \
  --option font_size=12 \
  --option include_cover=true \
  --option header_text="Medium Article" \
  --option footer_text="Generated with Medium Converter"
```

### Python API

```python
await convert_article(
    url="https://medium.com/example-article",
    output_format="pdf",
    output_path="article.pdf",
    export_options={
        "page_size": "Letter",
        "font_size": 12,
        "font_family": "Times-Roman",
        "include_cover": True,
        "header_text": "Medium Article",
        "footer_text": "Generated with Medium Converter"
    }
)
```

## Custom Styling

For advanced styling, you can provide a CSS stylesheet:

```python
custom_css = """
@page {
    @top-center {
        content: "Custom Header";
    }
    @bottom-center {
        content: "Page " counter(page);
    }
}

h1 {
    color: #0066cc;
    font-size: 24pt;
}

pre {
    background-color: #f5f5f5;
    padding: 10pt;
    border-radius: 5pt;
}
"""

await convert_article(
    url="https://medium.com/example-article",
    output_format="pdf",
    output_path="article.pdf",
    export_options={
        "custom_stylesheet": custom_css
    }
)
```

Or provide a stylesheet file:

```python
await convert_article(
    url="https://medium.com/example-article",
    output_format="pdf",
    output_path="article.pdf",
    export_options={
        "stylesheet_path": "path/to/custom.css"
    }
)
```

## PDF Features

The PDF exporter provides several features:

1. **Cover Page**: Title, author, date, and estimated reading time
2. **Table of Contents**: Automatically generated TOC with page numbers
3. **Header and Footer**: Customizable header and footer content
4. **Syntax Highlighting**: Code blocks with syntax highlighting
5. **Hyperlinks**: Active hyperlinks to websites and internal references
6. **Images**: Embedded images with captions
7. **Math Rendering**: LaTeX math formulas rendered properly
8. **Bookmarks**: PDF bookmarks for easy navigation

## Implementation Details

Under the hood, Medium Converter uses ReportLab for PDF generation. The process involves:

1. Parsing the article into a structured document
2. Converting the content to ReportLab's flowable objects
3. Applying styling and formatting
4. Generating the PDF with proper layout

For extremely complex layouts, consider using the LaTeX exporter and converting to PDF with a LaTeX processor.