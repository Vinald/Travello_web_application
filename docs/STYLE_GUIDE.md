# Code Style Guide

## Python Code Style

We follow [PEP 8](https://pep8.org/) with some additional guidelines.

### Naming Conventions

- **Modules**: `snake_case` (e.g., `destination_views.py`)
- **Classes**: `PascalCase` (e.g., `DestinationAdmin`)
- **Functions/Methods**: `snake_case` (e.g., `get_featured_destinations()`)
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_ITEMS_PER_PAGE`)
- **Private Methods**: prefix with `_` (e.g., `_internal_method()`)

### Imports

```python
# Standard library imports first
import os
import sys
from pathlib import Path

# Related third party imports
from django.db import models
from django.contrib.auth.models import User

# Local application imports
from core.models import BaseModel
from destination.services import get_featured_destinations
```

### Class Definitions

```python
class DestinationAdmin(admin.ModelAdmin):
    """
    Admin interface for Destination model.
    
    This class provides a customized admin interface with filtering,
    search, and custom actions for managing destinations.
    """
    list_display = ['name', 'price', 'offer']
    list_filter = ['offer', 'created_at']
    search_fields = ['name', 'description']

    def get_queryset(self, request):
        """Optimize database queries."""
        return super().get_queryset(request).select_related('category')
```

### Function Documentation

```python
def search_destinations(query, limit=10):
    """
    Search destinations by name or description.
    
    Args:
        query (str): Search query string
        limit (int): Maximum number of results. Defaults to 10.
    
    Returns:
        QuerySet: Destination objects matching the query
    
    Raises:
        ValueError: If query is empty
    
    Example:
        >>> results = search_destinations('paris', limit=5)
    """
    if not query:
        raise ValueError("Query cannot be empty")
    
    return Destination.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query)
    )[:limit]
```

### Line Length

Maximum 100 characters per line. Use line continuation for long lines:

```python
# Bad
context = {'destination': destination, 'news_posts': news_posts, 'testimonials': testimonials, 'sliders': sliders}

# Good
context = {
    'destination': destination,
    'news_posts': news_posts,
    'testimonials': testimonials,
    'sliders': sliders,
}
```

## Django Specific Guidelines

### Models

```python
from core.models import BaseModel
from django.db import models

class Destination(BaseModel):
    """
    Model representing a travel destination.
    
    Inherits from BaseModel for automatic timestamps.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        help_text="Destination name"
    )
    price = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        help_text="Price for visiting"
    )

    class Meta:
        verbose_name = "Destination"
        verbose_name_plural = "Destinations"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return f"{self.name} (${self.price})"
```

### Views

```python
from django.views import View
from django.views.generic import ListView
import logging

logger = logging.getLogger(__name__)

class DestinationListView(ListView):
    """List view for all destinations."""
    model = Destination
    template_name = 'destination_list.html'
    context_object_name = 'destinations'
    paginate_by = 12

    def get_queryset(self):
        """Optimize queries."""
        queryset = Destination.objects.all()
        
        # Apply filters
        if self.request.GET.get('offer'):
            queryset = queryset.filter(offer=True)
        
        return queryset.order_by('-created_at')
```

### Forms

```python
from django import forms
from django.core.exceptions import ValidationError

class DestinationFilterForm(forms.Form):
    """Form for filtering destinations."""
    price_min = forms.IntegerField(
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    price_max = forms.IntegerField(
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    def clean(self):
        """Validate price range."""
        cleaned_data = super().clean()
        price_min = cleaned_data.get('price_min')
        price_max = cleaned_data.get('price_max')

        if price_min and price_max and price_min > price_max:
            raise ValidationError("Min price cannot be greater than max price")

        return cleaned_data
```

### Admin Configuration

```python
from django.contrib import admin

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    """Admin interface for destinations."""
    list_display = ['name', 'price', 'offer', 'created_at']
    list_filter = ['offer', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Basic', {
            'fields': ('name', 'description')
        }),
        ('Details', {
            'fields': ('price', 'offer', 'image')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        """Prevent editing of certain fields."""
        if obj:
            return self.readonly_fields + ['price']
        return self.readonly_fields
```

## Template Guidelines

### Naming

- Use lowercase with underscores: `destination_list.html`
- Use meaningful names: `destination_detail.html` not `page.html`

### Structure

```html
{% extends 'base.html' %}
{% load static %}

{% block title %}Destinations - Travello{% endblock %}

{% block content %}
<div class="container">
    <!-- Page content -->
</div>
{% endblock %}

{% block extra_js %}
<script>
    // Inline scripts if necessary
</script>
{% endblock %}
```

### Static Files

```html
<!-- Always use {% static %} tag -->
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

## Testing Guidelines

### Test File Naming

- `test_models.py` - Model tests
- `test_views.py` - View tests
- `test_forms.py` - Form tests
- `test_services.py` - Service/utility tests

### Test Structure

```python
import pytest
from django.test import TestCase

class DestinationModelTests(TestCase):
    """Tests for Destination model."""

    def setUp(self):
        """Set up test fixtures."""
        self.destination = Destination.objects.create(
            name='Test',
            price=100
        )

    def test_destination_creation(self):
        """Test that destination is created correctly."""
        self.assertEqual(self.destination.name, 'Test')
        self.assertEqual(self.destination.price, 100)

    def test_destination_str(self):
        """Test string representation."""
        expected = 'Test ($100)'
        self.assertEqual(str(self.destination), expected)
```

### Test Best Practices

1. **One assertion per test when possible**
2. **Descriptive test names** (what it tests, what it expects)
3. **Use setUp/tearDown** for common code
4. **Mock external services**
5. **Test edge cases**

## Code Comments

### When to Comment

Comment WHY, not WHAT. The code shows WHAT it does.

```python
# Good
# Exclude past dates when fetching upcoming events
events = Event.objects.filter(date__gte=timezone.now())

# Bad
# Get events
events = Event.objects.filter(date__gte=timezone.now())
```

### Comment Style

```python
# For single line comments
# Use # with space

"""
For multi-line comments or docstrings,
use triple quotes with proper indentation.
"""
```

## Git Commit Messages

```
[FEATURE] Add destination search functionality

This commit adds a search form that allows users to filter
destinations by name and description. The search uses
case-insensitive matching for better UX.

- Add DestinationFilterForm
- Add search_destinations service function
- Update DestinationListView to handle filtering
- Add search_destinations tests

Closes #123
```

### Commit Types

- `[FEATURE]` - New feature
- `[BUGFIX]` - Bug fix
- `[REFACTOR]` - Code refactoring
- `[DOCS]` - Documentation
- `[STYLE]` - Code style changes
- `[TEST]` - Test updates
- `[PERF]` - Performance improvements

## Linting & Formatting

### Black Formatter

```bash
black .
```

### Flake8 Linter

```bash
flake8 .
```

### isort

```bash
isort .
```

### All Together

```bash
black . && isort . && flake8 .
```

## Code Review Checklist

- [ ] Follows PEP 8 and project style guide
- [ ] Has appropriate docstrings
- [ ] Includes tests
- [ ] No hardcoded values
- [ ] Proper error handling
- [ ] Database queries optimized
- [ ] No security vulnerabilities
- [ ] No duplicate code
- [ ] Commit messages are clear

---

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

