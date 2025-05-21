# Batch Processing

Medium Converter provides powerful batch processing capabilities to convert multiple articles at once.

## Command Line Interface

### Basic Batch Processing

Create a text file with Medium URLs, one per line:

```
https://medium.com/article1
https://medium.com/article2
https://medium.com/article3
```

Then run the batch command:

```bash
medium batch articles.txt -f markdown -d ./output-directory
```

### Batch Options

```bash
medium batch articles.txt \
  --format pdf \
  --output-dir ./articles \
  --concurrent 5 \
  --enhance \
  --llm-provider openai
```

| Option | Description | Default |
|--------|-------------|--------|
| `--format`, `-f` | Output format | `markdown` |
| `--output-dir`, `-d` | Output directory | Required |
| `--concurrent`, `-c` | Maximum concurrent downloads | `3` |
| `--enhance` | Use LLM to enhance content | `False` |
| `--no-enhance` | Disable LLM enhancement | Default |
| `--use-cookies` | Use browser cookies for auth | `True` |
| `--no-cookies` | Disable browser cookie fetching | `False` |
| `--llm-provider` | LLM provider to use | Default from config |
| `--verbose`, `-v` | Enable verbose output | `False` |
| `--quiet`, `-q` | Suppress non-error output | `False` |

## Python API

### Async Batch Processing

```python
import asyncio
from medium_converter import batch_convert

async def main():
    urls = [
        "https://medium.com/article1",
        "https://medium.com/article2",
        "https://medium.com/article3",
    ]
    
    results = await batch_convert(
        urls=urls,
        output_format="markdown",
        output_dir="./articles",
        enhance=True,
        max_concurrent=5
    )
    
    # Results contains information about each conversion
    for result in results:
        print(f"Converted: {result['url']} → {result['output_path']}")
        if result['error']:
            print(f"  Error: {result['error']}")

if __name__ == "__main__":
    asyncio.run(main())
```

### Synchronous Batch Processing

```python
from medium_converter import batch_convert_sync

urls = [
    "https://medium.com/article1",
    "https://medium.com/article2",
    "https://medium.com/article3",
]

results = batch_convert_sync(
    urls=urls,
    output_format="pdf",
    output_dir="./articles",
    enhance=False,
    max_concurrent=3
)

for result in results:
    print(f"Converted: {result['url']} → {result['output_path']}")
```

## Working with CSV Files

You can process lists of articles from CSV files:

```python
import csv
import asyncio
from medium_converter import batch_convert

async def process_csv(csv_file):
    # Read URLs from CSV
    urls = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            urls.append(row['url'])
    
    # Process the URLs
    await batch_convert(
        urls=urls,
        output_format="markdown",
        output_dir="./articles"
    )

if __name__ == "__main__":
    asyncio.run(process_csv("articles.csv"))
```

## Error Handling

Batch processing continues even if some articles fail. Errors are captured in the results:

```python
import asyncio
from medium_converter import batch_convert

async def main():
    urls = [
        "https://medium.com/article1",
        "https://invalid-url",  # This will fail
        "https://medium.com/article3",
    ]
    
    results = await batch_convert(
        urls=urls,
        output_format="markdown",
        output_dir="./articles"
    )
    
    # Process results and handle errors
    successful = [r for r in results if not r['error']]
    failed = [r for r in results if r['error']]
    
    print(f"Successfully converted: {len(successful)} articles")
    print(f"Failed to convert: {len(failed)} articles")
    
    for result in failed:
        print(f"Failed to convert {result['url']}: {result['error']}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Performance Optimization

### Concurrency Control

The `max_concurrent` parameter controls how many articles are processed simultaneously. This should be balanced based on your system resources:

- CPU-bound tasks (like LLM enhancement): use fewer concurrent tasks (1-2 per CPU core)
- I/O-bound tasks (like downloading): use more concurrent tasks (10-20 is often reasonable)

```python
# Optimize for CPU-bound tasks (with LLM enhancement)
await batch_convert(
    urls=urls,
    enhance=True,
    max_concurrent=4  # Good for a quad-core system
)

# Optimize for I/O-bound tasks (without LLM enhancement)
await batch_convert(
    urls=urls,
    enhance=False,
    max_concurrent=15  # Higher concurrency for network-bound tasks
)
```

### Progress Tracking

For long-running batch jobs, you can track progress:

```python
import asyncio
from medium_converter import batch_convert
from tqdm import tqdm  # For progress bars

async def main():
    urls = [f"https://medium.com/article{i}" for i in range(1, 101)]  # 100 URLs
    
    # Create a progress callback
    progress_bar = tqdm(total=len(urls))
    
    def progress_callback(url, status):
        progress_bar.update(1)
        progress_bar.set_description(f"Processed: {url}")
    
    results = await batch_convert(
        urls=urls,
        output_format="markdown",
        output_dir="./articles",
        progress_callback=progress_callback
    )
    
    progress_bar.close()

if __name__ == "__main__":
    asyncio.run(main())
```

## Advanced Use Cases

### Custom Naming

You can customize how output files are named:

```python
import os
import asyncio
from medium_converter import batch_convert

def custom_filename_generator(url, article):
    # Use the article date and title for the filename
    date_str = article.date.strftime("%Y-%m-%d") if hasattr(article.date, "strftime") else article.date
    safe_title = article.title.replace(" ", "_").replace("/", "-")[:50]  # First 50 chars
    return f"{date_str}_{safe_title}.md"

async def main():
    urls = [
        "https://medium.com/article1",
        "https://medium.com/article2",
    ]
    
    await batch_convert(
        urls=urls,
        output_format="markdown",
        output_dir="./articles",
        filename_generator=custom_filename_generator
    )

if __name__ == "__main__":
    asyncio.run(main())
```

### Batch Processing with Different Options per URL

For more flexibility, you can use the low-level API to customize options per URL:

```python
import asyncio
from medium_converter import convert_article
from medium_converter.llm.config import LLMConfig, LLMProvider

async def process_url(url, options):
    try:
        await convert_article(
            url=url,
            output_format=options["format"],
            output_path=options["output_path"],
            enhance=options["enhance"],
            llm_config=options.get("llm_config")
        )
        return {"url": url, "success": True, "output_path": options["output_path"]}
    except Exception as e:
        return {"url": url, "success": False, "error": str(e)}

async def main():
    # Different options for each URL
    urls_with_options = [
        {
            "url": "https://medium.com/article1",
            "format": "markdown",
            "output_path": "./articles/article1.md",
            "enhance": False
        },
        {
            "url": "https://medium.com/article2",
            "format": "pdf",
            "output_path": "./articles/article2.pdf",
            "enhance": True,
            "llm_config": LLMConfig(provider=LLMProvider.OPENAI)
        },
    ]
    
    # Process concurrently (up to 3 at a time)
    semaphore = asyncio.Semaphore(3)
    
    async def bounded_process(url_options):
        async with semaphore:
            return await process_url(url_options["url"], url_options)
    
    tasks = [bounded_process(opt) for opt in urls_with_options]
    results = await asyncio.gather(*tasks)
    
    return results

if __name__ == "__main__":
    asyncio.run(main())
```

This approach gives you complete control over how each URL is processed while still benefiting from concurrent execution.