import os
from datetime import timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-me')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + str(BASE_DIR / 'instance' / 'emg.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    UPLOAD_FOLDER = str(BASE_DIR / 'static' / 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', '')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'emgitcorporatetraining@hotmail.com')
