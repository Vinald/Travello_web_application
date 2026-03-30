"""
Views for the accounts app.
Handles user registration, login, and logout.
"""

import logging
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import RegistrationForm, LoginForm
from core.decorators import log_action

logger = logging.getLogger(__name__)


class RegisterView(View):
    """
    User registration view.
    Handles both GET (display form) and POST (process registration) requests.
    """
    template_name = 'account/register.html'
    form_class = RegistrationForm

    def get(self, request):
        """Display registration form."""
        if request.user.is_authenticated:
            return redirect('/')

        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """Process registration form submission."""
        form = self.form_class(request.POST)

        if form.is_valid():
            try:
                user = form.save()
                logger.info(f"New user registered: {user.username}")
                messages.success(request, 'Registration successful! Please log in.')
                return redirect('login')
            except Exception as e:
                logger.error(f"Registration error for user: {str(e)}")
                messages.error(request, 'Registration failed. Please try again.')
        else:
            # Add form errors to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

        return render(request, self.template_name, {'form': form})


class LoginView(View):
    """
    User login view.
    Handles both GET (display form) and POST (process login) requests.
    """
    template_name = 'account/login.html'
    form_class = LoginForm

    def get(self, request):
        """Display login form."""
        if request.user.is_authenticated:
            return redirect('/')

        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    @log_action("User Login Attempt")
    def post(self, request):
        """Process login form submission."""
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Try to authenticate user
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                logger.info(f"User logged in: {user.username}")
                messages.success(request, f'Welcome back, {user.first_name or user.username}!')

                # Redirect to next page if provided, otherwise home
                next_page = request.GET.get('next', '/')
                return redirect(next_page)
            else:
                logger.warning(f"Failed login attempt for username: {username}")
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors below.')

        return render(request, self.template_name, {'form': form})


@method_decorator(login_required(login_url='login'), name='dispatch')
class LogoutView(View):
    """
    User logout view.
    """

    def get(self, request):
        """Process logout request."""
        username = request.user.username
        auth.logout(request)
        logger.info(f"User logged out: {username}")
        messages.success(request, 'You have been logged out successfully.')
        return redirect('/')


# Keep functional views for backward compatibility
def register(request):
    """Functional view for registration (delegates to RegisterView)."""
    view = RegisterView.as_view()
    return view(request)


def login(request):
    """Functional view for login (delegates to LoginView)."""
    view = LoginView.as_view()
    return view(request)


def logout(request):
    """Functional view for logout (delegates to LogoutView)."""
    view = LogoutView.as_view()
    return view(request)
