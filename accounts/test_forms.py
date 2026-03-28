"""
Form tests for the accounts app.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from accounts.forms import RegistrationForm, LoginForm


class RegistrationFormTests(TestCase):
    """Tests for the RegistrationForm."""

    def test_valid_registration(self):
        """Test that a valid registration form is accepted."""
        form_data = {
            'username': 'newuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'password1': 'securepass123',
            'password2': 'securepass123',
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_password_mismatch(self):
        """Test that mismatched passwords are rejected."""
        form_data = {
            'username': 'newuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'password1': 'securepass123',
            'password2': 'differentpass123',
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Passwords do not match', str(form.errors))

    def test_duplicate_username(self):
        """Test that duplicate usernames are rejected."""
        User.objects.create_user(username='existinguser', email='existing@example.com', password='pass123')
        form_data = {
            'username': 'existinguser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'password1': 'securepass123',
            'password2': 'securepass123',
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_duplicate_email(self):
        """Test that duplicate emails are rejected."""
        User.objects.create_user(username='existinguser', email='existing@example.com', password='pass123')
        form_data = {
            'username': 'newuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'existing@example.com',
            'password1': 'securepass123',
            'password2': 'securepass123',
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_password_too_short(self):
        """Test that short passwords are rejected."""
        form_data = {
            'username': 'newuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'password1': 'short',
            'password2': 'short',
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())


class LoginFormTests(TestCase):
    """Tests for the LoginForm."""

    def test_valid_login_form(self):
        """Test that a valid login form is accepted."""
        form_data = {
            'username': 'testuser',
            'password': 'testpass123',
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_remember_me_checkbox(self):
        """Test that remember me checkbox works."""
        form_data = {
            'username': 'testuser',
            'password': 'testpass123',
            'remember_me': True,
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertTrue(form.cleaned_data['remember_me'])

