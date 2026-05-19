"""
Production configuration.
"""
import os
from config.default import Config

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    TESTING = False
    
    # MySQL for production
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'mysql+mysqlconnector://root:@localhost/certificate_sender'
    )
    
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError(
            'DATABASE_URL environment variable not set. '
            'This is required for production.'
        )
    
    # Security
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Must set a strong secret key
    if os.getenv('SECRET_KEY') == 'dev-secret-key-change-in-production':
        raise ValueError(
            'SECRET_KEY must be set in production environment. '
            'Use a strong, randomly generated key.'
        )
