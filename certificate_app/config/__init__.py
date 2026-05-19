"""Configuration module."""
import os

def get_config():
    """Get configuration based on environment."""
    env = os.getenv('FLASK_ENV', 'development').lower()
    
    if env == 'production':
        from config.production import ProductionConfig
        return ProductionConfig
    elif env == 'testing':
        from config.testing import TestingConfig
        return TestingConfig
    else:
        from config.development import DevelopmentConfig
        return DevelopmentConfig
