# Quick Start Guide

Get the Certificate Sender Application running in 5 minutes!

## 🚀 Quick Setup

### 1. Clone & Navigate
```bash
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
pip install -r requirements.txt
```

### 4. Configure Environment
```bash
cp .env.example .env
# Edit .env if needed (defaults work for development)
```

### 5. Initialize Database
```bash
python scripts/init_db.py
```

### 6. Run Development Server
```bash
python run.py
```

Visit **http://localhost:5000** in your browser! 🎉

---

## 📋 Using the Application

### Upload Participants
1. Prepare Excel file with columns: `name`, `email`, `certificate_file`
2. Visit dashboard
3. Click "Upload Participants"
4. Select your Excel file

### Send Certificates
1. Dashboard shows participant list
2. Select participants to email
3. Click "Send Certificates"
4. Check "Email Logs" for status

### Configure Email
1. Go to Settings (if available)
2. Enter SMTP credentials:
   - Email: `your-email@gmail.com`
   - Password: `app-specific-password` (Google)
   - Server: `smtp.gmail.com`
   - Port: `587`

---

## 🛠️ Common Commands

```bash
# Run development server
python run.py

# Run tests
pytest tests/

# Run with coverage
pytest --cov=app tests/

# Format code
make format

# Check code quality
make lint

# Create sample data
python scripts/create_sample_data.py

# Backup database
python scripts/backup_db.py
```

---

## 📁 Important Files

- `.env` - Configuration (create from `.env.example`)
- `app/models/` - Database models
- `app/routes/` - API endpoints
- `templates/` - HTML templates
- `static/` - CSS, JS, uploads
- `tests/` - Test suite

---

## 🆘 Troubleshooting

### Port Already in Use
```bash
# Change port in .env
FLASK_PORT=5001
```

### Database Issues
```bash
# Reinitialize database
rm certificate_sender.db
python scripts/init_db.py
```

### Import Errors
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### Email Not Sending
- Check SMTP credentials in settings
- Verify `.env` has mail configuration
- For Gmail: use app-specific password
- Enable "Less secure apps" if needed

---

## 📚 Next Steps

1. **Read Full Documentation**: See `README.md`
2. **API Reference**: Check `API.md`
3. **Deployment**: Review `DEPLOYMENT.md`
4. **Contributing**: See `CONTRIBUTING.md`

---

## 🔒 Production Checklist

Before deploying to production:
- [ ] Set strong `SECRET_KEY` in `.env`
- [ ] Configure MySQL database
- [ ] Set email credentials
- [ ] Review `.env` settings
- [ ] Run full test suite
- [ ] Review security settings
- [ ] Set `FLASK_ENV=production`
- [ ] Enable HTTPS
- [ ] Set up backups
- [ ] Configure logging

---

## 📞 Support

- Issues: Create GitHub issue with details
- Questions: Check documentation first
- Security: Email security@example.com

---

**Enjoy using Certificate Sender! 🎊**
