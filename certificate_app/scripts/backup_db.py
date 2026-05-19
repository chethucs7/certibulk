#!/usr/bin/env python
"""Database backup and restore utility."""
import sys
import os
import sqlite3
import subprocess
from pathlib import Path
from datetime import datetime

project_dir = Path(__file__).parent.parent.absolute()
sys.path.insert(0, str(project_dir))

from app import create_app

def backup_sqlite():
    """Backup SQLite database."""
    app = create_app()
    
    db_file = 'certificate_sender.db'
    backup_dir = project_dir / 'backups'
    backup_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = backup_dir / f'certificate_sender_backup_{timestamp}.db'
    
    try:
        import shutil
        shutil.copy2(db_file, backup_file)
        print(f"✓ SQLite database backed up to: {backup_file}")
        return str(backup_file)
    except Exception as e:
        print(f"✗ Backup failed: {str(e)}")
        sys.exit(1)

def backup_mysql(host, user, password, database):
    """Backup MySQL database."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_dir = project_dir / 'backups'
    backup_dir.mkdir(exist_ok=True)
    
    backup_file = backup_dir / f'{database}_backup_{timestamp}.sql'
    
    cmd = [
        'mysqldump',
        f'-h{host}',
        f'-u{user}',
        f'-p{password}',
        database
    ]
    
    try:
        with open(backup_file, 'w') as f:
            subprocess.run(cmd, stdout=f, check=True)
        print(f"✓ MySQL database backed up to: {backup_file}")
        return str(backup_file)
    except Exception as e:
        print(f"✗ Backup failed: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'mysql':
        backup_mysql('localhost', 'root', '', 'certificate_sender')
    else:
        backup_sqlite()
