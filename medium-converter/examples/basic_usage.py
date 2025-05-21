#!/usr/bin/env python3
"""Basic usage example for Medium Converter."""

import asyncio
import sys
import os

# Add the package to path for local testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from medium_converter.core.models import Article, ContentBlock, ContentType
from medium_converter.exporters.markdown import MarkdownExporter


async def main():
    """Run a basic example of Medium Converter."""
    # Create a sample article
    article = Article(
        title="Sample Medium Article",
        author="John Doe",
        date="2023-05-21",
        content=[
            ContentBlock(
                type=ContentType.TEXT,
                content="This is a sample article created with Medium Converter."
            ),
            ContentBlock(
                type=ContentType.HEADING,
                content="Introduction",
                metadata={"level": 2}
            ),
            ContentBlock(
                type=ContentType.TEXT,
                content="Medium Converter allows you to convert Medium articles to various formats."
            ),
            ContentBlock(
                type=ContentType.CODE,
                content="import medium_converter\nprint('Hello, world!')",
                metadata={"language": "python"}
            )
        ],
        estimated_reading_time=2,
        url="https://medium.com/sample-article",
        tags=["python", "converter", "medium"]
    )
    
    # Export to Markdown
    exporter = MarkdownExporter()
    md_content = exporter.export(article)
    
    print("=== Exported Markdown ===")
    print(md_content)
    
    # Save to file
    output_path = os.path.join(os.path.dirname(__file__), "sample_article.md")
    with open(output_path, "w") as f:
        f.write(md_content)
    
    print(f"\nSaved to: {output_path}")


if __name__ == "__main__":
    asyncio.run(main())