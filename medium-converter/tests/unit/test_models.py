"""Tests for the data models."""

import pytest
from medium_converter.core.models import Article, Section, ContentBlock, ContentType


def test_content_block_creation():
    """Test creating a ContentBlock."""
    block = ContentBlock(
        type=ContentType.TEXT,
        content="Sample text"
    )
    
    assert block.type == ContentType.TEXT
    assert block.content == "Sample text"
    assert block.metadata == {}


def test_section_creation():
    """Test creating a Section."""
    block = ContentBlock(
        type=ContentType.TEXT,
        content="Sample text"
    )
    
    section = Section(
        title="Sample Section",
        blocks=[block]
    )
    
    assert section.title == "Sample Section"
    assert len(section.blocks) == 1
    assert section.blocks[0].content == "Sample text"


def test_article_creation(sample_article):
    """Test creating an Article."""
    assert sample_article.title == "Sample Article Title"
    assert sample_article.author == "Sample Author"
    assert sample_article.date == "2023-01-01"
    assert len(sample_article.content) == 3
    assert sample_article.estimated_reading_time == 5
    assert sample_article.url == "https://medium.com/sample-article"
    assert sample_article.tags == ["test", "sample"]