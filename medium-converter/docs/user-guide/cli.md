# Command Line Interface

Medium Converter provides a simple but powerful command-line interface (CLI).

## Basic Commands

### Convert Command

The main functionality is provided by the `convert` command:

```bash
medium convert <url> [options]
```

#### Options

| Option | Description |
| ------ | ----------- |
| `--format`, `-f` | Output format (markdown, pdf, html, latex, epub, docx) |
| `--output`, `-o` | Output file path |
| `--output-dir`, `-d` | Output directory (auto-generates filename) |
| `--enhance` | Use LLM to enhance article content |
| `--no-enhance` | Disable LLM enhancement (default) |
| `--use-cookies` | Use browser cookies for authentication |
| `--no-cookies` | Disable browser cookie fetching |
| `--llm-provider` | LLM provider to use (openai, anthropic, google, mistral, local) |

#### Examples

```bash
# Basic conversion to Markdown
medium convert https://medium.com/example-article

# Convert to PDF
medium convert https://medium.com/example-article -f pdf -o article.pdf

# Convert with LLM enhancement using OpenAI
medium convert https://medium.com/example-article --enhance --llm-provider openai

# Convert with browser cookies for paywall access
medium convert https://medium.com/example-article --use-cookies
```

### Batch Command

For converting multiple articles at once:

```bash
medium batch <file> [options]
```

The `file` should contain a list of Medium URLs, one per line.

#### Options

| Option | Description |
| ------ | ----------- |
| `--format`, `-f` | Output format (markdown, pdf, html, latex, epub, docx) |
| `--output-dir`, `-d` | Output directory (required) |
| `--enhance` | Use LLM to enhance article content |
| `--no-enhance` | Disable LLM enhancement (default) |
| `--concurrent`, `-c` | Maximum number of concurrent downloads (default: 3) |
| `--use-cookies` | Use browser cookies for authentication |
| `--no-cookies` | Disable browser cookie fetching |
| `--llm-provider` | LLM provider to use (openai, anthropic, google, mistral, local) |

#### Examples

```bash
# Convert multiple articles
medium batch articles.txt -f pdf -d ./articles

# Convert with enhancement and higher concurrency
medium batch articles.txt -f markdown -d ./articles --enhance -c 5
```

### Config Command

Manage persistent configuration:

```bash
medium config <action> [key] [value]
```

#### Actions

| Action | Description |
| ------ | ----------- |
| `show` | Display current configuration |
| `set` | Set a configuration value |
| `get` | Get a configuration value |
| `reset` | Reset configuration to defaults |

#### Examples

```bash
# Show current configuration
medium config show

# Set default format
medium config set default_format pdf

# Set LLM provider
medium config set llm.provider anthropic

# Reset configuration
medium config reset
```

## Global Options

These options work with all commands:

| Option | Description |
| ------ | ----------- |
| `--verbose`, `-v` | Enable verbose output |
| `--debug` | Enable debug logging |
| `--quiet`, `-q` | Suppress all output except errors |
| `--help`, `-h` | Show help message |
| `--version` | Show version information |

## Environment Variables

The CLI respects the environment variables documented in the [Configuration](../getting-started/configuration.md) section.