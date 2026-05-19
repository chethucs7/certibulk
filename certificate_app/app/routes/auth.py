"""Routes package."""
from flask import Blueprint

main_bp = Blueprint('main', __name__)

# Import routes
from app.routes import main_bp  # noqa: F401
