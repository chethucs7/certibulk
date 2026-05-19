#!/usr/bin/env python
"""Development server entry point."""
import os
import sys
from pathlib import Path

# Add the project directory to the Python path
project_dir = Path(__file__).parent.absolute()
sys.path.insert(0, str(project_dir))

from app import create_app

if __name__ == '__main__':
    app = create_app()
    
    host = os.getenv('FLASK_HOST', '127.0.0.1')
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_ENV', 'development') == 'development'
    
    app.run(
        host=host,
        port=port,
        debug=debug,
        use_reloader=True
    )
