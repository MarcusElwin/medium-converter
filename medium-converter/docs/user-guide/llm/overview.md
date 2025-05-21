# LLM Enhancement Overview

Medium Converter includes an optional feature to enhance article content using Large Language Models (LLMs). This enhancement can improve readability, clarity, and grammar while preserving the original meaning.

## What LLM Enhancement Does

When enabled, LLM enhancement:

1. Fixes grammar and spelling errors
2. Improves sentence structure and flow
3. Makes technical explanations clearer
4. Enhances overall readability
5. Preserves the original meaning and intent
6. Maintains the author's voice and style

## Installation

LLM enhancement requires additional dependencies:

```bash
# Core LLM dependencies
pip install medium-converter[llm]

# Provider-specific dependencies
pip install medium-converter[openai]  # For OpenAI models
pip install medium-converter[anthropic]  # For Anthropic Claude models
pip install medium-converter[google]  # For Google Gemini models
pip install medium-converter[mistral]  # For Mistral AI models
pip install medium-converter[local]  # For local models via llama-cpp

# All LLM providers
pip install medium-converter[all-llm]
```

## Basic Usage

### Command Line

```bash
# Enable enhancement with default provider (OpenAI if API key is set)
medium convert https://medium.com/example-article --enhance

# Specify a provider
medium convert https://medium.com/example-article --enhance --llm-provider anthropic
```

### Python API

```python
from medium_converter import convert_article

# Enable enhancement with default provider
await convert_article(
    url="https://medium.com/example-article",
    output_format="markdown",
    output_path="article.md",
    enhance=True
)

# Specify a provider using LLMConfig
from medium_converter.llm.config import LLMConfig, LLMProvider

llm_config = LLMConfig(
    provider=LLMProvider.ANTHROPIC,
    model="claude-3-sonnet-20240229",
    temperature=0.7
)

await convert_article(
    url="https://medium.com/example-article",
    output_format="markdown",
    output_path="article.md",
    enhance=True,
    llm_config=llm_config
)
```

## Configuration

You can configure LLM enhancement using environment variables:

```bash
# Provider selection
export MEDIUM_LLM_PROVIDER=openai  # or anthropic, google, mistral, local

# API keys
export OPENAI_API_KEY=your_api_key
export ANTHROPIC_API_KEY=your_api_key
export GOOGLE_API_KEY=your_api_key
export MISTRAL_API_KEY=your_api_key

# Model selection
export OPENAI_MODEL=gpt-4
export ANTHROPIC_MODEL=claude-3-opus-20240229
export GOOGLE_MODEL=gemini-pro
export MISTRAL_MODEL=mistral-large-latest

# Parameters
export MEDIUM_LLM_TEMPERATURE=0.5
export MEDIUM_LLM_MAX_TOKENS=4000
```

## How It Works

LLM enhancement processes each content block in the article:

1. Extracts the text content from the article
2. Prepares prompts for the LLM with appropriate context
3. Calls the LLM API with the prompt
4. Replaces the original text with the enhanced version
5. Preserves all formatting, images, and structure

For example, this prompt template is used:

```
You are a world-class editor and writer. Your task is to enhance the following text 
from an article titled "{article_title}" while preserving its meaning and intent.

THE TEXT TO ENHANCE:
{text}

Please improve this text by:
1. Fixing any grammar or spelling errors
2. Improving clarity and flow
3. Making the language more engaging and precise
4. Ensuring technical accuracy
5. Keeping a consistent style and tone

YOUR ENHANCED VERSION (respond with only the enhanced text, nothing else):
```

## Privacy and Data Usage

When using LLM enhancement:

- Article content is sent to the LLM provider's API
- Your API key is used for authentication and billing
- Data handling is subject to the provider's privacy policy
- No article content is stored by Medium Converter
- For enhanced privacy, consider using local models

## Limitations

LLM enhancement has some limitations:

- May occasionally alter meaning despite safeguards
- Quality depends on the LLM provider and model
- Can increase processing time significantly
- Requires API keys and may incur costs
- May have token limits for very long articles

## Next Steps

- [Learn about supported LLM providers](providers.md)
- [Set up self-hosted LLMs](self-hosted.md)
- [Read the API reference for LLM enhancement](../../api-reference/llm.md)