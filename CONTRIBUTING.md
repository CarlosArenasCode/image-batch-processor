# Contributing to Image Batch Processor

Thank you for your interest in contributing to Image Batch Processor! This document provides guidelines and instructions for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Reporting Issues](#reporting-issues)

## Code of Conduct

By participating in this project, you agree to abide by our code of conduct:
- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Git
- A GitHub account

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/image-batch-processor.git
   cd image-batch-processor
   ```

## Development Setup

### 1. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
# Install production dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt

# Install package in development mode
pip install -e .
```

### 3. Set Up Pre-commit Hooks

```bash
# Install pre-commit hooks
pre-commit install

# Run hooks on all files (optional)
pre-commit run --all-files
```

## Development Workflow

### 1. Create a Branch

```bash
# Create and switch to a new branch
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

### 2. Make Changes

- Write your code
- Add or update tests
- Update documentation if needed

### 3. Run Tests and Checks

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=image_batch_processor

# Run linting
flake8 .

# Check code formatting
black --check .

# Fix code formatting
black .

# Run type checking
mypy image_batch_processor/
```

## Coding Standards

### Code Style

- Follow PEP 8 style guidelines
- Use Black for code formatting (line length: 88 characters)
- Use meaningful variable and function names
- Add type hints where appropriate

### Documentation

- Add docstrings to all public functions and classes
- Use Google-style docstrings
- Update README.md if adding new features

### Example Docstring

```python
def resize_image(image_path: str, width: int, height: int) -> bool:
    """Resize an image to specified dimensions.
    
    Args:
        image_path: Path to the input image file.
        width: Target width in pixels.
        height: Target height in pixels.
        
    Returns:
        True if successful, False otherwise.
        
    Raises:
        FileNotFoundError: If the image file doesn't exist.
        ValueError: If width or height are not positive integers.
    """
```

## Testing

### Writing Tests

- Write tests for all new functionality
- Use pytest for testing
- Place tests in the `tests/` directory
- Test file names should start with `test_`

### Test Structure

```python
import pytest
from image_batch_processor import some_function

def test_some_function():
    """Test description."""
    # Arrange
    input_data = "test_input"
    
    # Act
    result = some_function(input_data)
    
    # Assert
    assert result == expected_output
```

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_specific.py

# Run with coverage report
pytest --cov=image_batch_processor --cov-report=html
```

## Submitting Changes

### 1. Commit Your Changes

Use conventional commit messages:

```bash
# Feature
git commit -m "feat: add image rotation functionality"

# Bug fix
git commit -m "fix: resolve memory leak in batch processing"

# Documentation
git commit -m "docs: update installation instructions"

# Refactor
git commit -m "refactor: improve error handling in CLI"
```

### 2. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 3. Create Pull Request

1. Go to your fork on GitHub
2. Click "New Pull Request"
3. Fill out the PR template
4. Wait for review

### Pull Request Guidelines

- Fill out the PR template completely
- Include screenshots for UI changes
- Reference any related issues
- Ensure all CI checks pass
- Respond to review feedback promptly

## Reporting Issues

### Before Reporting

1. Check existing issues to avoid duplicates
2. Ensure you're using the latest version
3. Test with minimal reproduction case

### Issue Information

Please include:
- Version number
- Operating system
- Python version
- Steps to reproduce
- Expected vs actual behavior
- Error messages or stack traces

## Development Tips

### Useful Commands

```bash
# Install package in development mode
pip install -e .

# Run the CLI tool during development
python -m image_batch_processor --help

# Build documentation locally
mkdocs serve

# Run security audit
pip-audit
```

### Project Structure

```
image-batch-processor/
├── image_batch_processor/    # Main package
│   ├── __init__.py
│   ├── cli.py               # Command line interface
│   ├── core.py              # Core processing logic
│   └── utils.py             # Utility functions
├── tests/                   # Test files
├── docs/                    # Documentation
├── .github/                 # GitHub templates and workflows
├── requirements.txt         # Production dependencies
├── requirements-dev.txt     # Development dependencies
├── pyproject.toml          # Modern Python configuration
└── README.md               # Project documentation
```

## Getting Help

- Create an issue for bugs or feature requests
- Check existing documentation and issues first
- Be patient and respectful when asking for help

## Recognition

Contributors will be recognized in the project's README and release notes.

Thank you for contributing to Image Batch Processor! 🎉