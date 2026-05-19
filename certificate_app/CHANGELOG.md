# Changelog

All notable changes to the Certificate Sender Application will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial production structure setup

### Changed
- Reorganized codebase for production deployment

### Fixed
- Database model relationships

### Deprecated
- Legacy configuration system

### Removed
- Old app.py structure

### Security
- Implemented environment-based configuration
- Added secret key validation for production

## [1.0.0] - 2024-01-XX

### Added
- Initial release
- Dashboard for certificate management
- Participant management system
- Email distribution functionality
- Excel file upload support
- SMTP configuration management
- Email logging and audit trail
- API endpoints for all major features
- Comprehensive test suite
- Docker support
- Deployment guides
- Documentation

### Features
- Multi-environment configuration (dev, staging, production)
- SQLite for development, MySQL for production
- Flask-SQLAlchemy for ORM
- Email sending with attachments
- CORS support
- Comprehensive error handling
- Logging system

---

## Version Format

Versions follow MAJOR.MINOR.PATCH:
- MAJOR: Breaking changes
- MINOR: New features, backward compatible
- PATCH: Bug fixes, backward compatible

## Guidelines for Contributors

When adding to changelog:
1. Add changes under [Unreleased] section
2. Use these categories: Added, Changed, Deprecated, Removed, Fixed, Security
3. Link to GitHub issues/PRs when applicable
4. Keep entries brief and clear

### Example

```
### Added
- New email template variable support (#123)
- API rate limiting

### Fixed
- Email sending timeout issue (#456)
```
