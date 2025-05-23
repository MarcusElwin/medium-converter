# Medium Converter - Claude Guide

## Project Overview
Medium Converter is a Python tool for fetching, converting, and exporting Medium articles to various formats like Markdown and PDF. It includes LLM-based enhancement capabilities.

## Key Commands

### Development
```bash
# Install dependencies
pip install poetry
poetry install

# Run tests
poetry run pytest

# Type checking
poetry run mypy medium_converter

# Linting
poetry run ruff check .
```

### Documentation
```bash
# Build docs
poetry install --with docs
poetry run mkdocs build

# Serve docs locally
poetry run mkdocs serve
```

### Release Process
The project uses GitHub Actions for automated releases with semantic versioning.

## Project Structure
- `medium_converter/`: Main package
  - `core/`: Core functionality (auth, fetching, parsing)
  - `exporters/`: Output format converters
  - `llm/`: LLM integration for content enhancement
  - `utils/`: Helper utilities
- `tests/`: Unit and integration tests
- `docs/`: Documentation

## Workflows
The project uses GitHub Actions workflows for:
- Semantic versioning and releases
- PyPI publishing
- Documentation deployment
- PR reviews with Claude

## Common Tasks
- Adding new exporters: Create a new class in `exporters/` that inherits from `BaseExporter`
- Adding LLM providers: Add provider configuration in `llm/providers.py`
- Implementing new features: Follow existing patterns and add appropriate tests

## Local Setup
See `docs/getting-started/installation.md` for detailed setup instructions.