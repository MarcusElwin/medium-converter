# Troubleshooting

This guide helps you diagnose and fix common issues with Medium Converter.

## Common Issues

### Installation Problems

#### Missing Dependencies

**Symptoms:**
- `ImportError` or `ModuleNotFoundError` when running Medium Converter
- Error messages about missing packages

**Solutions:**

```bash
# Reinstall with all dependencies
pip install medium-converter[all]

# Or install specific extras
pip install medium-converter[pdf,llm]

# Check installed dependencies
pip list | grep medium-converter
```

#### Compatibility Issues

**Symptoms:**
- Errors mentioning Python version compatibility
- Package conflicts

**Solutions:**

```bash
# Check your Python version
python --version

# Ensure you're using Python 3.11 or higher
# Create a fresh virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install with isolation to avoid dependency conflicts
pip install --isolated medium-converter
```

### Connection Issues

#### Failed to Fetch Article

**Symptoms:**
- `ConnectionError` or `HTTPError`
- Timeout errors
- "Failed to fetch article" message

**Solutions:**

```python
# Increase timeout and retry attempts
from medium_converter import convert_article

await convert_article(
    url="https://medium.com/example",
    http_options={
        "timeout": 60,  # Seconds
        "retries": 3,
        "backoff_factor": 2  # Exponential backoff
    }
)
```

Also check:
- Your internet connection
- If the Medium article URL is valid
- If Medium's servers are experiencing issues

#### Proxy Configuration

**Symptoms:**
- Connection errors in environments with proxies

**Solutions:**

```python
# Configure proxy settings
from medium_converter import convert_article

await convert_article(
    url="https://medium.com/example",
    http_options={
        "proxies": {
            "http": "http://proxy.example.com:8080",
            "https": "http://proxy.example.com:8080"
        }
    }
)
```

Or set environment variables:

```bash
export HTTP_PROXY="http://proxy.example.com:8080"
export HTTPS_PROXY="http://proxy.example.com:8080"
```

### Paywall Access Issues

#### Cookie Extraction Failures

**Symptoms:**
- "Unable to extract cookies from browser" errors
- Paywall content not accessible despite having a Medium membership

**Solutions:**

1. Manually provide cookies:

```python
from medium_converter import convert_article

await convert_article(
    url="https://medium.com/example",
    cookies={
        "sid": "your_sid_cookie_value",
        "uid": "your_uid_cookie_value"
    }
)
```

2. Check if your browser stores cookies in an accessible location
3. Ensure you're logged into Medium in your browser
4. Try a different supported browser

### Export Format Issues

#### PDF Generation Problems

**Symptoms:**
- `ReportLabError` or other PDF-related errors
- Missing fonts or corrupted PDF output

**Solutions:**

```python
# Configure PDF generation options
from medium_converter import convert_article

await convert_article(
    url="https://medium.com/example",
    output_format="pdf",
    export_options={
        "default_font": "Helvetica",  # Use standard font
        "embed_fonts": True,
        "fallback_fonts": ["Arial", "Times New Roman"],
        "handle_errors": "strict"  # Options: "ignore", "warn", "strict"
    }
)
```

#### Image Processing Issues

**Symptoms:**
- Missing images in output
- Image download errors

**Solutions:**

```python
# Configure image handling
from medium_converter import convert_article

await convert_article(
    url="https://medium.com/example",
    export_options={
        "image_options": {
            "download_timeout": 30,  # Seconds per image
            "max_size": 10 * 1024 * 1024,  # 10MB max size
            "skip_on_error": True,  # Continue if an image fails
            "alternative_cdn": True  # Try alternative CDNs if primary fails
        }
    }
)
```

### LLM Enhancement Issues

#### API Key Problems

**Symptoms:**
- Authentication errors with LLM providers
- "Invalid API key" or similar errors

**Solutions:**

1. Check your API key is valid and has sufficient permissions/credits
2. Ensure environment variables are set correctly:

```bash
# For OpenAI
export OPENAI_API_KEY="your_key_here"

# For Anthropic
export ANTHROPIC_API_KEY="your_key_here"

# For other providers
export GOOGLE_API_KEY="your_key_here"
export MISTRAL_API_KEY="your_key_here"
```

