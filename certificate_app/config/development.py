"""
Development configuration.
"""
import os
from config.default import Config

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    TESTING = False
    
    # SQLite for development
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'sqlite:///certificate_sender.db'
    )
    SQLALCHEMY_ECHO = True
    
    # Disable CSRF for development
    WTF_CSRF_ENABLED = False
    
    # Session timeout longer for development
    PERMANENT_SESSION_LIFETIME = 86400
