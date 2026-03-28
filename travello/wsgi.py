"""
WSGI config for travello project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from pathlib import Path

# Set environment to production if not already set
if 'ENVIRONMENT' not in os.environ:
    os.environ['ENVIRONMENT'] = os.getenv('ENVIRONMENT', 'development')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travello.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