3. Provide the API key directly:

```python
from medium_converter import convert_article
from medium_converter.llm.config import LLMConfig, LLMProvider

llm_config = LLMConfig(
    provider=LLMProvider.OPENAI,
    api_key="your_actual_api_key_here"
)

await convert_article(
    url="https://medium.com/example",
    enhance=True,
    llm_config=llm_config
)
```

#### Token Limit Exceeded

**Symptoms:**
- Context length or token limit errors from LLM providers

**Solutions:**

```python
# Enable chunking to handle large articles
from medium_converter import convert_article
from medium_converter.llm.config import LLMConfig

llm_config = LLMConfig(
    chunking={
        "enable": True,
        "max_chunk_size": 1000,
        "overlap": 50
    }
)

await convert_article(
    url="https://medium.com/example",
    enhance=True,
    llm_config=llm_config
)
```

### Memory and Performance Issues

#### Out of Memory Errors

**Symptoms:**
- `MemoryError` or process killed
- System becomes unresponsive

**Solutions:**

```python
# Configure for low memory usage
from medium_converter import convert_article

await convert_article(
    url="https://medium.com/example",
    memory_options={
        "low_memory": True,
        "max_image_size": 1024 * 1024,  # 1MB max per image
        "stream_processing": True,
        "cleanup_interval": 10  # Seconds between memory cleanup
    }
)
```

#### Slow Processing

**Symptoms:**
- Conversion takes a very long time

**Solutions:**

See the [Performance Optimization](performance.md) guide for detailed strategies.

```python
# Basic performance optimization
from medium_converter import convert_article

await convert_article(
    url="https://medium.com/example",
    performance_options={
        "optimize_for": "speed",  # Options: "quality", "balance", "speed"
        "parallel_processing": True,
        "skip_unnecessary_steps": True
    }
)
```

## Debugging Techniques

### Enabling Debug Logging

```python
import logging
from medium_converter import convert_article

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("medium_converter_debug.log"),
        logging.StreamHandler()
    ]
)

# Specific module logging
logging.getLogger("medium_converter.core.fetcher").setLevel(logging.DEBUG)
logging.getLogger("medium_converter.llm").setLevel(logging.DEBUG)

# Now run your conversion
await convert_article(
    url="https://medium.com/example",
    debug=True  # Enable all debug features
)
```

### Command Line Debugging

```bash
# Enable verbose output
medium convert https://medium.com/example -v

# Maximum verbosity
medium convert https://medium.com/example -vvv

# Debug mode with full stack traces
medium convert https://medium.com/example --debug

# Export debug information to file
medium convert https://medium.com/example --debug --log-file debug.log
```

### Capturing Data for Bug Reports

```python
from medium_converter import convert_article

await convert_article(
    url="https://medium.com/example",
    debug_options={
        "capture_inputs": True,  # Store input data
        "capture_outputs": True,  # Store output data
        "capture_http": True,  # Store HTTP requests/responses
        "debug_dir": "./debug_output"  # Where to store debug information
    }
)
```

## Contacting Support

If you encounter an issue that you can't resolve, please create a GitHub issue with the following information:

1. Medium Converter version: `pip show medium-converter`
2. Python version: `python --version`
3. Operating system and version
4. Full error message and stack trace
5. Steps to reproduce the issue
6. Any debugging logs you've collected

Create issues at: [https://github.com/MarcusElwin/medium-converter/issues](https://github.com/MarcusElwin/medium-converter/issues)

## Common Error Reference

| Error Code | Description | Typical Solution |
|------------|-------------|------------------|
| `MC-E001` | Connection error | Check internet connection, URL validity |
| `MC-E002` | Authentication error | Verify API keys or cookies |
| `MC-E003` | Parser error | Article might have unusual formatting |
| `MC-E004` | Export format error | Install required dependencies |
| `MC-E005` | LLM provider error | Check API key and provider status |
| `MC-E006` | Memory error | Use low memory options |
| `MC-E007` | File system error | Check permissions and disk space |
| `MC-E008` | Configuration error | Verify configuration values |

For a complete error reference, see the [API documentation](../api-reference/core.md).