"""Tests for the DOCX exporter."""

import io
from unittest.mock import MagicMock, patch

import pytest

from medium_converter.core.models import Article, ContentBlock, ContentType, Section
from medium_converter.exporters.docx import DocxExporter

# Skip tests if python-docx is not available
docx = pytest.importorskip("docx")


class TestDocxExporter:
    """Tests for the DOCX exporter."""

    def test_init(self):
        """Test exporter initialization."""
        exporter = DocxExporter()
        assert isinstance(exporter, DocxExporter)

    def test_export_simple_article(self):
        """Test exporting a simple article."""
        article = Article(
            title="Test Article",
            author="Test Author",
            date="2023-01-01",
            content=[
                ContentBlock(type=ContentType.TEXT, content="This is a test paragraph.")
            ],
        )

        exporter = DocxExporter()
        result = exporter.export(article)

        # We can't easily check the content of a binary docx file,
        # but we can check that it's bytes and non-empty
        assert isinstance(result, bytes)
        assert len(result) > 0

    def test_export_complex_article(self):
        """Test exporting a more complex article."""
        article = Article(
            title="Complex Test Article",
            author="Test Author",
            date="2023-01-01",
            tags=["test", "docx", "export"],
            estimated_reading_time=5,
            content=[
                Section(
                    title="Introduction",
                    blocks=[
                        ContentBlock(
                            type=ContentType.TEXT, content="This is the introduction."
                        ),
                        ContentBlock(
                            type=ContentType.QUOTE, content="This is a quote."
                        ),
                    ],
                ),
                Section(
                    title="Code Example",
                    blocks=[
                        ContentBlock(
                            type=ContentType.CODE,
                            content="print('Hello, world!')",
                            metadata={"language": "python"},
                        )
                    ],
                ),
                ContentBlock(
                    type=ContentType.HEADING,
                    content="Conclusion",
                    metadata={"level": 2},
                ),
                ContentBlock(type=ContentType.TEXT, content="This is the conclusion."),
                ContentBlock(
                    type=ContentType.LIST,
                    content="Item 1\nItem 2\nItem 3",
                    metadata={"list_type": "unordered"},
                ),
            ],
        )

        exporter = DocxExporter()
        result = exporter.export(article)

        assert isinstance(result, bytes)
        assert len(result) > 0

    def test_export_to_file(self, tmp_path):
        """Test exporting to a file."""
        article = Article(
            title="Test Article",
            author="Test Author",
            date="2023-01-01",
            content=[
                ContentBlock(type=ContentType.TEXT, content="This is a test paragraph.")
            ],
        )

        output_file = tmp_path / "test.docx"
        exporter = DocxExporter()

        with patch("docx.Document") as mock_document:
            # Setup the mock
            mock_doc = MagicMock()
            mock_document.return_value = mock_doc

            exporter.export(article, str(output_file))

            # Check that save was called with the correct path
            mock_doc.save.assert_called_once_with(str(output_file))

    def test_export_to_fileobj(self):
        """Test exporting to a file-like object."""
        article = Article(
            title="Test Article",
            author="Test Author",
            date="2023-01-01",
            content=[
                ContentBlock(type=ContentType.TEXT, content="This is a test paragraph.")
            ],
        )

        output = io.BytesIO()
        exporter = DocxExporter()

        # Replace actual implementation with mock
        with (
            patch.object(DocxExporter, "_format_block"),
            patch("docx.Document") as mock_document,
        ):
            mock_doc = MagicMock()
            mock_document.return_value = mock_doc
            mock_bytes = b"mock docx content"
            mock_bytesio = MagicMock()
            mock_bytesio.read.return_value = mock_bytes
            mock_doc.save.side_effect = lambda obj: None  # Mock the save method

            with patch("io.BytesIO", return_value=mock_bytesio):
                result = exporter.export(article, output)

                # Check that write was called
                assert mock_bytesio.read.called
                # The result should be the mock bytes
                assert result == mock_bytes
