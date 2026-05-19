"""Test database models."""
import pytest
from app.models import db, Participant, SMTPSettings, EmailTemplate, EmailLog


def test_create_participant(app):
    """Test creating a participant."""
    with app.app_context():
        participant = Participant(
            name='John Doe',
            email='john@example.com',
            match_status='Matched'
        )
        db.session.add(participant)
        db.session.commit()
        
        assert participant.id is not None
        assert participant.name == 'John Doe'
        assert participant.email_status == 'Pending'


def test_create_smtp_settings(app):
    """Test creating SMTP settings."""
    with app.app_context():
        settings = SMTPSettings(
            smtp_email='test@gmail.com',
            smtp_password='password123',
            sender_name='Test Sender'
        )
        db.session.add(settings)
        db.session.commit()
        
        assert settings.id is not None
        assert settings.sender_name == 'Test Sender'


def test_create_email_log(app):
    """Test creating an email log."""
    with app.app_context():
        log = EmailLog(
            name='Test User',
            email='test@example.com',
            status='Sent'
        )
        db.session.add(log)
        db.session.commit()
        
        assert log.id is not None
        assert log.status == 'Sent'
