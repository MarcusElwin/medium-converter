# Quick Start

This guide will help you get started with Medium Converter quickly.

## Basic Usage

### Command Line

The simplest way to use Medium Converter is through the command line:

```bash
# Convert to Markdown (default)
medium convert https://medium.com/example-article

# Convert to PDF
medium convert https://medium.com/example-article -f pdf -o article.pdf

# Convert with LLM enhancement
medium convert https://medium.com/example-article --enhance
```

### Python API

Medium Converter can also be used as a Python library:

```python
import asyncio
from medium_converter import convert_article

async def main():
    # Basic conversion
    await convert_article(
        url="https://medium.com/example-article",
        output_format="markdown",
        output_path="article.md"
    )
    
    # With enhancement
    await convert_article(
        url="https://medium.com/example-article",
        output_format="pdf",
        output_path="article.pdf",
        enhance=True
    )

if __name__ == "__main__":
    asyncio.run(main())
```

## Common Options

### Export Formats

Medium Converter supports various export formats:

- `markdown` (default): Converts to Markdown format
- `pdf`: Generates a PDF document
- `html`: Creates an HTML file
- `latex`: Produces LaTeX source
- `epub`: Creates an EPUB e-book
- `docx`: Generates a Word document

### Access Paywalled Articles

Medium Converter can use your browser cookies to access articles behind the paywall:

```bash
# Using command line
medium convert https://medium.com/example-article --use-cookies

# Using Python
await convert_article(
    url="https://medium.com/example-article",
    use_cookies=True
)
```

### LLM Enhancement

You can enhance the article content using LLMs:

```bash
# Using command line
medium convert https://medium.com/example-article --enhance --llm-provider openai

# Using Python
await convert_article(
    url="https://medium.com/example-article",
    enhance=True,
    llm_config={
        "provider": "openai",
        "model": "gpt-3.5-turbo"
    }
)
```

## Next Steps

- Learn more about [CLI usage](../user-guide/cli.md)
- Explore the [Python API](../user-guide/python-api.md)
- Understand [authentication](../user-guide/auth.md) for paywalled articles
- Configure [LLM enhancement](../user-guide/llm/overview.md)