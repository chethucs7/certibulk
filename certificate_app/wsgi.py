"""WSGI application entry point for production."""
import os
import sys
from pathlib import Path

# Add the project directory to the Python path
project_dir = Path(__file__).parent.absolute()
sys.path.insert(0, str(project_dir))

from app import create_app

# Create Flask app
app = create_app()

if __name__ == '__main__':
    app.run()
