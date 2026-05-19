"""Database models for Certificate Application."""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class SMTPSettings(db.Model):
    """SMTP configuration settings."""
    __tablename__ = 'smtp_settings'
    
    id = db.Column(db.Integer, primary_key=True)
    smtp_email = db.Column(db.String(255), nullable=False, unique=True)
    smtp_password = db.Column(db.String(255), nullable=False)
    sender_name = db.Column(db.String(255), default='Certificate Sender')
    smtp_server = db.Column(db.String(255), default='smtp.gmail.com')
    smtp_port = db.Column(db.Integer, default=587)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<SMTPSettings {self.sender_name}>'


class EmailTemplate(db.Model):
    """Email template configuration."""
    __tablename__ = 'email_templates'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    subject = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    def __repr__(self):
        return f'<EmailTemplate {self.name}>'


class Participant(db.Model):
    """Participant data for certificate distribution."""
    __tablename__ = 'participants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    certificate_file = db.Column(db.String(255), default=None)
    match_status = db.Column(
        db.Enum('Missing', 'Matched'),
        default='Missing',
        nullable=False
    )
    email_status = db.Column(
        db.Enum('Pending', 'Sent', 'Failed'),
        default='Pending',
        nullable=False
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Participant {self.name}>'


class EmailLog(db.Model):
    """Email sending log for audit trail."""
    __tablename__ = 'email_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(
        db.Integer,
        db.ForeignKey('participants.id', ondelete='SET NULL'),
        nullable=True
    )
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    sender_name = db.Column(db.String(255))
    certificate_file = db.Column(db.String(255))
    status = db.Column(db.Enum('Sent', 'Failed'), nullable=False)
    error_message = db.Column(db.Text)
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<EmailLog {self.name} - {self.status}>'
