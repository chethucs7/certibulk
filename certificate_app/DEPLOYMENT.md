# Deployment Guide

This guide covers deploying the Certificate Sender Application to various platforms.

## Pre-Deployment Checklist

- [ ] All tests passing
- [ ] Environment variables configured
- [ ] Database backups created
- [ ] Static files collected
- [ ] SSL/TLS certificates ready
- [ ] Secret key set to strong random value
- [ ] Email configuration verified

## Local Production Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
pip install gunicorn
```

### 2. Configure Environment

```bash
export FLASK_ENV=production
export SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')
export DATABASE_URL="mysql+mysqlconnector://user:password@localhost/certificate_sender"
```

### 3. Initialize Database

```bash
python scripts/init_db.py
python scripts/backup_db.py
```

### 4. Run with Gunicorn

```bash
gunicorn -w 4 -b 0.0.0.0:8000 --timeout 120 wsgi:app
```

## Docker Deployment

### 1. Build Image

```bash
docker build -f docker/Dockerfile -t certificate-app:latest .
```

### 2. Run Container

```bash
docker run -d \
  --name certificate-app \
  -p 8000:8000 \
  --env-file .env \
  -v app_logs:/app/logs \
  -v app_uploads:/app/app/static/uploads \
  certificate-app:latest
```

### 3. Docker Compose

```bash
docker-compose -f docker/docker-compose.yml up -d
```

## Nginx Reverse Proxy

### Configuration Example

```nginx
upstream app {
    server 127.0.0.1:8000;
    server 127.0.0.1:8001;
    server 127.0.0.1:8002;
}

server {
    listen 80;
    server_name example.com;
    
    # Redirect to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name example.com;
    
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    
    # Security headers
    add_header Strict-Transport-Security "max-age=31536000" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "DENY" always;
    
    client_max_body_size 50M;
    
    location / {
        proxy_pass http://app;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
    }
    
    location /static/ {
        alias /app/app/static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
```

## Systemd Service

### Create Service File

```bash
sudo nano /etc/systemd/system/certificate-app.service
```

```ini
[Unit]
Description=Certificate Sender Application
After=network.target

[Service]
Type=notify
User=appuser
WorkingDirectory=/opt/certificate-app
Environment="FLASK_ENV=production"
EnvironmentFile=/opt/certificate-app/.env
ExecStart=/opt/certificate-app/venv/bin/gunicorn \
    -w 4 \
    -b 0.0.0.0:8000 \
    --timeout 120 \
    wsgi:app
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### Enable and Start Service

```bash
sudo systemctl daemon-reload
sudo systemctl enable certificate-app
sudo systemctl start certificate-app
sudo systemctl status certificate-app
```

## Cloud Platform Deployment

### Azure App Service

```bash
# Install Azure CLI
az login

# Create resource group
az group create --name cert-app-rg --location eastus

# Create app service plan
az appservice plan create \
  --name cert-app-plan \
  --resource-group cert-app-rg \
  --sku B1 \
  --is-linux

# Create app
az webapp create \
  --resource-group cert-app-rg \
  --plan cert-app-plan \
  --name certificate-app \
  --runtime "PYTHON:3.11"

# Configure
az webapp config appsettings set \
  --resource-group cert-app-rg \
  --name certificate-app \
  --settings FLASK_ENV=production

# Deploy
az webapp deployment source config-zip \
  --resource-group cert-app-rg \
  --name certificate-app \
  --src deployment.zip
```

### AWS Elastic Beanstalk

```bash
# Install EB CLI
pip install awsebcli

# Initialize
eb init -p python-3.11 certificate-app --region us-east-1

# Create environment
eb create production-env

# Deploy
eb deploy
```

## Monitoring & Logging

### Log Rotation

```bash
# logrotate configuration
sudo nano /etc/logrotate.d/certificate-app
```

```
/opt/certificate-app/logs/*.log {
    daily
    missingok
    rotate 14
    compress
    delaycompress
    notifempty
    create 0640 appuser appuser
    sharedscripts
}
```

### Health Checks

```bash
# Test endpoint
curl -f https://example.com/health || exit 1
```

## Backup Strategy

### Automated Backup

```bash
#!/bin/bash
# backup.sh
BACKUP_DIR="/backups"
DB_USER="root"
DB_PASS="password"

mysqldump -u $DB_USER -p$DB_PASS certificate_sender | \
  gzip > "$BACKUP_DIR/backup_$(date +%Y%m%d_%H%M%S).sql.gz"

# Keep only 7 days of backups
find $BACKUP_DIR -name "backup_*.sql.gz" -mtime +7 -delete
```

Schedule with crontab:
```bash
0 2 * * * /opt/certificate-app/backup.sh
```

## Security Hardening

1. **Firewall**: Restrict ports
```bash
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

2. **SSL/TLS**: Use Let's Encrypt
```bash
sudo certbot certonly --standalone -d example.com
```

3. **Database**: Use strong passwords
```sql
CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'strong_password';
GRANT ALL ON certificate_sender.* TO 'appuser'@'localhost';
```

## Troubleshooting

### High Memory Usage

```bash
# Check gunicorn processes
ps aux | grep gunicorn

# Reduce workers if needed
gunicorn -w 2 wsgi:app  # Default is 4
```

### Database Locks

```sql
-- MySQL
SHOW PROCESSLIST;
KILL <process_id>;
```

### 502 Bad Gateway

- Check if app is running: `systemctl status certificate-app`
- Check logs: `tail -f /opt/certificate-app/logs/app.log`
- Check nginx: `sudo nginx -t`

## Performance Tuning

### Database
- Add indexes on frequently queried columns
- Use connection pooling
- Archive old logs

### Application
- Enable caching headers
- Use CDN for static files
- Implement async email sending

### Server
- Use SSD storage
- Increase file descriptors
- Tune TCP settings

---

For platform-specific issues, see platform documentation or contact support.
