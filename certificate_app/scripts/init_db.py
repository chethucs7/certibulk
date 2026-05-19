#!/usr/bin/env python
"""Database initialization and migration script."""
import sys
import os
from pathlib import Path

# Add the project directory to the Python path
project_dir = Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(project_dir))

from app import create_app, db
from app.models import SMTPSettings, EmailTemplate

def init_database():
    """Initialize the database."""
    app = create_app()
    
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("✓ Database tables created successfully")
        
        # Check if already seeded
        if SMTPSettings.query.first():
            print("⚠ Database already contains data")
            return
        
        print("\nSeeding sample data...")
        
        # Add sample SMTP settings
        smtp = SMTPSettings(
            smtp_email='example@gmail.com',
            smtp_password='app_password_here',
            sender_name='Certificate Sender',
            smtp_server='smtp.gmail.com',
            smtp_port=587
        )
        db.session.add(smtp)
        
        # Add sample email template
        template = EmailTemplate(
            name='Certificate Distribution',
            subject='Your Certificate - [EVENT_NAME]',
            message='''Dear {name},

Congratulations! Please find your certificate attached.

This certificate is issued to acknowledge your participation and achievement.

Best regards,
Certificate Sender Team'''
        )
        db.session.add(template)
        
        db.session.commit()
        print("✓ Sample data seeded successfully")
        
        print("\n✓ Database initialization completed!")
        print("\nNext steps:")
        print("1. Update SMTP settings in the application dashboard")
        print("2. Upload participant Excel file")
        print("3. Start sending certificates!")

if __name__ == '__main__':
    try:
        init_database()
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        sys.exit(1)
