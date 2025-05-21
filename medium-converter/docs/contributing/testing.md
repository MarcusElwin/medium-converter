# Testing Guide

This document outlines how to test Medium Converter effectively.

## Setting Up the Test Environment

### Prerequisites

- Python 3.11 or newer
- Poetry installed
- Git

### Installation

```bash
# Clone the repository if you haven't already
git clone https://github.com/MarcusElwin/medium-converter.git
cd medium-converter

# Install dependencies with development extras
poetry install --with dev

# Activate the virtual environment
poetry shell
```

## Running Tests

### Running All Tests

```bash
# Run all tests
pytest

# Run with increased verbosity
pytest -v

# Run with coverage report
pytest --cov=medium_converter

# Generate HTML coverage report
pytest --cov=medium_converter --cov-report=html
```

### Running Specific Tests

```bash
# Run tests in a specific file
pytest tests/unit/test_models.py

# Run a specific test class
pytest tests/unit/test_models.py::TestArticle

# Run a specific test function
pytest tests/unit/test_models.py::TestArticle::test_article_creation

# Run tests matching a pattern
pytest -k "models or parser"
```

## Test Structure

The test suite is organized as follows:

```
tests/
├── conftest.py         # Shared fixtures
├── unit/               # Unit tests
│   ├── test_models.py  # Tests for data models
│   ├── test_parser.py  # Tests for HTML parsing
│   └── ...
└── integration/        # Integration tests
    ├── test_fetcher.py # Tests for article fetching
    ├── test_exports.py # Tests for export formats
    └── ...
```

### Test Types

#### Unit Tests

Unit tests focus on testing individual components in isolation. These tests are fast and should not make external network calls or depend on external services.

```python
# Example unit test
def test_markdown_exporter_formatting(sample_article):
    exporter = MarkdownExporter()
    result = exporter.export(sample_article)
    
    assert sample_article.title in result
    assert sample_article.author in result
    assert "##" in result  # Should contain headings
```

#### Integration Tests

Integration tests verify that different components work together correctly. These tests may involve file system operations or mocked external services.

```python
# Example integration test with mocked response
def test_article_fetch_and_parse(mock_httpx_client):
    # Setup mock response
    mock_html = "<html><body><article>...</article></body></html>"
    mock_httpx_client.get.return_value.text = mock_html
    
    # Run the test
    article = fetch_and_parse("https://example.com/article")
    
    # Verify results
    assert article.title is not None
    assert len(article.content) > 0
```

#### End-to-End Tests

End-to-end tests verify the whole system works together. These are marked with `pytest.mark.e2e` and are skipped by default unless explicitly enabled.

```python
@pytest.mark.e2e
def test_full_conversion_process():
    # This test actually downloads a public Medium article
    result = convert_article_sync(
        url="https://medium.com/official-public-test-article",
        output_format="markdown",
        output_path=None  # Return as string
    )
    
    assert result is not None
    assert len(result) > 100
```

## Test Fixtures

Common test fixtures are defined in `conftest.py`:

```python
@pytest.fixture
def sample_article():
    """Create a sample article for testing."""
    return Article(
        title="Sample Article",
        author="Test Author",
        date="2023-01-01",
        content=[...],
        # ...
    )

@pytest.fixture
def mock_httpx_client(monkeypatch):
    """Mock the HTTPX client for testing."""
    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_client.return_value.__aenter__.return_value = mock_client
    mock_client.get.return_value = mock_response
    
    monkeypatch.setattr("httpx.AsyncClient", mock_client)
    return mock_client
```

## Mocking External Services

### Mocking HTTP Requests

For tests that would normally make HTTP requests, use the `responses` package to mock responses:

```python
import responses

@responses.activate
def test_fetch_article():
    # Mock the HTTP response
    responses.add(
        responses.GET,
        "https://medium.com/test-article",
        body="<html><body><article>Test content</article></body></html>",
        status=200,
    )
    
    # Test the function
    html = fetch_article_sync("https://medium.com/test-article")
    
    assert "Test content" in html
```

### Mocking LLM Providers

For testing LLM enhancement without making actual API calls:

```python
@pytest.fixture
def mock_llm_client(monkeypatch):
    """Mock LLM client for testing."""
    mock_client = MagicMock()
    mock_client.generate.return_value = "Enhanced test content"
    
    monkeypatch.setattr(
        "medium_converter.llm.providers.get_llm_client",
        lambda config: mock_client
    )
    
    return mock_client

# Then in your test
def test_enhance_article(sample_article, mock_llm_client):
    enhanced = enhance_article_sync(sample_article)
    
    assert "Enhanced test content" in str(enhanced.content)
    assert mock_llm_client.generate.called
```

## Test Data

Sample test data is stored in the `tests/data` directory:

```
tests/data/
├── html/               # Sample HTML files
│   ├── article1.html   # Complete article
│   └── paywall.html    # Article with paywall
├── responses/          # Sample API responses
└── expected/           # Expected output files
    ├── markdown/       # Expected Markdown output
    └── pdf/            # Expected PDF output
```

Load test data in tests like this:

```python
import os

def test_parse_article_with_real_html():
    # Load test HTML file
    html_path = os.path.join(os.path.dirname(__file__), "../data/html/article1.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Test parsing
    article = parse_article(html)
    assert article.title == "Expected Title"
```

## Writing New Tests

### Test-Driven Development

For new features, consider following test-driven development (TDD):

1. Write a failing test that describes the expected behavior
2. Implement the minimum code to make the test pass
3. Refactor the code while ensuring tests continue to pass

### Test Naming Convention

Tests should follow this naming convention:

- `test_[function_name]_[scenario]_[expected_result]`

Examples:
- `test_parse_article_with_paywall_returns_partial_content`
- `test_markdown_exporter_with_images_includes_image_links`

### Testing Complex Async Code

Use `pytest-asyncio` for testing asynchronous code:

```python
import pytest

@pytest.mark.asyncio
async def test_async_function():
    result = await async_function()
    assert result == expected_value
```

## Test Coverage

Aim for high test coverage, particularly for critical code paths:

```bash
# Generate coverage report
pytest --cov=medium_converter --cov-report=term-missing

# Generate HTML report
pytest --cov=medium_converter --cov-report=html
```

The HTML report will be available in the `htmlcov` directory.

## Continuous Integration

Tests are automatically run on GitHub Actions for:
- Each pull request
- Commits to the main branch

The CI pipeline runs:
1. Linting with ruff and black
2. Type checking with mypy
3. Unit tests
4. Integration tests
5. Coverage reporting

## Test Best Practices

1. **Keep tests fast**: Slow tests discourage frequent testing
2. **One assertion per test**: Tests should verify one specific behavior
3. **Use descriptive test names**: Names should explain the test's purpose
4. **Don't test implementation details**: Test behavior, not how it's implemented
5. **Don't skip tests without a good reason**: Skipped tests often indicate problems
6. **Run tests often**: Catch issues early
7. **Avoid test interdependency**: Tests should be able to run in any order

## Troubleshooting Tests

### Common Issues

1. **Flaky tests**: If tests sometimes fail, they may have timing issues or external dependencies
2. **Slow tests**: Look for unnecessary I/O or processing in tests
3. **Failing tests**: Use `pytest -v --tb=native` for better error information

### Debug Options

```bash
# Show local variables in tracebacks
pytest --showlocals

# Drop into PDB on test failures
pytest --pdb

# Increase verbosity
pytest -vv

# Show slowest tests
pytest --durations=10
```