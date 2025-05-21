# Development Guide

This guide will help you set up a development environment for working on Medium Converter.

## Prerequisites

- Python 3.11 or newer
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management
- [Git](https://git-scm.com/downloads) for version control

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/MarcusElwin/medium-converter.git
cd medium-converter
```

### Install Dependencies

```bash
# Install all dependencies including development tools
poetry install --all-extras

# Or without optional dependencies
poetry install
```

### Activate the Virtual Environment

```bash
poetry shell
```

## Project Structure

```
medium-converter/
├── medium_converter/            # Main package
│   ├── __init__.py              # Public API & version
│   ├── cli.py                   # CLI interface
│   ├── core/                    # Core functionality
│   │   ├── __init__.py
│   │   ├── fetcher.py           # HTTP client
│   │   ├── parser.py            # HTML parsing
│   │   ├── auth.py              # Authentication
│   │   └── models.py            # Data models
│   ├── exporters/               # Format exporters 
│   │   ├── __init__.py
│   │   ├── base.py              # Base exporter
│   │   ├── markdown.py          # Markdown exporter
│   │   └── ...
│   ├── llm/                     # LLM integration
│   │   ├── __init__.py
│   │   ├── config.py            # Configuration
│   │   ├── enhancer.py          # Content enhancement
│   │   └── ...
│   └── utils/                   # Utilities
│       ├── __init__.py
│       └── helpers.py           # Helper functions
├── tests/                       # Test suite
│   ├── conftest.py              # Test fixtures
│   ├── unit/                    # Unit tests
│   └── integration/             # Integration tests
├── docs/                        # Documentation
├── examples/                    # Example scripts
├── pyproject.toml               # Project configuration
└── README.md                    # Project readme
```

## Development Workflow

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=medium_converter

# Run specific test file
pytest tests/unit/test_models.py
```

### Code Style and Linting

The project uses Black, Ruff, and MyPy for code quality:

```bash
# Format code with Black
black medium_converter tests

# Run linter
ruff medium_converter tests

# Run type checks
mypy medium_converter
```

### Building Documentation

```bash
# Build documentation
mkdocs build

# Serve documentation locally
mkdocs serve
```

## Adding Features

### Adding a New Exporter

1. Create a new file in `medium_converter/exporters/` (e.g., `html.py`)
2. Implement the exporter class that inherits from `BaseExporter`
3. Implement the required methods (especially `export()`)
4. Register the format in `medium_converter/cli.py`
5. Add tests in `tests/unit/exporters/`
6. Add documentation in `docs/user-guide/formats/`

Example:

```python
# medium_converter/exporters/html.py
from typing import Optional, Union, TextIO
from .base import BaseExporter
from ..core.models import Article

class HTMLExporter(BaseExporter):
    """Export Medium articles to HTML format."""
    
    def export(self, article: Article, output: Optional[Union[str, TextIO]] = None) -> str:
        """Export an article to HTML.
        
        Args:
            article: The article to export
            output: Optional output file path or file-like object
            
        Returns:
            The exported content as string
        """
        # Implementation here
        html_content = f"<!DOCTYPE html>\n<html>\n<head>\n<title>{article.title}</title>\n</head>\n<body>\n"
        # ... more implementation
        
        # Write to file if specified
        if output:
            if isinstance(output, str):
                with open(output, 'w', encoding='utf-8') as f:
                    f.write(html_content)
            else:
                output.write(html_content)
        
        return html_content
```

### Adding a New LLM Provider

1. Create or modify the provider implementation in `medium_converter/llm/providers.py`
2. Add the provider to the `LLMProvider` enum in `medium_converter/llm/config.py`
3. Implement the client class that inherits from `LLMClient`
4. Update the `get_llm_client` function to include your provider
5. Add relevant tests
6. Add documentation

## Submitting Changes

1. Create a new branch: `git checkout -b feature/your-feature-name`
2. Make your changes and commit them with descriptive messages
3. Run tests to ensure everything is working
4. Push your branch: `git push origin feature/your-feature-name`
5. Create a pull request on GitHub

## Release Process

1. Update version in `pyproject.toml`
2. Update changelog with your changes
3. Run the release script: `./scripts/publish.sh`
4. Create a new release on GitHub

## Code Conventions

- Use [Google style docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Write comprehensive tests for new features
- Keep functions small and focused
- Document all public APIs
- Use type hints for all functions and methods