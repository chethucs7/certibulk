"""Test configuration and fixtures."""
import pytest
import os
import sys
from pathlib import Path

# Add the project directory to the Python path
project_dir = Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(project_dir))

from app import create_app, db
from config.testing import TestingConfig


@pytest.fixture
def app():
    """Create and configure a test application."""
    app = create_app('testing')
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """Test client for making requests."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Test runner for CLI commands."""
    return app.test_cli_runner()
