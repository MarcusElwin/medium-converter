"""HTML Parser for Medium articles."""

from typing import Dict, List, Optional
from bs4 import BeautifulSoup
from .models import Article, Section, ContentBlock


def parse_article(html: str) -> Article:
    """Parse a Medium article's HTML content.

    Args:
        html: The HTML content of the Medium article

    Returns:
        Structured Article object
    """
    soup = BeautifulSoup(html, "lxml")
    # Placeholder implementation
    return Article(
        title="Sample Article Title",
        author="Sample Author",
        date="2023-01-01",
        content=[],
        estimated_reading_time=5,
    )
