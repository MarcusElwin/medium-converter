# Medium Converter

[![PyPI version](https://img.shields.io/pypi/v/medium-converter.svg)](https://pypi.org/project/medium-converter/)
[![Python versions](https://img.shields.io/pypi/pyversions/medium-converter.svg)](https://pypi.org/project/medium-converter/)
[![PyPI implementation](https://img.shields.io/pypi/implementation/medium-converter.svg)](https://pypi.org/project/medium-converter/)
[![PyPI status](https://img.shields.io/pypi/status/medium-converter.svg)](https://pypi.org/project/medium-converter/)
[![PyPI downloads](https://img.shields.io/pypi/dm/medium-converter.svg)](https://pypi.org/project/medium-converter/)
[![License](https://img.shields.io/github/license/MarcusElwin/medium-converter.svg)](https://github.com/MarcusElwin/medium-converter/blob/main/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/medium-converter/badge/?version=latest)](https://medium-converter.readthedocs.io/)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/badge/ruff-checked-brightgreen)](https://github.com/astral-sh/ruff)
[![Mypy: checked](https://img.shields.io/badge/mypy-checked-blue)](https://github.com/python/mypy)
[![codecov](https://codecov.io/gh/MarcusElwin/medium-converter/branch/main/graph/badge.svg)](https://codecov.io/gh/MarcusElwin/medium-converter)
[![Formats](https://img.shields.io/badge/formats-MD%20|%20PDF%20|%20DOCX%20|%20HTML%20|%20EPUB%20|%20LaTeX-blue)](https://medium-converter.readthedocs.io/en/latest/user-guide/formats/exporters-overview/)

[![Tests](https://github.com/MarcusElwin/medium-converter/actions/workflows/pull-request.yml/badge.svg)](https://github.com/MarcusElwin/medium-converter/actions/workflows/pull-request.yml)
[![Release](https://github.com/MarcusElwin/medium-converter/actions/workflows/release.yml/badge.svg)](https://github.com/MarcusElwin/medium-converter/actions/workflows/release.yml)
[![Docs](https://github.com/MarcusElwin/medium-converter/actions/workflows/docs.yml/badge.svg)](https://github.com/MarcusElwin/medium-converter/actions/workflows/docs.yml)
[![Semantic Release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/MarcusElwin/medium-converter/graphs/commit-activity)
[![GitHub last commit](https://img.shields.io/github/last-commit/MarcusElwin/medium-converter.svg)](https://github.com/MarcusElwin/medium-converter/commits/main)
[![GitHub issues](https://img.shields.io/github/issues/MarcusElwin/medium-converter.svg)](https://github.com/MarcusElwin/medium-converter/issues)
[![GitHub stars](https://img.shields.io/github/stars/MarcusElwin/medium-converter.svg)](https://github.com/MarcusElwin/medium-converter/stargazers)
[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/MarcusElwin/medium-converter.svg)](https://github.com/MarcusElwin/medium-converter)

**Convert Medium articles to various formats with optional LLM enhancement.**

## Features

- 📚 **Multiple export formats**: Markdown, PDF, HTML, LaTeX, EPUB, DOCX
- 🤖 **LLM enhancement**: Improve clarity and fix grammar with AI
- 🔓 **Paywall access**: Use your browser cookies to access articles behind the paywall
- 🎨 **Custom styling**: Customize the output appearance
- ⚡ **Async processing**: Efficient batch conversion

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

## Development Guide

### Prerequisites

- Python 3.11+
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/MarcusElwin/medium-converter.git
cd medium-converter

# Install dependencies with Poetry
poetry install --all-extras

# Activate virtual environment
poetry shell
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=medium_converter
```

### Code Quality

```bash
# Run type checking
mypy medium_converter

# Run linting
ruff medium_converter

# Format code
black medium_converter
```

### Building Documentation

```bash
# Build documentation
mkdocs build

# Serve documentation locally
mkdocs serve
```

## Project Structure

```
medium-converter/
├── medium_converter/       # Main package
│   ├── __init__.py         # Public API & version
│   ├── cli.py              # CLI interface
│   ├── core/               # Core functionality
│   ├── exporters/          # Export formats
│   ├── llm/                # LLM integration
│   └── utils/              # Utilities
├── tests/                  # Test suite
├── docs/                   # Documentation
├── examples/               # Example scripts
├── pyproject.toml          # Project configuration
└── README.md               # Project readme
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

See [Contributing Guide](https://medium-converter.readthedocs.io/en/latest/contributing/development/) for more details.

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