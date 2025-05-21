# Installation

Medium Converter is available on PyPI and can be installed using pip.

## Basic Installation

```bash
pip install medium-converter
```

This installs the core package with basic functionality for fetching and converting Medium articles to Markdown format.

## Optional Dependencies

Medium Converter uses optional dependencies to keep the base installation light. You can install additional features using "extras".

### Export Formats

```bash
# For PDF export
pip install medium-converter[pdf]

# For Word DOCX export
pip install medium-converter[word]

# For LaTeX export
pip install medium-converter[latex]

# For EPUB export
pip install medium-converter[epub]

# For HTML export
pip install medium-converter[html]

# For all export formats
pip install medium-converter[all-formats]
```

### LLM Enhancement

```bash
# For basic LLM support (required for any LLM provider)
pip install medium-converter[llm]

# For OpenAI (GPT models)
pip install medium-converter[openai]

# For Anthropic (Claude models)
pip install medium-converter[anthropic]

# For Google (Gemini models)
pip install medium-converter[google]

# For Mistral AI
pip install medium-converter[mistral]

# For local models (via llama-cpp-python)
pip install medium-converter[local]

# For all LLM providers
pip install medium-converter[all-llm]
```

### Development and Documentation

```bash
# For development dependencies
pip install medium-converter[dev]

# For documentation
pip install medium-converter[docs]
```

### All Features

```bash
# Install everything
pip install medium-converter[all]
```

## Installation from Source

If you want to install the latest development version or contribute to the project, you can install from source:

```bash
# Clone the repository
git clone https://github.com/MarcusElwin/medium-converter.git
cd medium-converter

# Install with Poetry
poetry install --all-extras

# Or with pip
pip install -e .
```

## System Requirements

- Python 3.11 or higher
- Windows, macOS, or Linux