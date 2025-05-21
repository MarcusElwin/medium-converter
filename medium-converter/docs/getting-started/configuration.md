# Configuration

Medium Converter can be configured in several ways to customize its behavior.

## Environment Variables

Medium Converter looks for the following environment variables:

### Authentication

```bash
# Set Medium cookies manually
MEDIUM_SID=your_sid_cookie
MEDIUM_UID=your_uid_cookie

# Disable auto-cookie fetching from browser
MEDIUM_NO_BROWSER_COOKIES=1
```

### LLM Configuration

```bash
# OpenAI
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-4  # Defaults to gpt-3.5-turbo

# Anthropic
ANTHROPIC_API_KEY=your_anthropic_api_key
ANTHROPIC_MODEL=claude-3-sonnet-20240229  # Default is claude-3-haiku-20240307

# Google
GOOGLE_API_KEY=your_google_api_key
GOOGLE_MODEL=gemini-pro  # Default

# Mistral
MISTRAL_API_KEY=your_mistral_api_key
MISTRAL_MODEL=mistral-medium  # Default
```

### Export Options

```bash
# Default output directory
MEDIUM_OUTPUT_DIR=~/Documents/medium-articles

# Default export format
MEDIUM_DEFAULT_FORMAT=pdf
```

## Configuration File

Medium Converter also looks for a configuration file at `~/.medium-converter/config.toml`:

```toml
[general]
default_format = "markdown"
output_dir = "~/Documents/medium-articles"
use_browser_cookies = true

[llm]
provider = "openai"
model = "gpt-3.5-turbo"
temperature = 0.7
api_key = "your_api_key"  # Better to use environment variable

[export.pdf]
page_size = "A4"
font_size = 11
include_images = true

[export.markdown]
syntax_highlighting = true
include_frontmatter = true
```

## CLI Configuration

You can create persistent CLI configuration using the `medium config` command:

```bash
# Set default export format
medium config set default_format pdf

# Set LLM provider
medium config set llm.provider openai

# View current configuration
medium config show

# Reset to defaults
medium config reset
```

## Python API Configuration

When using the Python API, you can pass configuration options directly:

```python
from medium_converter import convert_article
from medium_converter.llm import LLMConfig, LLMProvider

async def main():
    # Configure LLM
    llm_config = LLMConfig(
        provider=LLMProvider.ANTHROPIC,
        model="claude-3-sonnet-20240229",
        temperature=0.5
    )
    
    # Configure export options
    export_options = {
        "include_images": True,
        "syntax_highlighting": True,
        "page_size": "A4",
        "font_size": 11
    }
    
    await convert_article(
        url="https://medium.com/example-article",
        output_format="pdf",
        output_path="article.pdf",
        enhance=True,
        llm_config=llm_config,
        export_options=export_options
    )
```

## Configuration Priority

Medium Converter configuration is applied in the following order (later items override earlier ones):

1. Default values
2. Configuration file
3. Environment variables
4. Direct function arguments or CLI options