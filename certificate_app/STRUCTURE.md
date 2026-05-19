# Project Structure Documentation

## Directory Overview

```
certificate_app/
├── app/                          # Main application package
│   ├── __init__.py              # Flask application factory
│   ├── models/                  # Database models (SQLAlchemy ORM)
│   │   └── __init__.py          # Model definitions
│   ├── routes/                  # API routes and blueprints
│   │   ├── __init__.py          # Route blueprint definitions
│   │   └── auth.py              # Authentication routes (future)
│   ├── services/                # Business logic layer
│   │   └── __init__.py          # Email service and utilities
│   ├── utils/                   # Utility functions
│   │   └── __init__.py          # Helper functions
│   ├── templates/               # Jinja2 HTML templates
│   │   └── dashboard.html       # Main dashboard template
│   └── static/                  # Static assets
│       ├── css/                 # Stylesheets
│       │   └── style.css
│       ├── js/                  # JavaScript files
│       └── uploads/             # File upload directories
│           ├── certificates/    # Uploaded certificates
│           └── excel/           # Uploaded Excel files
│
├── config/                       # Configuration management
│   ├── __init__.py              # Config loader
│   ├── default.py               # Base configuration
│   ├── development.py           # Development settings
│   ├── production.py            # Production settings
│   └── testing.py               # Test settings
│
├── migrations/                   # Database migrations
│   └── __init__.py              # Migration module
│
├── tests/                        # Test suite
│   ├── __init__.py              # Test package
│   ├── conftest.py              # Pytest fixtures
│   ├── test_routes.py           # Route tests
│   ├── test_models.py           # Model tests
│   └── test_services.py         # Service tests
│
├── scripts/                      # Utility scripts
│   ├── init_db.py               # Database initialization
│   ├── backup_db.py             # Database backup
│   └── create_sample_data.py    # Sample data creation
│
├── logs/                         # Application logs
│   └── app.log                  # Main application log
│
├── docker/                       # Docker configuration
│   ├── Dockerfile               # Production Dockerfile
│   └── docker-compose.yml       # Docker Compose setup
│
├── .github/                      # GitHub specific
│   └── workflows/               # CI/CD workflows
│       ├── tests.yml            # Test workflow
│       ├── code-quality.yml     # Code quality checks
│       └── security.yml         # Security checks
│
├── .env.example                  # Environment variables template
├── .env                          # Environment variables (DO NOT COMMIT)
├── .gitignore                    # Git ignore patterns
├── .editorconfig                 # Editor configuration
├── requirements.txt              # Production dependencies
├── requirements-dev.txt          # Development dependencies
├── setup.py                      # Package setup configuration
├── pyproject.toml               # Python project configuration
├── run.py                        # Development server entry point
├── wsgi.py                       # Production WSGI entry point
├── Makefile                      # Development commands
│
├── README.md                     # Project overview
├── API.md                        # API documentation
├── DEPLOYMENT.md                 # Deployment guide
├── CONTRIBUTING.md               # Contributing guidelines
├── CHANGELOG.md                  # Version history
├── LICENSE                       # MIT License
└── SECURITY.md                   # Security policy
```

## Key Directories Explained

### `/app`
The main application package containing all Flask-related code.

