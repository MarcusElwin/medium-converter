"""Tests for helper functions."""

import os
import pytest
from medium_converter.utils.helpers import normalize_medium_url, safe_filename, get_default_output_path


def test_normalize_medium_url():
    """Test normalizing Medium URLs."""
    # Test medium.com URL
    url = "https://medium.com/towards-data-science/article-123?source=email-digest&foo=bar"
    normalized = normalize_medium_url(url)
    assert normalized == "https://medium.com/towards-data-science/article-123"
    
    # Test publication URL
    url = "https://towardsdatascience.com/article-123?source=email-digest&foo=bar"
    normalized = normalize_medium_url(url)
    assert normalized == "https://towardsdatascience.com/article-123"
    
    # Test non-Medium URL
    url = "https://example.com/article"
    normalized = normalize_medium_url(url)
    assert normalized == url


def test_safe_filename():
    """Test creating safe filenames."""
    # Test spaces
    assert safe_filename("Hello World") == "Hello_World"
    
    # Test special characters
    assert safe_filename("Hello, World!") == "Hello_World"
    
    # Test long filename
    long_name = "a" * 200
    assert len(safe_filename(long_name)) == 100


def test_get_default_output_path(monkeypatch):
    """Test generating default output paths."""
    # Mock getcwd to return a predictable path
    monkeypatch.setattr(os, "getcwd", lambda: "/test/dir")
    
    url = "https://medium.com/towards-data-science/article-123"
    title = "Test Article"
    format = "md"
    
    path = get_default_output_path(url, title, format)
    assert path == "/test/dir/Test_Article_medium.com.md"