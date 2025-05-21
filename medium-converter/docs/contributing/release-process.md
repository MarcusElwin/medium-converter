# Release Process

This document describes the process for releasing new versions of Medium Converter.

## Version Numbering

Medium Converter follows [Semantic Versioning](https://semver.org/) (SemVer):

- **MAJOR** version for incompatible API changes
- **MINOR** version for new functionality in a backward compatible manner
- **PATCH** version for backward compatible bug fixes

Example: `1.2.3` represents major version 1, minor version 2, patch version 3.

## Release Checklist

### 1. Pre-release Checks

- [ ] Ensure all tests pass: `pytest`
- [ ] Run type checking: `mypy medium_converter`
- [ ] Run linting: `ruff medium_converter`
- [ ] Run code formatting: `black medium_converter`
- [ ] Check test coverage: `pytest --cov=medium_converter`
- [ ] Verify documentation is up-to-date: `mkdocs build`
- [ ] Run the package with key features to ensure everything works
- [ ] Prepare changelog entry

### 2. Update Version and Changelog

1. Update version in `pyproject.toml`:

```toml
[tool.poetry]
name = "medium-converter"
version = "x.y.z"  # Update this line
```

2. Create a changelog entry in `CHANGELOG.md`:

```markdown
## [x.y.z] - YYYY-MM-DD

### Added
- New feature 1
- New feature 2

### Changed
- Change 1
- Change 2

### Fixed
- Bug fix 1
- Bug fix 2

### Removed
- Removed feature 1
```

3. Commit the changes:

```bash
git add pyproject.toml CHANGELOG.md
git commit -m "Bump version to x.y.z"
```

### 3. Create Git Tag

Create a Git tag for the release:

```bash
git tag -a vx.y.z -m "Version x.y.z"
git push origin vx.y.z
```

### 4. Build the Package

Build the package using Poetry:

```bash
# Clean any previous builds
rm -rf dist/

# Build the package
poetry build
```

This will create both `.tar.gz` and `.whl` files in the `dist/` directory.

### 5. Test the Built Package

Test the built package in a clean environment:

```bash
# Create a temporary directory
mkdir /tmp/medium-converter-test
cd /tmp/medium-converter-test

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the built package
pip install /path/to/medium-converter/dist/medium-converter-x.y.z.tar.gz

# Test basic functionality
python -c "import medium_converter; print(medium_converter.__version__)"
```

### 6. Upload to PyPI

Upload the package to PyPI:

```bash
# First to test PyPI (recommended)
poetry publish -r testpypi

# Then to real PyPI
poetry publish
```

Or use twine directly:

```bash
# First to test PyPI (recommended)
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Then to real PyPI
twine upload dist/*
```

### 7. Create GitHub Release

1. Go to the [GitHub releases page](https://github.com/MarcusElwin/medium-converter/releases)
2. Click "Draft a new release"
3. Choose the tag you created
4. Fill in the release title (usually "Version x.y.z")
5. Copy the changelog entry into the description
6. Upload the distribution files
7. Publish the release

### 8. Update Documentation

Make sure the documentation is updated on Read the Docs:

1. Log in to [Read the Docs](https://readthedocs.org/)
2. Go to the Medium Converter project
3. Trigger a new build for the latest version
4. Make sure the new version is set as the default version

### 9. Announce the Release

Announce the new release in appropriate channels:

- GitHub Discussions
- Twitter/X
- Reddit (r/Python, etc.)
- Any other relevant community platforms

## Post-Release

After a successful release:

1. Bump the version in `pyproject.toml` to the next development version with `.dev0` suffix:

```toml
[tool.poetry]
name = "medium-converter"
version = "x.y.(z+1).dev0"  # Next version with dev suffix
```

2. Commit this change:

```bash
git add pyproject.toml
git commit -m "Bump to development version x.y.(z+1).dev0"
git push origin main
```

## Hotfix Releases

For critical bugs in a released version:

1. Create a hotfix branch from the release tag:

```bash
git checkout -b hotfix/x.y.(z+1) vx.y.z
```

2. Fix the bug and update version to `x.y.(z+1)`
3. Update the changelog
4. Commit changes and create a pull request
5. After approval, merge the PR
6. Create a new tag and follow the release process above

## Major Releases

For major releases (x.0.0), additional steps are recommended:

1. Create a release candidate first: `x.0.0-rc1`
2. Get feedback from users
3. Fix any issues and create another RC if needed
4. When stable, release the final version

## Versioning in the Code

The version number should be available in code:

```python
# medium_converter/__init__.py
"""Medium Converter - Convert Medium articles to various formats with LLM enhancement."""

import importlib.metadata

try:
    __version__ = importlib.metadata.version("medium-converter")
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.1.0"  # Default during development
```

## Automating the Release Process

A release GitHub Action workflow can automate some of these steps. Here's a basic example:

```yaml
name: Release

on:
  workflow_dispatch:
    inputs:
      version:
        description: 'Version number (e.g., 1.2.3)'
        required: true

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install poetry
      
      - name: Update version
        run: |
          poetry version ${{ github.event.inputs.version }}
      
      - name: Build and publish
        env:
          POETRY_PYPI_TOKEN_PYPI: ${{ secrets.PYPI_TOKEN }}
        run: |
          poetry build
          poetry publish
      
      - name: Create GitHub Release
        uses: softprops/action-gh-release@v1
        with:
          tag_name: v${{ github.event.inputs.version }}
          name: Version ${{ github.event.inputs.version }}
          generate_release_notes: true
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```