- **models/**: SQLAlchemy ORM models for database tables
- **routes/**: Flask blueprints organizing API endpoints
- **services/**: Business logic separated from routes
- **utils/**: Helper functions and utilities
- **templates/**: Jinja2 templates for HTML rendering
- **static/**: CSS, JS, images, and upload directories

### `/config`
Environment-specific configuration files.

- **default.py**: Base settings used by all environments
- **development.py**: Development-specific overrides
- **production.py**: Production-specific settings with security checks
- **testing.py**: Test environment configuration
- **__init__.py**: Configuration loader that selects appropriate config

### `/tests`
Test suite organized by component.

- **conftest.py**: Pytest fixtures for test setup
- **test_*.py**: Test files for each component
- Tests follow AAA pattern: Arrange, Act, Assert

### `/scripts`
Standalone utility scripts for maintenance tasks.

- **init_db.py**: Initialize database with schema
- **backup_db.py**: Backup database
- **create_sample_data.py**: Create test data

### `/docker`
Docker-related files for containerization.

- **Dockerfile**: Production-ready image definition
- **docker-compose.yml**: Multi-container orchestration
- Images are optimized for production with minimal size

## File Organization Philosophy

### Separation of Concerns

```
Request → Route Handler → Service → Model → Database
```

1. **Routes** (app/routes/): Handle HTTP requests/responses
2. **Services** (app/services/): Contain business logic
3. **Models** (app/models/): Define data structures
4. **Utils** (app/utils/): Provide helper functions

### Configuration Hierarchy

```
Default Config
    ↓
Environment-specific Config (development/production/testing)
    ↓
Environment Variables (.env)
```

Environment variables override configuration files, allowing per-deployment customization.

### Testing Organization

- **test_routes.py**: Test API endpoints
- **test_models.py**: Test database models
- **test_services.py**: Test business logic

Tests are isolated, use fixtures, and mock external dependencies.

## Important Files

### Configuration
- **.env**: Environment variables (created from .env.example)
- **config/*.py**: Configuration for different environments
- **pyproject.toml**: Project metadata and tool configuration

### Entry Points
- **run.py**: Development server (used with `python run.py`)
- **wsgi.py**: Production WSGI application (used with gunicorn/uwsgi)

### Dependencies
- **requirements.txt**: Production dependencies
- **requirements-dev.txt**: Development-only dependencies
- **setup.py**: Package installation configuration

### Documentation
- **README.md**: Getting started guide
- **API.md**: API endpoint documentation
- **DEPLOYMENT.md**: Deployment instructions
- **CONTRIBUTING.md**: Development guidelines
- **CHANGELOG.md**: Version history
- **SECURITY.md**: Security policies

## Environment-Specific Paths

### Development
- Database: `certificate_sender.db` (SQLite)
- Logs: Console output
- Upload folder: `app/static/uploads/`

### Production
- Database: MySQL connection string from env
- Logs: `logs/app.log` (file-based with rotation)
- Upload folder: Configured path with permissions

## Adding New Features

### Step 1: Create Model
Add to `app/models/__init__.py`:
```python
class MyModel(db.Model):
    __tablename__ = 'my_models'
    id = db.Column(db.Integer, primary_key=True)
    # ... fields
```

### Step 2: Create Service
Add to `app/services/__init__.py`:
```python
def my_business_logic():
    # Implementation
    pass
```

### Step 3: Create Route
Add to `app/routes/__init__.py`:
```python
@main_bp.route('/api/my-endpoint', methods=['GET'])
def my_endpoint():
    # Use service
    return jsonify({'data': my_business_logic()})
```

### Step 4: Add Tests
Add to `tests/test_*.py`:
```python
def test_my_endpoint(client):
    response = client.get('/api/my-endpoint')
    assert response.status_code == 200
```

## Performance Considerations

### Database
- Use indexes on frequently queried columns
- Implement connection pooling for production
- Archive old logs and email records

### Application
- Static files served by CDN/reverse proxy in production
- Implement caching headers
- Use background tasks for email sending

### Deployment
- Use multiple gunicorn workers
- Load balance with nginx
- Monitor resource usage

## Security Considerations

### Sensitive Data
- `.env` file is in .gitignore (never commit secrets)
- Use strong SECRET_KEY in production
- Database passwords encrypted/secured

### Code
- Input validation on all endpoints
- SQL injection prevention (via SQLAlchemy ORM)
- CORS configured for specific origins
- HTTPS enforced in production

### Dependencies
- Regular dependency updates
- Security scanning in CI/CD
- Review third-party packages

## Troubleshooting

### Database Issues
- Check DATABASE_URL in .env
- Ensure MySQL/SQLite is running
- Check file permissions

### Import Errors
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt`
- Check PYTHONPATH

### Port Issues
- Change FLASK_PORT in .env
- Kill existing process on port
- Check firewall rules

## Next Steps

1. Copy `.env.example` to `.env` and configure
2. Run `python scripts/init_db.py` to initialize database
3. Run `python run.py` to start development server
4. Access dashboard at `http://localhost:5000`

---

For detailed information, see individual documentation files (README.md, API.md, DEPLOYMENT.md, etc.).
