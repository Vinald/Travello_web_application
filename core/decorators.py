"""
Custom decorators for the Travello application.
"""

from functools import wraps
from django.contrib.auth.decorators import login_required as django_login_required
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)


def login_required(view_func):
    """
    Enhanced login_required decorator that handles both regular views and AJAX requests.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'error': 'Unauthorized'}, status=401)
            return django_login_required(view_func)(request, *args, **kwargs)
        return view_func(request, *args, **kwargs)
    return wrapper


def require_ajax(view_func):
    """
    Decorator to ensure a view only accepts AJAX requests.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'error': 'Bad Request'}, status=400)
        return view_func(request, *args, **kwargs)
    return wrapper


def log_action(action_name):
    """
    Decorator to log user actions.
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            logger.info(
                f"Action: {action_name} | User: {request.user} | IP: {get_client_ip(request)}"
            )
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


def get_client_ip(request):
    """
    Get the client IP address from the request.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

