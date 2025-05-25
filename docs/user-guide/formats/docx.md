# DOCX Format

Medium Converter allows you to export articles to Microsoft Word DOCX format, providing compatibility with one of the most widely used document formats.

## Features

- Complete article conversion with proper formatting
- Headings with proper hierarchy
- Text formatting and styles
- Code blocks with monospace font
- Lists (both ordered and unordered)
- Image support with captions
- Block quotes using Word's quote style
- Metadata including title, author, and publication date

## Installation

To enable DOCX export, you need to install the `python-docx` dependency:

```bash
pip install medium-converter[word]
```

Or if you want all features:

```bash
pip install medium-converter[all]
```

## Usage

### Command Line

```bash
# Export a Medium article to DOCX format
medium convert https://medium.com/example-article -f docx -o article.docx
```

### Python API

```python
import asyncio
from medium_converter import convert_article

async def main():
    await convert_article(
        url="https://medium.com/example-article",
        output_format="docx",
        output_path="article.docx"
    )

if __name__ == "__main__":
    asyncio.run(main())
```

## Document Structure

The DOCX exporter creates documents with the following structure:

1. **Title**: The article title centered at the top in large font
2. **Byline**: Author and publication date
3. **Tags**: If available, shown as hashtags
4. **Reading Time**: If available, shown in italics
5. **Content**: The main article content
   - Sections with proper heading levels
   - Paragraphs with standard formatting
   - Code blocks in monospace font
   - Images with captions
   - Quotes with the Word "Quote" style
   - Lists with proper formatting

## Customization

Currently, the DOCX exporter uses standard Word styles and formatting. Future versions may include options for customizing styles, templates, and additional formatting options.

## Limitations

- Remote images are not automatically downloaded; they are replaced with a placeholder
- Complex formatting in tables is not fully supported
- Some Medium-specific features may not have direct equivalents in Word