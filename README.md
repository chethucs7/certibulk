# Certificate Sender Application - Production Ready

> **Production-grade Flask application for managing and distributing certificates via email**

A professional, scalable solution for managing participants and distributing certificates via email with full audit trails, multi-environment support, and enterprise-grade security.

## ✨ Key Features

- ✅ **Participant Management** - Excel upload, data validation, duplicate handling
- ✅ **Certificate Distribution** - Automated email sending with attachments
- ✅ **Email Configuration** - SMTP management with secure storage
- ✅ **Audit Logging** - Complete email history and delivery status tracking
- ✅ **Multi-Environment** - Development, staging, and production configurations
- ✅ **RESTful API** - Programmatic access to all features
- ✅ **Docker Support** - Container-ready with docker-compose
- ✅ **Security Hardened** - CORS, CSRF protection, input validation, secure headers
- ✅ **Comprehensive Testing** - Unit tests, integration tests, coverage reporting
- ✅ **Well Documented** - API docs, deployment guides, security policies

## 📦 Tech Stack

- **Backend**: Python 3.8+ with Flask 3.0+
- **Database**: MySQL 5.7+ (SQLite for development)
- **ORM**: SQLAlchemy 2.0+
- **Data Processing**: Pandas, OpenPyXL
- **Email**: Flask-Mail with SMTP
- **Testing**: Pytest with fixtures and coverage
- **Containerization**: Docker & Docker Compose
- **CI/CD**: GitHub Actions workflows
- **Frontend**: HTML/CSS with Bootstrap (Ready for React/Vue)

## 🚀 Quick Start

**Get running in 5 minutes!** See [certificate_app/QUICKSTART.md](certificate_app/QUICKSTART.md)

```bash
cd certificate_app

# Create & activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/macOS

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env

# Initialize database
python scripts/init_db.py

# Run development server
python run.py
```

Visit **http://localhost:5000** ✅

## 📂 Directory Structure

```
certificate_app/              # Main application directory
├── app/                       # Flask application package
│   ├── models/               # Database models
│   ├── routes/               # API routes
│   ├── services/             # Business logic
│   ├── utils/                # Utilities
│   ├── templates/            # HTML templates
│   └── static/               # CSS, JS, uploads
├── config/                    # Environment configuration
├── tests/                     # Test suite
├── scripts/                   # Utility scripts
├── docker/                    # Docker setup
├── README.md                  # Full documentation
├── API.md                     # API reference
├── requirements.txt           # Production dependencies
└── [Configuration files]
```

## 📖 Documentation

All documentation is in `certificate_app/`:

| Document | Purpose |
|----------|---------|
| [QUICKSTART.md](certificate_app/QUICKSTART.md) | **⭐ Start here** - 5-minute setup |
| [README.md](certificate_app/README.md) | Full feature guide |
| [API.md](certificate_app/API.md) | API endpoint documentation |
| [DEPLOYMENT.md](certificate_app/DEPLOYMENT.md) | Production deployment |
| [SECURITY.md](certificate_app/SECURITY.md) | Security best practices |
| [CONTRIBUTING.md](certificate_app/CONTRIBUTING.md) | Developer guidelines |
| [STRUCTURE.md](certificate_app/STRUCTURE.md) | Architecture overview |
| [CHANGELOG.md](certificate_app/CHANGELOG.md) | Version history |

## 🔧 Requirements

- Python 3.8+
- MySQL 5.7+ (or SQLite for development)
- pip / virtualenv

## 🛠️ Development

### Run Tests
```bash
cd certificate_app
pytest tests/ -v
pytest --cov=app tests/        # With coverage
```

### Code Quality
```bash
make lint      # Check code style
make format    # Auto-format code
```

## 🐳 Docker

### Development
```bash
cd certificate_app
docker-compose -f docker/docker-compose.yml up
```

### Production
```bash
docker build -f certificate_app/docker/Dockerfile -t certificate-app:latest .
docker run -p 8000:8000 --env-file certificate_app/.env certificate-app:latest
```

## 🚢 Production Deployment

Complete deployment guides for all platforms in [certificate_app/DEPLOYMENT.md](certificate_app/DEPLOYMENT.md):

- **Local**: Gunicorn + Nginx
- **Azure**: App Service deployment
- **AWS**: Elastic Beanstalk
- **Docker**: Container deployment
- **Heroku**: Platform as a Service

## 🔒 Security

✅ Production security features:
- Environment-based configuration
- Secret key validation
- Input validation & sanitization
- SQLAlchemy ORM (SQL injection prevention)
- CORS protection
- CSRF protection
- Secure session handling
- Comprehensive logging
- Error handling

**Before production deployment**, review [certificate_app/SECURITY.md](certificate_app/SECURITY.md)

## 🤝 Contributing

See [certificate_app/CONTRIBUTING.md](certificate_app/CONTRIBUTING.md) for:
- Code style guidelines
- Testing requirements
- Pull request process
- Development setup

## 📄 License

MIT License - See [certificate_app/LICENSE](certificate_app/LICENSE)

## 📞 Support

- **Documentation**: Check files in `certificate_app/`
- **Issues**: Create GitHub issue with details
- **Security**: Email security@example.com

## ✨ What Makes This Production-Ready

✅ Professional folder structure  
✅ Multi-environment configuration  
✅ Comprehensive testing setup  
✅ Security best practices  
✅ Docker containerization  
✅ CI/CD workflows  
✅ Extensive documentation  
✅ API documentation  
✅ Deployment guides  
✅ Development tools (Makefile, etc.)

---

**Next Steps**: 👉 [certificate_app/QUICKSTART.md](certificate_app/QUICKSTART.md)

**Version**: 1.0.0 | **Status**: Production Ready ✅
