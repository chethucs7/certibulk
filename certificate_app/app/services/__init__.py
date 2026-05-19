"""Email service for sending certificates."""
from flask import current_app
from flask_mail import Message
from app import mail
from app.models import db, Participant, EmailLog
import os
from datetime import datetime


def send_email_with_certificate(participant):
    """
    Send email with certificate to participant.
    
    Args:
        participant: Participant object
    
    Returns:
        bool: True if email sent successfully
    
    Raises:
        Exception: If email sending fails
    """
    try:
        if not participant.certificate_file:
            raise ValueError(f'No certificate file for {participant.name}')
        
        cert_path = os.path.join(
            current_app.config['CERT_FOLDER'],
            participant.certificate_file
        )
        
        if not os.path.exists(cert_path):
            raise FileNotFoundError(f'Certificate file not found: {cert_path}')
        
        # Create email message
        msg = Message(
            subject='Your Certificate',
            recipients=[participant.email],
            body=f'Dear {participant.name},\n\nPlease find your certificate attached.\n\nBest regards'
        )
        
        with open(cert_path, 'rb') as attachment:
            msg.attach(
                participant.certificate_file,
                'application/pdf',
                attachment.read()
            )
        
        # Send email
        mail.send(msg)
        
        # Update participant status
        participant.email_status = 'Sent'
        
        # Log email
        log = EmailLog(
            participant_id=participant.id,
            name=participant.name,
            email=participant.email,
            sender_name=current_app.config.get('MAIL_DEFAULT_SENDER', ''),
            certificate_file=participant.certificate_file,
            status='Sent'
        )
        
        db.session.add(log)
        db.session.commit()
        
        current_app.logger.info(f'Email sent successfully to {participant.email}')
        return True
    
    except Exception as e:
        # Log failure
        log = EmailLog(
            participant_id=participant.id if 'participant' in locals() else None,
            name=participant.name if 'participant' in locals() else 'Unknown',
            email=participant.email if 'participant' in locals() else 'Unknown',
            sender_name=current_app.config.get('MAIL_DEFAULT_SENDER', ''),
            certificate_file=participant.certificate_file if 'participant' in locals() else '',
            status='Failed',
            error_message=str(e)
        )
        
        db.session.add(log)
        db.session.commit()
        
        current_app.logger.error(f'Failed to send email: {str(e)}')
        raise


def send_bulk_emails(participant_ids):
    """
    Send emails to multiple participants.
    
    Args:
        participant_ids: List of participant IDs
    
    Returns:
        dict: Status of send operation
    """
    sent = 0
    failed = 0
    errors = []
    
    for participant_id in participant_ids:
        try:
            participant = Participant.query.get(participant_id)
            if participant:
                send_email_with_certificate(participant)
                sent += 1
        except Exception as e:
            failed += 1
            errors.append({'id': participant_id, 'error': str(e)})
    
    return {
        'sent': sent,
        'failed': failed,
        'errors': errors
    }
