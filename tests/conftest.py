"""Test fixtures for Medium Converter."""

import pytest
from medium_converter.core.models import Article, Section, ContentBlock, ContentType


@pytest.fixture
def sample_article() -> Article:
    """Create a sample article for testing.
    
    Returns:
        A sample Article object
    """
    return Article(
        title="Sample Article Title",
        author="Sample Author",
        date="2023-01-01",
        content=[
            ContentBlock(
                type=ContentType.TEXT, 
                content="This is a sample paragraph of text for testing purposes."
            ),
            Section(
                title="Sample Section",
                blocks=[
                    ContentBlock(
                        type=ContentType.TEXT,
                        content="This is text inside a section."
                    ),
                    ContentBlock(
                        type=ContentType.CODE,
                        content="print('Hello, world!')",
                        metadata={"language": "python"}
                    )
                ]
            ),
            ContentBlock(
                type=ContentType.IMAGE,
                content="https://example.com/image.jpg",
                metadata={"alt": "Sample image"}
            )
        ],
        estimated_reading_time=5,
        url="https://medium.com/sample-article",
        tags=["test", "sample"]
    )