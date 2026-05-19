#!/usr/bin/env python
"""Create sample test data."""
import sys
from pathlib import Path

project_dir = Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(project_dir))

from app import create_app, db
from app.models import Participant

def create_sample_data():
    """Create sample participant data for testing."""
    app = create_app()
    
    sample_participants = [
        Participant(
            name='John Doe',
            email='john@example.com',
            match_status='Matched',
            certificate_file='john_certificate.pdf'
        ),
        Participant(
            name='Jane Smith',
            email='jane@example.com',
            match_status='Matched',
            certificate_file='jane_certificate.pdf'
        ),
        Participant(
            name='Bob Johnson',
            email='bob@example.com',
            match_status='Matched',
            certificate_file='bob_certificate.pdf'
        ),
    ]
    
    with app.app_context():
        # Check if data already exists
        if Participant.query.count() > 0:
            print("⚠ Sample data already exists")
            return
        
        for participant in sample_participants:
            db.session.add(participant)
        
        db.session.commit()
        print(f"✓ Created {len(sample_participants)} sample participants")

if __name__ == '__main__':
    try:
        create_sample_data()
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        sys.exit(1)
