"""
Models for the destination app.
Contains Destination, NewsPosts, Testimonial, and HomeSlider models.
"""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, URLValidator
from core.models import BaseModel


class Destination(BaseModel):
    """
    Model representing a travel destination.

    Attributes:
        name: Destination name (max 100 chars)
        image: Destination image
        price: Price for visiting (must be >= 0)
        description: Detailed description
        offer: Whether the destination is on offer
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        help_text="Destination name"
    )
    image = models.ImageField(
        upload_to="pictures",
        help_text="Destination image"
    )
    price = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        help_text="Price for visiting this destination"
    )
    description = models.TextField(
        help_text="Detailed description of the destination"
    )
    offer = models.BooleanField(
        default=False,
        db_index=True,
        help_text="Is this destination on special offer?"
    )

    class Meta:
        verbose_name = "Destination"
        verbose_name_plural = "Destinations"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['offer', '-created_at']),
            models.Index(fields=['price']),
        ]

    def __str__(self):
        return f"{self.name} (${self.price})"

    def __repr__(self):
        return f"<Destination: {self.name}>"


class NewsPosts(BaseModel):
    """
    Model representing blog posts or news articles about travel.

    Attributes:
        image: Article cover image
        date: Date of publication
        month: Month of publication
        title: Article title
        category: Article category
        content: Article content
    """
    image = models.ImageField(
        upload_to="news_pictures",
        help_text="Article cover image"
    )
    date = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(31)],
        help_text="Day of the month (1-31)"
    )
    month = models.CharField(
        max_length=20,
        help_text="Month name"
    )
    title = models.CharField(
        max_length=200,
        db_index=True,
        help_text="Article title"
    )
    category = models.CharField(
        max_length=100,
        db_index=True,
        help_text="Article category"
    )
    content = models.TextField(
        help_text="Article content"
    )

    class Meta:
        verbose_name = "News Post"
        verbose_name_plural = "News Posts"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['category', '-created_at']),
        ]

    def __str__(self):
        return f"{self.title} ({self.month} {self.date})"

    def __repr__(self):
        return f"<NewsPosts: {self.title}>"


class Testimonial(BaseModel):
    """
    Model representing customer testimonials.

    Attributes:
        content: Testimonial text
        author: Author's name
        position: Author's position/title
    """
    content = models.TextField(
        help_text="Testimonial content"
    )
    author = models.CharField(
        max_length=100,
        db_index=True,
        help_text="Testimonial author's name"
    )
    position = models.CharField(
        max_length=100,
        help_text="Author's position or title"
    )

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author} - {self.position}"

    def __repr__(self):
        return f"<Testimonial: {self.author}>"


class HomeSlider(BaseModel):
    """
    Model representing images for the home page slider.

    Attributes:
        title: Slider image title
        image: Slider image
    """
    title = models.CharField(
        max_length=200,
        help_text="Slider image title"
    )
    image = models.ImageField(
        upload_to="home_slider_pictures",
        help_text="Slider image"
    )

    class Meta:
        verbose_name = "Home Slider"
        verbose_name_plural = "Home Sliders"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<HomeSlider: {self.title}>"
