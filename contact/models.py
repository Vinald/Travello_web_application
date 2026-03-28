"""
Models for the contact app.
"""

from django.db import models
from core.models import BaseModel


class Contact(BaseModel):
    """
    Model to store contact form submissions.

    Attributes:
        name: Visitor's name
        email: Visitor's email address
        subject: Message subject
        message: Message content
        is_read: Whether admin has read the message
    """
    STATUS_CHOICES = [
        ('new', 'New'),
        ('read', 'Read'),
        ('replied', 'Replied'),
    ]

    name = models.CharField(
        max_length=100,
        db_index=True,
        help_text="Sender's name"
    )
    email = models.EmailField(
        db_index=True,
        help_text="Sender's email address"
    )
    subject = models.CharField(
        max_length=200,
        help_text="Message subject"
    )
    message = models.TextField(
        help_text="Message content"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        db_index=True,
        help_text="Message status"
    )
    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True,
        help_text="Sender's IP address"
    )

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status', '-created_at']),
        ]

    def __str__(self):
        return f"{self.subject} from {self.name}"

    def __repr__(self):
        return f"<Contact: {self.subject}>"
