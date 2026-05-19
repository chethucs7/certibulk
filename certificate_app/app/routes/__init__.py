"""Main routes blueprint."""
from flask import Blueprint, render_template, request, jsonify, current_app, send_from_directory, send_file
from werkzeug.utils import secure_filename
import pandas as pd
import io
import os
from datetime import datetime
from app.models import db, Participant, SMTPSettings, EmailTemplate, EmailLog
from app.services.email_service import send_email_with_certificate

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Dashboard homepage."""
    stats = {
        'total_participants': Participant.query.count(),
        'sent_emails': Participant.query.filter_by(email_status='Sent').count(),
        'failed_emails': Participant.query.filter_by(email_status='Failed').count(),
        'pending_emails': Participant.query.filter_by(email_status='Pending').count(),
    }
    return render_template('dashboard.html', stats=stats)


@main_bp.route('/api/upload', methods=['POST'])
def upload_file():
    """Handle file upload."""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not _allowed_file(file.filename):
            return jsonify({'error': 'File type not allowed'}), 400
        
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['EXCEL_FOLDER'], filename)
        file.save(filepath)
        
        current_app.logger.info(f'File uploaded: {filename}')
        return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200
    
    except Exception as e:
        current_app.logger.error(f'Upload error: {str(e)}')
        return jsonify({'error': str(e)}), 500


@main_bp.route('/api/participants', methods=['GET'])
def get_participants():
    """Get all participants."""
    try:
        participants = Participant.query.all()
        return jsonify([{
            'id': p.id,
            'name': p.name,
            'email': p.email,
            'match_status': p.match_status,
            'email_status': p.email_status,
            'certificate_file': p.certificate_file,
            'created_at': p.created_at.isoformat()
        } for p in participants]), 200
    except Exception as e:
        current_app.logger.error(f'Get participants error: {str(e)}')
        return jsonify({'error': str(e)}), 500


@main_bp.route('/api/send-emails', methods=['POST'])
def send_emails():
    """Send emails to participants."""
    try:
        data = request.get_json()
        participant_ids = data.get('participant_ids', [])
        
        if not participant_ids:
            return jsonify({'error': 'No participants selected'}), 400
        
        participants = Participant.query.filter(Participant.id.in_(participant_ids)).all()
        
        sent_count = 0
        failed_count = 0
        
        for participant in participants:
            try:
                send_email_with_certificate(participant)
                sent_count += 1
            except Exception as e:
                current_app.logger.error(f'Failed to send email to {participant.email}: {str(e)}')
                failed_count += 1
        
        return jsonify({
            'message': f'Sent {sent_count} emails, {failed_count} failed',
            'sent_count': sent_count,
            'failed_count': failed_count
        }), 200
    
    except Exception as e:
        current_app.logger.error(f'Send emails error: {str(e)}')
        return jsonify({'error': str(e)}), 500


@main_bp.route('/api/smtp-settings', methods=['GET', 'POST'])
def smtp_settings():
    """Get or update SMTP settings."""
    try:
        if request.method == 'GET':
            settings = SMTPSettings.query.first()
            if not settings:
                return jsonify({'error': 'SMTP settings not configured'}), 404
            
            return jsonify({
                'id': settings.id,
                'sender_name': settings.sender_name,
                'smtp_server': settings.smtp_server,
                'smtp_port': settings.smtp_port,
                'updated_at': settings.updated_at.isoformat()
            }), 200
        
        elif request.method == 'POST':
            data = request.get_json()
            
            settings = SMTPSettings.query.first()
            if not settings:
                settings = SMTPSettings()
                db.session.add(settings)
            
            settings.smtp_email = data.get('smtp_email', settings.smtp_email)
            settings.smtp_password = data.get('smtp_password', settings.smtp_password)
            settings.sender_name = data.get('sender_name', settings.sender_name)
            settings.smtp_server = data.get('smtp_server', settings.smtp_server)
            settings.smtp_port = int(data.get('smtp_port', settings.smtp_port))
            
            db.session.commit()
            current_app.logger.info('SMTP settings updated')
            
            return jsonify({'message': 'SMTP settings updated successfully'}), 200
    
    except Exception as e:
        current_app.logger.error(f'SMTP settings error: {str(e)}')
        return jsonify({'error': str(e)}), 500


@main_bp.route('/api/logs', methods=['GET'])
def get_logs():
    """Get email logs."""
    try:
        logs = EmailLog.query.order_by(EmailLog.sent_at.desc()).limit(100).all()
        
        return jsonify([{
            'id': log.id,
            'name': log.name,
            'email': log.email,
            'status': log.status,
            'error_message': log.error_message,
            'sent_at': log.sent_at.isoformat()
        } for log in logs]), 200
    except Exception as e:
        current_app.logger.error(f'Get logs error: {str(e)}')
        return jsonify({'error': str(e)}), 500


def _allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']
