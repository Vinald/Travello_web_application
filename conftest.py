"""
Pytest configuration and fixtures for Travello application.
"""

import os
import django
from django.conf import settings
import pytest


def pytest_configure():
    """Configure Django settings for testing."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travello.settings')
    if not settings.configured:
        django.setup()


@pytest.fixture
def django_db_setup():
    """Setup test database."""
    pass


@pytest.fixture
def admin_user(db):
    """Create and return an admin user."""
    from django.contrib.auth.models import User
    return User.objects.create_superuser(
        username='admin',
        email='admin@test.com',
        password='admin123'
    )


@pytest.fixture
def test_user(db):
    """Create and return a regular user."""
    from django.contrib.auth.models import User
    return User.objects.create_user(
        username='testuser',
        email='test@test.com',
        password='test123',
        first_name='Test',
        last_name='User'
    )


@pytest.fixture
def destination(db):
    """Create and return a test destination."""
    from destination.models import Destination
    return Destination.objects.create(
        name='Test Destination',
        price=100,
        description='A test destination',
        offer=False
    )


@pytest.fixture
def featured_destination(db):
    """Create and return a featured destination."""
    from destination.models import Destination
    return Destination.objects.create(
        name='Featured Destination',
        price=200,
        description='A featured destination',
        offer=True
    )


@pytest.fixture
def contact_message(db):
    """Create and return a test contact message."""
    from contact.models import Contact
    return Contact.objects.create(
        name='John Doe',
        email='john@test.com',
        subject='Test Subject',
        message='Test message content',
        status='new'
    )

