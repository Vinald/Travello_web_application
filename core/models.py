"""
Base model class with common fields like created_at and updated_at.
"""

from django.db import models


class BaseModel(models.Model):
    """
    Abstract base model for all models in the application.
    Provides common fields: created_at, updated_at
    """
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Automatically set when the object is created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Automatically updated when the object is modified"
    )

    class Meta:
        abstract = True
        ordering = ['-created_at']

    def __repr__(self):
        return f"<{self.__class__.__name__} pk={self.pk}>"
