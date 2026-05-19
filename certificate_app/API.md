# API Documentation

## Overview

The Certificate Sender Application provides a RESTful API for managing participants, sending certificates, and managing configurations.

**Base URL**: `http://localhost:5000` (development) or `https://example.com` (production)

## Authentication

Currently, the API is open. For production, consider implementing:
- API keys
- JWT tokens
- OAuth 2.0

## Response Format

All responses are in JSON format.

### Success Response

```json
{
  "status": "success",
  "data": {},
  "message": "Operation completed"
}
```

### Error Response

```json
{
  "status": "error",
  "message": "Error description",
  "code": 400
}
```

## Endpoints

### Dashboard

#### Get Dashboard Statistics

```
GET /
```

Returns dashboard statistics including participant counts and email statuses.

**Response**: HTML dashboard page

---

### Participants

#### List All Participants

```
GET /api/participants
```

Get a list of all participants.

**Response**:
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "match_status": "Matched",
    "email_status": "Pending",
    "certificate_file": "john_certificate.pdf",
    "created_at": "2024-01-01T10:00:00"
  }
]
```

**Status Codes**:
- `200` - Success
- `500` - Server error

---

### File Management

#### Upload Excel File

```
POST /api/upload
```

Upload an Excel file containing participant data.

**Request**:
- Content-Type: `multipart/form-data`
- Field: `file` (Excel file)

**Response**:
```json
{
  "message": "File uploaded successfully",
  "filename": "participants.xlsx"
}
```

**Status Codes**:
- `200` - Success
- `400` - No file provided or invalid type
- `500` - Server error

**Allowed Extensions**: `.xlsx`, `.xls`, `.pdf`, `.png`, `.jpg`, `.jpeg`

---

### Email Operations

#### Send Emails to Participants

```
POST /api/send-emails
```

Send certificates via email to selected participants.

**Request Body**:
```json
{
  "participant_ids": [1, 2, 3]
}
```

**Response**:
```json
{
  "message": "Sent 3 emails, 0 failed",
  "sent_count": 3,
  "failed_count": 0
}
```

**Status Codes**:
- `200` - Success
- `400` - No participants selected
- `500` - Server error

---

### SMTP Configuration

#### Get SMTP Settings

```
GET /api/smtp-settings
```

Retrieve current SMTP configuration.

**Response**:
```json
{
  "id": 1,
  "sender_name": "Certificate Sender",
  "smtp_server": "smtp.gmail.com",
  "smtp_port": 587,
  "updated_at": "2024-01-01T10:00:00"
}
```

**Status Codes**:
- `200` - Success
- `404` - Settings not configured
- `500` - Server error

---

#### Update SMTP Settings

```
POST /api/smtp-settings
```

Update SMTP configuration.

**Request Body**:
```json
{
  "smtp_email": "sender@gmail.com",
  "smtp_password": "app_password",
  "sender_name": "Certificate Distribution",
  "smtp_server": "smtp.gmail.com",
  "smtp_port": 587
}
```

**Response**:
```json
{
  "message": "SMTP settings updated successfully"
}
```

**Status Codes**:
- `200` - Success
- `500` - Server error

**Security Note**: SMTP password is stored in the database. Ensure database is secured and encrypted.

---

### Email Logs

#### Get Email Logs

```
GET /api/logs
```

Retrieve email sending logs (last 100 records).

**Query Parameters**:
- `limit` (optional): Number of records to return (default: 100)
- `status` (optional): Filter by status ('Sent', 'Failed')

**Response**:
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "status": "Sent",
    "error_message": null,
    "sent_at": "2024-01-01T10:00:00"
  }
]
```

**Status Codes**:
- `200` - Success
- `500` - Server error

---

## Error Codes

| Code | Message | Solution |
|------|---------|----------|
| 400 | Bad Request | Check request format and parameters |
| 404 | Not Found | Resource does not exist |
| 500 | Internal Server Error | Check server logs |
| 503 | Service Unavailable | Database or email service down |

---

## Rate Limiting

Currently not implemented. Recommended for production:
- 100 requests per minute per IP
- 1000 requests per day per API key

---

## Pagination

For large datasets, pagination is recommended:

```
GET /api/participants?page=1&per_page=20
```

---

## Filtering and Sorting

### Participants Filtering

```
GET /api/participants?status=Pending&email_status=Failed
```

### Sorting

```
GET /api/participants?sort=name&order=asc
```

---

## Webhooks

Future feature: Receive notifications for email events

```
POST https://your-domain.com/webhooks/email-status
```

Payload:
```json
{
  "event": "email.sent",
  "participant_id": 1,
  "timestamp": "2024-01-01T10:00:00",
  "status": "success"
}
```

---

## Testing the API

### Using cURL

```bash
# Get participants
curl http://localhost:5000/api/participants

# Upload file
curl -F "file=@participants.xlsx" http://localhost:5000/api/upload

# Send emails
curl -X POST http://localhost:5000/api/send-emails \
  -H "Content-Type: application/json" \
  -d '{"participant_ids": [1, 2, 3]}'
```

### Using Python Requests

```python
import requests

base_url = 'http://localhost:5000'

# Get participants
response = requests.get(f'{base_url}/api/participants')
print(response.json())

# Upload file
files = {'file': open('participants.xlsx', 'rb')}
response = requests.post(f'{base_url}/api/upload', files=files)
print(response.json())

# Send emails
data = {'participant_ids': [1, 2, 3]}
response = requests.post(f'{base_url}/api/send-emails', json=data)
print(response.json())
```

### Using Postman

1. Import endpoints from this documentation
2. Set base URL variable
3. Create request collection
4. Use Environment variables for sensitive data

---

## Best Practices

1. **Error Handling**: Always check response status codes
2. **Rate Limiting**: Implement backoff strategies
3. **Timeouts**: Set appropriate timeouts for long-running operations
4. **Validation**: Validate input data before sending
5. **Security**: Use HTTPS in production
6. **Logging**: Log all API calls for debugging

---

## Changelog

### v1.0.0
- Initial API documentation
- All endpoints documented
- Example requests included

---

For additional help, see README.md or contact support.
