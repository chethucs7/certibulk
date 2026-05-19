"""Utility functions for the application."""
import os
import pandas as pd
from werkzeug.utils import secure_filename
from flask import current_app


def allowed_file(filename):
    """
    Check if file is allowed.
    
    Args:
        filename: Name of the file
    
    Returns:
        bool: True if file is allowed
    """
    if '.' not in filename:
        return False
    
    ext = filename.rsplit('.', 1)[1].lower()
    return ext in current_app.config.get('ALLOWED_EXTENSIONS', set())


def parse_excel_file(filepath):
    """
    Parse Excel file and extract participant data.
    
    Args:
        filepath: Path to Excel file
    
    Returns:
        list: List of dictionaries with participant data
    
    Raises:
        Exception: If file cannot be parsed
    """
    try:
        df = pd.read_excel(filepath)
        
        # Validate required columns
        required_columns = ['name', 'email']
        if not all(col in df.columns for col in required_columns):
            raise ValueError(f'Excel file must contain columns: {required_columns}')
        
        # Convert to list of dictionaries
        data = df.to_dict('records')
        
        return data
    
    except Exception as e:
        raise Exception(f'Error parsing Excel file: {str(e)}')


def get_file_size_mb(filepath):
    """
    Get file size in MB.
    
    Args:
        filepath: Path to file
    
    Returns:
        float: File size in MB
    """
    if os.path.exists(filepath):
        return os.path.getsize(filepath) / (1024 * 1024)
    return 0


def safe_filename(filename):
    """
    Create a safe filename.
    
    Args:
        filename: Original filename
    
    Returns:
        str: Sanitized filename
    """
    return secure_filename(filename)
