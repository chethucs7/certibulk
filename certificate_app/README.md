# Certificate Sender Application

A production-grade Flask application for managing and sending certificates to participants via email.

## Project Description

**Certibulk** is an enterprise-level certificate distribution and management platform designed to automate the process of creating, managing, and distributing digital certificates to large numbers of participants. Built with Flask and MySQL, the application provides a comprehensive solution for organizations needing to efficiently handle certificate workflows at scale.

The application streamlines the entire certificate lifecycle—from participant data import to automated email delivery with digital attachments. Organizations can upload participant lists via Excel files, generate customized certificates, and automatically distribute them to recipients with personalized emails. The system maintains a complete audit trail of all activities, including delivery status, failed attempts, and communication logs.

**Key Capabilities:**
- **Bulk Processing**: Handle thousands of participants efficiently through Excel-based data import and batch certificate distribution
- **Email Integration**: Seamless SMTP configuration with retry mechanisms, attachment handling, and delivery tracking
- **Multi-Environment Support**: Separate configurations for development, staging, and production environments with environment-specific database and email settings
- **RESTful API**: Complete REST API for programmatic access to certificate operations, participant management, and delivery status
- **Audit & Logging**: Comprehensive logging system tracking all operations, email sends, and failures with detailed timestamps
- **Role-Based Access**: Authentication system for managing user permissions and controlling access to sensitive operations
- **Data Validation**: Built-in validation for participant data, email addresses, and file uploads to prevent data integrity issues
- **Error Handling**: Robust error handling with user-friendly error messages, retry logic, and detailed debugging information

**Technical Stack:** Flask web framework, SQLAlchemy ORM, MySQL database, Jinja2 templating, RESTful API design patterns, Docker containerization support, comprehensive test coverage.

**Use Cases:** Academic institutions distributing course completion certificates, corporate training programs issuing professional credentials, event organizers sending attendance certificates, certification bodies distributing skill-based digital credentials.

## Features

- ✅ Participant management (upload via Excel)
- ✅ Certificate distribution system
- ✅ Email sending with attachments
- ✅ SMTP configuration management
- ✅ Email log and audit trail
- ✅ Multi-environment configuration (development, staging, production)
- ✅ RESTful API endpoints
- ✅ Comprehensive error handling and logging

## Project Structure

```
certificate_app/
├── app/                          # Main application package
│   ├── __init__.py              # Flask app factory
│   ├── models/                  # Database models
│   ├── routes/                  # API routes/blueprints
│   ├── services/                # Business logic services
│   ├── utils/                   # Utility functions
│   ├── templates/               # Jinja2 templates
│   └── static/                  # Static assets (CSS, JS, uploads)
├── config/                       # Configuration management
├── migrations/                   # Database migrations
├── tests/                        # Test suite
├── scripts/                      # Utility scripts
├── logs/                         # Application logs
├── docker/                       # Docker configuration
├── run.py                        # Development server entry
├── wsgi.py                       # Production WSGI entry
├── requirements.txt              # Production dependencies
├── requirements-dev.txt          # Development dependencies
├── .env.example                  # Environment variables template
├── .gitignore                    # Git ignore patterns
└── README.md                     # This file
```

## Prerequisites

- Python 3.8+
- MySQL 5.7+ (or SQLite for development)
- pip/virtualenv

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd certificate_app
```

### 2. Create Virtual Environment

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Production
pip install -r requirements.txt

# Development (includes testing tools)
pip install -r requirements.txt -r requirements-dev.txt
```

### 4. Configure Environment Variables

```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your configuration
# - Set database URL
# - Configure email settings
# - Set secret key
```

### 5. Initialize Database

```bash
# Using Flask CLI
flask db-init

# Or using Python
python -c "from app import create_app; app = create_app(); app.app_context().push(); from app.models import db; db.create_all()"
```

## Running the Application

### Development

```bash
# Using Flask development server
python run.py

# Or using Flask CLI
FLASK_ENV=development FLASK_APP=run.py flask run

# Application will be available at http://localhost:5000
```

### Production

```bash
# Using Gunicorn (install with: pip install gunicorn)
gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app

# Or using any WSGI server (uWSGI, Waitress, etc.)
```

### Docker

