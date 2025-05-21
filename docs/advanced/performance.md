# Performance Optimization

This guide provides tips and strategies for optimizing the performance of Medium Converter.

## General Performance Tips

### Hardware Considerations

- **CPU**: Multi-core processors help with parallel processing
- **Memory**: 8GB+ recommended, especially for PDF generation and LLM enhancement
- **Disk**: SSD improves file I/O performance
- **Network**: Stable internet connection required for fetching articles

### Software Considerations

- **Python Version**: Python 3.11+ offers better performance than older versions
- **Dependencies**: Keep dependencies updated for performance improvements
- **Virtual Environment**: Use a dedicated virtual environment for consistent performance

## Optimizing Article Fetching

### HTTP Client Configuration

```python
from medium_converter.core.fetcher import fetch_article

# Configure HTTP client for better performance
await fetch_article(
    url="https://medium.com/example",
    http_options={
        "timeout": 30,  # Increase timeout for slow connections
        "follow_redirects": True,
        "http2": True,  # Enable HTTP/2 for better performance
        "limits": {
            "max_connections": 10,
            "max_keepalive_connections": 5,
            "keepalive_expiry": 60.0  # seconds
        }
    }
)
```

### Caching

Enable caching to avoid refetching the same articles:

```python
from medium_converter import convert_article

# Enable caching
await convert_article(
    url="https://medium.com/example",
    cache_options={
        "enable": True,
        "ttl": 86400,  # Cache for 24 hours
        "cache_dir": "~/.medium-converter/cache"
    }
)
```

## Optimizing Export Process

### Format-Specific Optimizations

#### PDF Optimization

```python
await convert_article(
    url="https://medium.com/example",
    output_format="pdf",
    export_options={
        "compress_images": True,  # Optimize image size
        "defer_images": True,  # Defer image loading for faster initial processing
        "optimize_for": "size"  # Options: "size", "quality", "speed"
    }
)
```

#### Markdown Optimization

```python
await convert_article(
    url="https://medium.com/example",
    output_format="markdown",
    export_options={
        "lazy_image_loading": True,  # Use lazy loading for images
        "minimize_whitespace": True,  # Reduce file size
        "skip_metadata": True  # Skip frontmatter for faster processing
    }
)
```

## LLM Enhancement Optimization

### Model Selection

Different models offer different performance characteristics:

| Model | Processing Speed | Quality | Token Limit |
|-------|-----------------|---------|-------------|
| GPT-3.5-Turbo | Fast | Good | 4K-16K |
| GPT-4 | Slow | Excellent | 8K-32K |
| Claude 3 Haiku | Very Fast | Good | 200K |
| Claude 3 Sonnet | Medium | Very Good | 200K |
| Claude 3 Opus | Slow | Excellent | 200K |
| Mistral Medium | Fast | Good | 32K |
| Local 7B Model | Varies | Good | Varies |

### Chunking and Batching

For large articles, process content in chunks:

```python
from medium_converter.llm.enhancer import enhance_article
from medium_converter.llm.config import LLMConfig

llm_config = LLMConfig(
    # Provider settings
    chunking={
        "enable": True,
        "max_chunk_size": 1000,  # Characters per chunk
        "overlap": 100,  # Overlap between chunks for context
        "batch_size": 5  # Process 5 chunks at once
    }
)

await enhance_article(article, llm_config)
```

### Parallel Processing

For multiple articles, use parallel processing:

```python
from medium_converter import batch_convert

await batch_convert(
    urls=["url1", "url2", "url3"],
    output_format="markdown",
    output_dir="./articles",
    max_concurrent=3,  # Process 3 articles at once
    enhance=True,
    enhancement_options={
        "parallel_blocks": True  # Process multiple content blocks in parallel
    }
)
```

## Memory Management

### Reducing Memory Usage

```python
# Configure for lower memory usage
await convert_article(
    url="https://medium.com/example",
    memory_options={
        "low_memory": True,  # Use more disk, less RAM
        "cleanup_temporary": True,  # Aggressively clean temp files
        "stream_output": True  # Stream output rather than building in memory
    }
)
```

