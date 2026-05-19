# Contributing to Certificate Sender Application

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Help others succeed

## Getting Started

### 1. Fork the Repository

```bash
git clone https://github.com/your-fork/certificate-app.git
cd certificate-app
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

Use descriptive branch names:
- `feature/add-new-feature` for new features
- `fix/resolve-issue` for bug fixes
- `docs/update-readme` for documentation
- `test/add-tests` for test improvements

### 3. Set Up Development Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
pip install -r requirements-dev.txt

cp .env.example .env
```

### 4. Make Your Changes

Follow these guidelines:

#### Code Style

- Follow PEP 8 style guidelines
- Use 4 spaces for indentation
- Keep lines under 100 characters
- Use descriptive variable names

Format with Black:
```bash
black app/ tests/ scripts/
```

Lint with Flake8:
```bash
flake8 app/ tests/
```

#### Commits

```bash
git add .
git commit -m "Brief description of changes"

# Write meaningful commit messages
# - Use imperative mood ("Add feature" not "Added feature")
# - Limit first line to 50 characters
# - Reference related issues (#123)
```

### 5. Add Tests

Ensure new features have tests:

```bash
# Add tests to tests/ directory
pytest tests/

# Check coverage
pytest --cov=app tests/
```

Test coverage should be >= 80% for new code.

### 6. Update Documentation

Update relevant documentation:
- README.md if adding/changing features
- Comments in code for complex logic
- Docstrings for functions/classes
- .env.example if adding new env vars

### 7. Submit Pull Request

```bash
git push origin feature/your-feature-name
```

Create a Pull Request with:
- Clear title describing the change
- Description of what changed and why
- Link to related issues
- Screenshots if applicable

## Pull Request Checklist

- [ ] Code follows PEP 8 style
- [ ] New tests added for new features
- [ ] All tests pass (`pytest`)
- [ ] Code coverage maintained
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
- [ ] Commits are clean and well-described
- [ ] No secrets or sensitive data committed

## Review Process

1. At least one maintainer review required
2. All CI checks must pass
3. Tests must have high coverage
4. Code quality standards must be met

## Areas for Contribution

### High Priority
- 🐛 Bug fixes
- 📚 Documentation improvements
- ♻️ Code refactoring
- 🧪 Test coverage
- 🔒 Security improvements

### Future Features
- Email scheduling
- Template variable support
- Participant data validation
- Advanced reporting
- API authentication/authorization

## Coding Standards

### Python

```python
# Good
def send_email_to_participant(participant: Participant) -> bool:
    """
    Send email with certificate to participant.
    
    Args:
        participant: Participant object to send email to
    
    Returns:
        bool: True if successful, False otherwise
    """
    pass

# Bad
def send_email(p):
    # Send email
    pass
```

### Naming Conventions

- Classes: `PascalCase` (e.g., `EmailService`)
- Functions/Variables: `snake_case` (e.g., `send_email`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES`)
- Private: prefix with `_` (e.g., `_internal_method`)

### Comments

```python
# Good - explains why
if retry_count > MAX_RETRIES:
    # Give up after max retries to prevent infinite loops
    return False

# Bad - explains what (code already shows this)
if retry_count > MAX_RETRIES:
    # Check if retry count exceeds max
    return False
```

## Testing Standards

```python
# Test file naming: test_*.py or *_test.py
# Test function naming: test_*

import pytest

def test_send_email_success(app):
    """Test successful email sending."""
    participant = Participant(name='Test', email='test@example.com')
    result = send_email(participant)
    assert result is True

def test_send_email_missing_certificate(app):
    """Test email sending fails without certificate."""
    participant = Participant(name='Test', email='test@example.com', 
                            certificate_file=None)
    with pytest.raises(ValueError):
        send_email(participant)
```

## Documentation Standards

- Use clear, concise language
- Include code examples
- Explain the "why", not just the "what"
- Keep README updated
- Add docstrings to all public functions

## Questions?

- Check existing issues/PRs
- Create a GitHub discussion
- Contact maintainers
- Read the documentation

## Thank You!

Your contributions help make this project better! 🙏
