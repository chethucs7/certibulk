"""Test basic routes."""
import pytest


def test_index_route(client):
    """Test the index route."""
    response = client.get('/')
    assert response.status_code == 200


def test_get_participants(client):
    """Test get participants endpoint."""
    response = client.get('/api/participants')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_smtp_settings_not_configured(client):
    """Test SMTP settings when not configured."""
    response = client.get('/api/smtp-settings')
    assert response.status_code == 404
