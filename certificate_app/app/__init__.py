"""Flask application factory."""
import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from app.models import db

mail = Mail()

def create_app(config_name=None):
    """
    Create and configure the Flask application.
    
    Args:
        config_name: Configuration environment (development, production, testing)
                     If None, uses FLASK_ENV environment variable
    
    Returns:
        Flask: Configured Flask application
    """
    app = Flask(__name__, 
                template_folder='templates',
                static_folder='static')
    
    # Load configuration
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    if config_name.lower() == 'production':
        from config.production import ProductionConfig
        app.config.from_object(ProductionConfig)
    elif config_name.lower() == 'testing':
        from config.testing import TestingConfig
        app.config.from_object(TestingConfig)
    else:
        from config.development import DevelopmentConfig
        app.config.from_object(DevelopmentConfig)
    
    # Initialize extensions
    db.init_app(app)
    mail.init_app(app)
    CORS(app, origins=app.config.get('CORS_ORIGINS', '*'))
    
    # Create necessary directories
    _create_directories(app)
    
    # Setup logging
    _setup_logging(app)
    
    # Register blueprints
    _register_blueprints(app)
    
    # Register CLI commands
    _register_cli_commands(app)
    
    with app.app_context():
        db.create_all()
    
    return app


def _create_directories(app):
    """Create necessary directories."""
    directories = [
        app.config['UPLOAD_FOLDER'],
        app.config['EXCEL_FOLDER'],
        app.config['CERT_FOLDER'],
        os.path.dirname(app.config['LOG_FILE'])
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def _setup_logging(app):
    """Configure logging."""
    if not app.debug and not app.testing:
        log_file = app.config['LOG_FILE']
        
        if not os.path.exists(os.path.dirname(log_file)):
            os.makedirs(os.path.dirname(log_file))
        
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=10485760,  # 10MB
            backupCount=10
        )
        
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        
        file_handler.setLevel(app.config['LOG_LEVEL'])
        app.logger.addHandler(file_handler)
        app.logger.setLevel(app.config['LOG_LEVEL'])


def _register_blueprints(app):
    """Register Flask blueprints."""
    from app.routes import main_bp
    app.register_blueprint(main_bp)


def _register_cli_commands(app):
    """Register CLI commands."""
    @app.cli.command()
    def init_db():
        """Initialize the database."""
        db.create_all()
        app.logger.info('Database initialized.')
    
    @app.cli.command()
    def seed_db():
        """Seed the database with sample data."""
        from app.models import SMTPSettings, EmailTemplate
        
        if SMTPSettings.query.first():
            app.logger.info('Database already seeded.')
            return
        
        # Add sample data
        app.logger.info('Database seeded successfully.')
