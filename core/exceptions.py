"""
Custom exceptions for the Travello application.
"""


class TravelloException(Exception):
    """Base exception for Travello application."""
    pass


class ValidationError(TravelloException):
    """Raised when validation fails."""
    pass


class NotFoundError(TravelloException):
    """Raised when a resource is not found."""
    pass


class UnauthorizedError(TravelloException):
    """Raised when user is not authorized to perform an action."""
    pass


class RateLimitError(TravelloException):
    """Raised when rate limit is exceeded."""
    pass


class ExternalServiceError(TravelloException):
    """Raised when an external service call fails."""
    pass

