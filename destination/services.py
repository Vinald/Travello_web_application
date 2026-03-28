"""
Service layer for destination app business logic.
"""

import logging
from django.db.models import Q
from .models import Destination, NewsPosts

logger = logging.getLogger(__name__)


def get_featured_destinations(limit=6):
    """
    Get featured destinations (those on offer).

    Args:
        limit: Number of destinations to return

    Returns:
        QuerySet of featured destinations
    """
    return Destination.objects.filter(offer=True).order_by('-created_at')[:limit]


def get_destinations_by_price_range(min_price, max_price):
    """
    Get destinations within a price range.

    Args:
        min_price: Minimum price
        max_price: Maximum price

    Returns:
        QuerySet of destinations in price range
    """
    return Destination.objects.filter(
        price__gte=min_price,
        price__lte=max_price
    ).order_by('price')


def search_destinations(query):
    """
    Search destinations by name or description.

    Args:
        query: Search query string

    Returns:
        QuerySet of matching destinations
    """
    return Destination.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query)
    ).order_by('-created_at')


def get_latest_news(limit=6):
    """
    Get latest news posts.

    Args:
        limit: Number of posts to return

    Returns:
        QuerySet of latest news posts
    """
    return NewsPosts.objects.all().order_by('-created_at')[:limit]


def get_news_by_category(category):
    """
    Get news posts by category.

    Args:
        category: News category

    Returns:
        QuerySet of news posts in category
    """
    return NewsPosts.objects.filter(category=category).order_by('-created_at')

