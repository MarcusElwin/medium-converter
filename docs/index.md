# Medium Converter

<div class="grid cards" markdown>

- 📚 **Simple to use**  
  Convert Medium articles to various formats with minimal configuration

- 📄 **Multiple formats**  
  Export to Markdown, PDF, HTML, EPUB, LaTeX, and DOCX

- 🤖 **LLM enhancement**  
  Improve article text with AI-powered grammar and clarity improvements

- 🔓 **Paywall access**  
  Use your browser cookies to access articles behind the paywall 

</div>

## Overview

Medium Converter is a Python package that allows you to download Medium articles and convert them to various formats. It's designed to be easy to use while offering powerful features for advanced users.

```python
import asyncio
from medium_converter import convert_article

async def main():
    await convert_article(
        url="https://medium.com/example-article",
        output_format="markdown",
        output_path="article.md",
        enhance=True  # Use LLM enhancement
    )

if __name__ == "__main__":
    asyncio.run(main())
```

## Key Features

- **📑 Multiple export formats**: Convert to Markdown, PDF, HTML, EPUB, LaTeX, and DOCX
- **🤖 LLM enhancement**: Improve clarity and fix grammar with AI
- **🔓 Paywall access**: Use your browser cookies to access articles behind the paywall
- **⚡ Async processing**: Convert multiple articles in parallel
- **💻 Cross-platform**: Works on Windows, macOS, and Linux

## Installation

```bash
pip install medium-converter
```

For additional features:

```bash
# For PDF export
pip install medium-converter[pdf]

# For LLM enhancement with OpenAI
pip install medium-converter[llm,openai]

# For all features
pip install medium-converter[all]
```

## Command Line Interface

Medium Converter provides a beautiful command-line interface with emojis and colors:

```bash
# Basic conversion
medium convert https://medium.com/example-article

# Convert to PDF with enhancement
medium convert https://medium.com/example-article -f pdf --enhance

# Batch processing
medium batch articles.txt -d ./output-dir
```

## Quick Links

- [Installation guide](getting-started/installation.md)
- [Quick start](getting-started/quickstart.md)
- [CLI usage](user-guide/cli.md)
- [Python API](user-guide/python-api.md)
- [GitHub repository](https://github.com/MarcusElwin/medium-converter)

## License

Medium Converter is released under the [MIT License](https://github.com/MarcusElwin/medium-converter/blob/main/LICENSE).