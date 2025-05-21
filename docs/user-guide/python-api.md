# Python API

Medium Converter provides both synchronous and asynchronous Python APIs for integration into your projects.

## High-Level Functions

### Asynchronous API

The main asynchronous function for converting a single article:

```python
import asyncio
from medium_converter import convert_article

async def main():
    await convert_article(
        url="https://medium.com/example-article",
        output_format="markdown",
        output_path="article.md",
        enhance=False,
        use_cookies=True,
        llm_config=None,
        export_options=None
    )

if __name__ == "__main__":
    asyncio.run(main())
```

For batch conversion of multiple articles:

```python
import asyncio
from medium_converter import batch_convert

async def main():
    urls = [
        "https://medium.com/article1",
        "https://medium.com/article2",
        "https://medium.com/article3",
    ]
    
    await batch_convert(
        urls=urls,
        output_format="markdown",
        output_dir="./articles",
        enhance=True,
        use_cookies=True,
        max_concurrent=3,
        llm_config=None,
        export_options=None
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### Synchronous API

For simpler use cases, synchronous versions are available:

```python
from medium_converter import convert_article_sync

# Convert a single article
convert_article_sync(
    url="https://medium.com/example-article",
    output_format="markdown",
    output_path="article.md",
    enhance=False
)
```

And for batch conversion:

```python
from medium_converter import batch_convert_sync

urls = [
    "https://medium.com/article1",
    "https://medium.com/article2",
]

batch_convert_sync(
    urls=urls,
    output_format="pdf",
    output_dir="./articles",
    enhance=True
)
```

## Function Parameters

### `convert_article` / `convert_article_sync`

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `url` | `str` | URL of the Medium article | (Required) |
| `output_format` | `str` | Export format (markdown, pdf, html, etc.) | `"markdown"` |
| `output_path` | `str` | Path to save the converted article | `None` (auto-generated) |
| `enhance` | `bool` | Use LLM to enhance content | `False` |
| `use_cookies` | `bool` | Use browser cookies for authentication | `True` |
| `llm_config` | `LLMConfig` | Configuration for LLM enhancement | `None` |
| `export_options` | `dict` | Format-specific export options | `None` |

### `batch_convert` / `batch_convert_sync`

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `urls` | `List[str]` | List of Medium article URLs | (Required) |
| `output_format` | `str` | Export format (markdown, pdf, html, etc.) | `"markdown"` |
| `output_dir` | `str` | Directory to save the converted articles | (Required) |
| `enhance` | `bool` | Use LLM to enhance content | `False` |
| `use_cookies` | `bool` | Use browser cookies for authentication | `True` |
| `max_concurrent` | `int` | Maximum number of concurrent downloads | `3` |
| `llm_config` | `LLMConfig` | Configuration for LLM enhancement | `None` |
| `export_options` | `dict` | Format-specific export options | `None` |

## Advanced Usage

### Custom Pipeline

For more control, you can use the individual components:

```python
import asyncio
from medium_converter.core.fetcher import fetch_article
from medium_converter.core.parser import parse_article
from medium_converter.core.auth import get_medium_cookies
from medium_converter.llm.enhancer import enhance_article
from medium_converter.llm.config import LLMConfig, LLMProvider
from medium_converter.exporters.markdown import MarkdownExporter

async def main():
    # Get authentication cookies
    cookies = get_medium_cookies()
    
    # Fetch article HTML
    html = await fetch_article(
        url="https://medium.com/example-article",
        cookies=cookies
    )
    
    # Parse article
    article = parse_article(html)
    
    # Set up LLM configuration
    llm_config = LLMConfig(
        provider=LLMProvider.OPENAI,
        model="gpt-3.5-turbo",
        temperature=0.7
    )
    
    # Enhance article content
    enhanced_article = await enhance_article(article, llm_config)
    
    # Export to Markdown
    exporter = MarkdownExporter()
    md_content = exporter.export(enhanced_article, "article.md")
    
    print(f"Article exported to article.md")

if __name__ == "__main__":
    asyncio.run(main())
```

### Error Handling

```python
import asyncio
from medium_converter import convert_article

async def main():
    try:
        await convert_article(
            url="https://medium.com/example-article",
            output_format="pdf",
            output_path="article.pdf"
        )
        print("Conversion successful")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except IOError as e:
        print(f"I/O error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```