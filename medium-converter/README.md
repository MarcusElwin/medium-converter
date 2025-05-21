# Medium Converter

[![PyPI version](https://img.shields.io/pypi/v/medium-converter.svg)](https://pypi.org/project/medium-converter/)
[![Python versions](https://img.shields.io/pypi/pyversions/medium-converter.svg)](https://pypi.org/project/medium-converter/)
[![License](https://img.shields.io/github/license/MarcusElwin/medium-converter.svg)](https://github.com/MarcusElwin/medium-converter/blob/main/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/medium-converter/badge/?version=latest)](https://medium-converter.readthedocs.io/)

**Convert Medium articles to various formats with optional LLM enhancement.**

## Features

- =Ú **Multiple export formats**: Markdown, PDF, HTML, LaTeX, EPUB, DOCX
- > **LLM enhancement**: Improve clarity and fix grammar with AI
- = **Paywall access**: Use your browser cookies to access articles behind the paywall
- <¨ **Custom styling**: Customize the output appearance
- ¡ **Async processing**: Efficient batch conversion

## Installation

```bash
# Basic installation
pip install medium-converter

# With PDF support
pip install medium-converter[pdf]

# With LLM enhancement using OpenAI
pip install medium-converter[llm,openai]

# All features
pip install medium-converter[all]
```

## Quick Start

### Command Line

```bash
# Convert to Markdown (default)
medium convert https://medium.com/example-article

# Convert to PDF with enhancement
medium convert https://medium.com/example-article -f pdf --enhance
```

### Python API

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

## Documentation

For detailed documentation, visit [medium-converter.readthedocs.io](https://medium-converter.readthedocs.io/).

## LLM Providers

Medium Converter supports multiple LLM providers for content enhancement:

- OpenAI (GPT models)
- Anthropic (Claude models)
- Google (Gemini models)
- Mistral AI
- Local models (via llama-cpp-python)

## License

MIT License - See [LICENSE](LICENSE) for details.

## Development

```bash
# Clone the repository
git clone https://github.com/MarcusElwin/medium-converter.git
cd medium-converter

# Install development dependencies
poetry install --all-extras

# Run tests
poetry run pytest

# Build documentation
poetry run mkdocs build
```