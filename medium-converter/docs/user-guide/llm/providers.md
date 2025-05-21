# LLM Providers

Medium Converter supports various LLM providers for content enhancement. This page details each provider's setup and configuration.

## OpenAI

### Installation

```bash
pip install medium-converter[openai]
```

### Configuration

```bash
# Environment variable
export OPENAI_API_KEY=your_api_key
export OPENAI_MODEL=gpt-4  # Optional, defaults to gpt-3.5-turbo
```

In Python:

```python
from medium_converter import convert_article
from medium_converter.llm.config import LLMConfig, LLMProvider

llm_config = LLMConfig(
    provider=LLMProvider.OPENAI,
    model="gpt-4",
    api_key="your_api_key",
    temperature=0.7,
    max_tokens=None  # Use model default
)

await convert_article(
    url="https://medium.com/example-article",
    enhance=True,
    llm_config=llm_config
)
```

### Available Models

- `gpt-3.5-turbo` (default)
- `gpt-3.5-turbo-16k`
- `gpt-4`
- `gpt-4-turbo`
- `gpt-4-32k`

## Anthropic

### Installation

```bash
pip install medium-converter[anthropic]
```

### Configuration

```bash
# Environment variable
export ANTHROPIC_API_KEY=your_api_key
export ANTHROPIC_MODEL=claude-3-sonnet-20240229  # Optional
```

In Python:

```python
from medium_converter import convert_article
from medium_converter.llm.config import LLMConfig, LLMProvider

llm_config = LLMConfig(
    provider=LLMProvider.ANTHROPIC,
    model="claude-3-opus-20240229",
    api_key="your_api_key",
    temperature=0.5
)

await convert_article(
    url="https://medium.com/example-article",
    enhance=True,
    llm_config=llm_config
)
```

### Available Models

- `claude-3-haiku-20240307` (default)
- `claude-3-sonnet-20240229`
- `claude-3-opus-20240229`
- `claude-2.1`
- `claude-2.0`

## Google

### Installation

```bash
pip install medium-converter[google]
```

### Configuration

```bash
# Environment variable
export GOOGLE_API_KEY=your_api_key
export GOOGLE_MODEL=gemini-pro  # Optional, this is the default
```

In Python:

```python
from medium_converter import convert_article
from medium_converter.llm.config import LLMConfig, LLMProvider

llm_config = LLMConfig(
    provider=LLMProvider.GOOGLE,
    model="gemini-pro",
    api_key="your_api_key",
    temperature=0.4
)

await convert_article(
    url="https://medium.com/example-article",
    enhance=True,
    llm_config=llm_config
)
```

### Available Models

- `gemini-pro` (default)
- `gemini-pro-vision`
- `gemini-1.5-pro`
- `gemini-1.5-flash`

## Mistral AI

### Installation

```bash
pip install medium-converter[mistral]
```

### Configuration

```bash
# Environment variable
export MISTRAL_API_KEY=your_api_key
export MISTRAL_MODEL=mistral-medium  # Optional, this is the default
```

In Python:

```python
from medium_converter import convert_article
from medium_converter.llm.config import LLMConfig, LLMProvider

llm_config = LLMConfig(
    provider=LLMProvider.MISTRAL,
    model="mistral-large-latest",
    api_key="your_api_key",
    temperature=0.7
)

await convert_article(
    url="https://medium.com/example-article",
    enhance=True,
    llm_config=llm_config
)
```

### Available Models

- `mistral-medium` (default)
- `mistral-small-latest`
- `mistral-large-latest`
- `open-mixtral-8x7b`
- `open-mistral-7b`

## Using LiteLLM

Medium Converter uses LiteLLM under the hood, which provides a unified interface to multiple LLM providers. This allows you to use any provider supported by LiteLLM by specifying the appropriate model name.

### Installation

```bash
pip install medium-converter[llm]
```

### Configuration

In Python:

```python
from medium_converter import convert_article
from medium_converter.llm.config import LLMConfig

# Custom provider via LiteLLM
llm_config = LLMConfig(
    model="replicate/llama-2-70b-chat:58d078176e02c219e11eb4da5a02a7830a283b14cf8f94537af893ccff5ee781",
    api_key="your_replicate_api_key",
    extra_params={
        "provider": "replicate"
    }
)

await convert_article(
    url="https://medium.com/example-article",
    enhance=True,
    llm_config=llm_config
)
```

## Provider Comparison

| Provider | Strengths | Limitations | Cost |
|----------|-----------|-------------|------|
| OpenAI | High quality, wide adoption | Higher cost, proprietary | $0.50-$30/million tokens |
| Anthropic | Great for long content, accurate | Higher cost, proprietary | $3-$15/million tokens |
| Google | Competitive pricing, reliable | Limited model options | $0.25-$1.50/million tokens |
| Mistral | Open weights options, competitive | Newer, less tested | $1-$8/million tokens |
| Local LLMs | Privacy, no API costs | Requires hardware, lower quality | Free (compute costs) |