### Handling Large Articles

For very large articles, use streaming mode:

```python
from medium_converter import convert_article_stream

async for chunk in convert_article_stream(
    url="https://medium.com/example-large-article",
    output_format="markdown",
    chunk_size=1000  # Process 1000 lines at a time
):
    # Process each chunk as it becomes available
    with open("large_article.md", "a") as f:
        f.write(chunk)
```

## Profiling and Benchmarking

### Performance Logging

Enable performance logging to identify bottlenecks:

```python
import logging
from medium_converter import convert_article

# Set up logging
logging.basicConfig(level=logging.INFO)
performance_logger = logging.getLogger("medium_converter.performance")
performance_logger.setLevel(logging.DEBUG)

# Add a handler to log to file
fh = logging.FileHandler("performance.log")
fh.setLevel(logging.DEBUG)
performance_logger.addHandler(fh)

# Now perform conversion with performance logging
await convert_article(
    url="https://medium.com/example",
    output_format="markdown",
    debug_options={
        "profile": True,  # Enable profiling
        "measure_time": True,  # Measure execution time of each step
        "log_memory": True,  # Log memory usage
    }
)
```

### Comparing Configurations

```python
import time
import asyncio
from medium_converter import convert_article

async def benchmark():
    url = "https://medium.com/example"
    configs = [
        {"name": "Default", "options": {}},
        {"name": "Optimized I/O", "options": {"http2": True, "cache": True}},
        {"name": "Low Memory", "options": {"low_memory": True}},
        {"name": "High Performance", "options": {
            "http2": True, 
            "cache": True,
            "parallel_blocks": True,
            "optimize_for": "speed"
        }}
    ]
    
    results = []
    for config in configs:
        start_time = time.time()
        
        await convert_article(
            url=url,
            output_format="markdown",
            **config["options"]
        )
        
        end_time = time.time()
        results.append({
            "name": config["name"],
            "time": end_time - start_time
        })
    
    # Print results
    for result in results:
        print(f"{result['name']}: {result['time']:.2f} seconds")

asyncio.run(benchmark())
```

## Advanced Configurations

### Configuration for High-Performance Servers

```python
from medium_converter import convert_article

# Configuration for high-performance servers
await convert_article(
    url="https://medium.com/example",
    server_options={
        "workers": 8,  # Number of worker processes
        "thread_pool_size": 20,  # Size of thread pool
        "use_uvloop": True,  # Use uvloop for better asyncio performance
        "use_process_pool": True  # Use process pool for CPU-bound tasks
    }
)
```

### Distributed Processing

For very large batch operations, you can distribute work:

```python
import asyncio
from medium_converter import batch_convert
from concurrent.futures import ProcessPoolExecutor

async def process_batch(batch_urls):
    return await batch_convert(
        urls=batch_urls,
        output_format="markdown",
        output_dir="./articles"
    )

async def distributed_processing(all_urls, num_processes=4):
    # Split URLs into batches
    batch_size = len(all_urls) // num_processes
    batches = [all_urls[i:i+batch_size] for i in range(0, len(all_urls), batch_size)]
    
    # Process each batch in a separate process
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        loop = asyncio.get_event_loop()
        tasks = [
            loop.run_in_executor(executor, asyncio.run, process_batch(batch))
            for batch in batches
        ]
        
        results = await asyncio.gather(*tasks)
        return [item for sublist in results for item in sublist]  # Flatten results

# Usage
all_urls = [f"https://medium.com/article{i}" for i in range(1, 101)]
asyncio.run(distributed_processing(all_urls, num_processes=4))
```

## Final Performance Checklist

- ✅ Choose the right output format for your needs
- ✅ Configure HTTP client appropriately
- ✅ Enable caching for repeated access
- ✅ Select appropriate LLM model for your quality/speed requirements
- ✅ Use batching and parallel processing when appropriate
- ✅ Monitor memory usage for large articles
- ✅ Keep dependencies updated
- ✅ Use Python 3.11+ for best performance