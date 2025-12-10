# Contributing to Wanzi

Thank you for your interest in contributing to Wanzi! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/wanzi.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Run tests: `python -m unittest test_wanzi -v`
6. Commit your changes: `git commit -m "Add your feature"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Create a Pull Request

## Development Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run tests
python -m unittest test_wanzi -v

# Test the CLI
python wanzi.py --help
```

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small
- Add tests for new features

## Testing

- Write unit tests for new features
- Ensure all tests pass before submitting a PR
- Aim for good test coverage

## Pull Request Guidelines

- Provide a clear description of the changes
- Reference any related issues
- Ensure tests pass
- Update documentation if needed
- Keep PRs focused on a single feature or fix

## Reporting Bugs

When reporting bugs, please include:

- Python version
- Operating system
- Steps to reproduce
- Expected behavior
- Actual behavior
- Error messages or logs

## Feature Requests

Feel free to open an issue to discuss new features before implementing them.

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help maintain a positive community

## Questions?

If you have questions, feel free to open an issue for discussion.

Thank you for contributing to Wanzi! 🎉