```bash
# Build image
docker build -f docker/Dockerfile -t certificate-app:latest .

# Run container
docker run -p 5000:5000 --env-file .env certificate-app:latest
```

## Configuration

### Environment Variables

See `.env.example` for all available configuration options.

Key variables:
- `FLASK_ENV`: development, testing, or production
- `SECRET_KEY`: Secret key for session management (MUST be strong in production)
- `DATABASE_URL`: Database connection string
- `MAIL_SERVER`: SMTP server address
- `MAIL_USERNAME`: SMTP username
- `MAIL_PASSWORD`: SMTP password

### Configuration Files

Configuration is managed through `config/` directory:
- `config/default.py`: Base configuration
- `config/development.py`: Development-specific settings
- `config/production.py`: Production-specific settings
- `config/testing.py`: Testing configuration

## API Endpoints

### Dashboard
- `GET /` - Main dashboard

### Participants
- `GET /api/participants` - List all participants
- `POST /api/participants` - Add participant

### Emails
- `POST /api/send-emails` - Send emails to participants
- `GET /api/logs` - Get email send logs

### Configuration
- `GET /api/smtp-settings` - Get SMTP configuration
- `POST /api/smtp-settings` - Update SMTP configuration

### File Management
- `POST /api/upload` - Upload Excel file with participant data

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_routes.py

# Run tests in verbose mode
pytest -v
```

## Database Migrations

Database migrations are handled automatically on application startup. For production, ensure proper backup procedures are in place.

## Logging

Logs are written to `logs/app.log` (production) and console output (development).

Log level can be configured via `LOG_LEVEL` environment variable:
- DEBUG
- INFO (default)
- WARNING
- ERROR
- CRITICAL

## Security Considerations

1. **Secret Key**: Always set a strong, randomly generated `SECRET_KEY` in production
2. **Environment Variables**: Never commit `.env` file; use `.env.example` as template
3. **Database**: Use strong passwords for database access
4. **HTTPS**: Enable HTTPS in production (use reverse proxy like nginx)
5. **CORS**: Configure `CORS_ORIGINS` appropriately for your domain
6. **Session Security**: Configure session cookies for HTTPS-only in production

## Deployment

### Gunicorn + Nginx

See `docker/` directory for example Docker setup or deployment guides.

### Platform-specific Guides

- Azure App Service: See `deployment/AZURE.md`
- AWS Elastic Beanstalk: See `deployment/AWS.md`
- Heroku: See `deployment/HEROKU.md`

## Troubleshooting

### Database Connection Issues

```bash
# Test MySQL connection
mysql -h localhost -u root -p

# Check DATABASE_URL format:
# SQLite: sqlite:///certificate_sender.db
# MySQL: mysql+mysqlconnector://user:password@host/dbname
```

### Email Sending Issues

```bash
# Verify SMTP settings
# - Check MAIL_SERVER, MAIL_PORT
# - Enable "Less secure apps" for Gmail
# - Use app-specific passwords for Gmail
```

### Port Already in Use

```bash
# Change port in .env
FLASK_PORT=5001

# Or kill process using port
# Linux/macOS: lsof -i :5000 | grep LISTEN | awk '{print $2}' | xargs kill -9
# Windows: netstat -ano | findstr :5000
```

## Contributing

1. Create a feature branch (`git checkout -b feature/amazing-feature`)
2. Commit your changes (`git commit -m 'Add amazing feature'`)
3. Push to the branch (`git push origin feature/amazing-feature`)
4. Open a Pull Request

Please ensure:
- Code follows PEP 8 style guidelines (use `black` and `flake8`)
- Tests are included for new features
- Database migrations are created if needed

## Performance Optimization

For large-scale deployments:

1. **Database**: Use connection pooling, add indexes
2. **Email**: Use task queue (Celery) for async email sending
3. **Caching**: Implement Redis caching for frequent queries
4. **CDN**: Serve static files through CDN
5. **Load Balancing**: Use load balancer with multiple app instances

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues and questions:
1. Check existing issues on GitHub
2. Create a new issue with detailed description
3. Include error logs and environment information

## Changelog

See CHANGELOG.md for version history and updates.

---

**Last Updated**: 2024
**Version**: 1.0.0
