"""Django settings for API Gateway"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-gateway-secret-key-change-in-production'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'rest_framework',
    'corsheaders',
    'gateway',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'gateway_project.urls'

WSGI_APPLICATION = 'gateway_project.wsgi.application'

DATABASES = {}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Service URLs
AUTH_SERVICE_URL = os.environ.get('AUTH_SERVICE_URL', 'http://auth:8000')
CUSTOMER_SERVICE_URL = os.environ.get('CUSTOMER_SERVICE_URL', 'http://customer:8000')
STAFF_SERVICE_URL = os.environ.get('STAFF_SERVICE_URL', 'http://staff:8000')
LAPTOP_SERVICE_URL = os.environ.get('LAPTOP_SERVICE_URL', 'http://laptop:8000')
MOBILE_SERVICE_URL = os.environ.get('MOBILE_SERVICE_URL', 'http://mobile:8000')

# JWT Settings
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'your-secret-key')
JWT_ALGORITHM = 'HS256'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}
