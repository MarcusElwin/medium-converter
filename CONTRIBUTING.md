# Contributing to Medium Converter

First off, thank you for considering contributing to Medium Converter! It's people like you that make this project better.

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct. Please be respectful, inclusive, and considerate when interacting with other contributors.

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report. Following these guidelines helps maintainers understand your report, reproduce the behavior, and find related reports.

**Before Submitting A Bug Report**

* Check the [issues](https://github.com/MarcusElwin/medium-converter/issues) for a list of current known issues.
* Perform a [search](https://github.com/MarcusElwin/medium-converter/issues) to see if the problem has already been reported. If it has and the issue is still open, add a comment to the existing issue instead of opening a new one.

**How Do I Submit A Good Bug Report?**

* Use a clear and descriptive title
* Describe the exact steps which reproduce the problem
* Provide specific examples to demonstrate the steps
* Describe the behavior you observed after following the steps and why this is a problem
* Explain which behavior you expected to see instead and why
* Include screenshots if applicable
* If the problem wasn't triggered by a specific action, describe what you were doing before the problem happened

### Suggesting Enhancements

Enhancement suggestions are tracked as [GitHub issues](https://github.com/MarcusElwin/medium-converter/issues). When creating an enhancement suggestion, please provide the following information:

* Use a clear and descriptive title
* Provide a step-by-step description of the suggested enhancement
* Describe the current behavior and why this enhancement would be useful
* Specify the context in which the enhancement would be most valuable
* Provide examples of how the enhancement would be used

### Pull Requests

Follow these steps to have your contribution considered by the maintainers:

1. Fork the repository
2. Clone your fork
3. Create a new branch: `git checkout -b my-feature-branch`
4. Make your changes
5. Run tests and linting: `poetry run pytest` and `poetry run ruff check medium_converter`
6. Commit your changes with a descriptive commit message
7. Push to your fork and [submit a pull request](https://github.com/MarcusElwin/medium-converter/compare)
8. Wait for your pull request to be reviewed and merged

## Development Environment Setup

### Prerequisites

* Python 3.11+
* [Poetry](https://python-poetry.org/docs/#installation) for dependency management

### Setting Up

1. Clone the repository:
   ```bash
   git clone https://github.com/MarcusElwin/medium-converter.git
   cd medium-converter
   ```

2. Install dependencies:
   ```bash
   poetry install --all-extras
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

### Development Workflow

1. Create a new branch:
   ```bash
   git checkout -b my-feature-branch
   ```

2. Make your changes

3. Run tests:
   ```bash
   pytest
   ```

4. Run linting:
   ```bash
   ruff check medium_converter
   ```

5. Run type checking:
   ```bash
   mypy medium_converter
   ```

6. Make sure the CLI works:
   ```bash
   medium --help
   ```

7. Commit your changes:
   ```bash
   git commit -m "Add my new feature"
   ```

## Style Guidelines

### Python Code

* Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
* Use [Black](https://github.com/psf/black) for code formatting
* Use [Ruff](https://github.com/astral-sh/ruff) for linting
* Use [mypy](https://mypy.readthedocs.io) for type checking
* Add docstrings for all modules, classes, and functions using the Google style

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* Consider starting the commit message with an applicable prefix:
    * `feat:` for new features
    * `fix:` for bug fixes
    * `docs:` for documentation changes
    * `style:` for formatting changes
    * `refactor:` for code refactoring
    * `test:` for adding or fixing tests
    * `perf:` for performance improvements
    * `ci:` for CI/CD changes
    * `chore:` for general maintenance tasks

## Licensing

By contributing, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).

## Thank You!

Thanks for your contributions - they're what make the open-source community great!