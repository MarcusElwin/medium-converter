# Markdown Export

Markdown is the default export format for Medium Converter. This format preserves the content structure while creating a plain text file that's readable and can be further processed with other Markdown tools.

## Basic Usage

### Command Line

```bash
# Default format is Markdown
medium convert https://medium.com/example-article

# Explicitly specify Markdown format
medium convert https://medium.com/example-article -f markdown -o article.md
```

### Python API

```python
from medium_converter import convert_article

# Using default format (markdown)
await convert_article(
    url="https://medium.com/example-article",
    output_path="article.md"
)

# Explicitly specify markdown format
await convert_article(
    url="https://medium.com/example-article",
    output_format="markdown",
    output_path="article.md"
)
```

## Customization Options

You can customize the Markdown export with the following options:

| Option | Description | Default |
|--------|-------------|---------|
| `include_frontmatter` | Add YAML frontmatter with metadata | `True` |
| `syntax_highlighting` | Enable syntax highlighting for code blocks | `True` |
| `include_toc` | Generate table of contents | `False` |
| `heading_style` | Style for headings (atx or setext) | `"atx"` |
| `image_path` | Path for downloaded images | `"images/"` |
| `download_images` | Download and save images locally | `False` |

### Command Line

```bash
medium convert https://medium.com/example-article -f markdown \
  --option include_frontmatter=true \
  --option include_toc=true \
  --option download_images=true
```

### Python API

```python
await convert_article(
    url="https://medium.com/example-article",
    output_format="markdown",
    output_path="article.md",
    export_options={
        "include_frontmatter": True,
        "include_toc": True,
        "download_images": True,
        "image_path": "assets/images/",
    }
)
```

## Output Format

The Markdown output follows these conventions:

1. Article title as main heading (H1)
2. Optional YAML frontmatter with metadata
3. Optional table of contents
4. Article sections with appropriate heading levels
5. Images with alt text when available
6. Code blocks with language specification
7. Tables as GitHub-style Markdown tables
8. Mathematical formulas using KaTeX syntax

### Example Output

```markdown
---
title: "Example Article Title"
author: "Author Name"
date: "2023-05-20"
url: "https://medium.com/example-article"
tags: ["programming", "python", "tutorial"]
reading_time: 5
---

# Example Article Title

By Author Name | May 20, 2023 | 5 min read

## Introduction

This is a paragraph of text from the article. It might contain *emphasized* or **bold** text.

![Image description](images/image1.jpg)

### Code Example

```python
def hello_world():
    print("Hello, world!")
```

## Conclusion

This is the conclusion paragraph.
```

## Using with Other Tools

Markdown output is compatible with:

- Static site generators (Jekyll, Hugo, Gatsby)
- Documentation tools (MkDocs, VuePress, Docusaurus)
- Note-taking applications (Obsidian, Notion)
- Version control systems for easy diffing
- Markdown editors and processors (Pandoc)