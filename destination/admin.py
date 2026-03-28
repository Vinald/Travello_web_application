"""
Admin configuration for the destination app.
"""

from django.contrib import admin
from django.utils.html import format_html
from .models import Destination, Testimonial, NewsPosts, HomeSlider


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    """Admin interface for Destination model."""
    list_display = ['name', 'price', 'offer_badge', 'created_at']
    list_filter = ['offer', 'created_at', 'price']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
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

    def offer_badge(self, obj):
        """Display offer status with colored badge."""
        if obj.offer:
            return format_html(
                '<span style="background-color: #28a745; color: white; padding: 5px 10px; border-radius: 3px;">On Offer</span>'
            )
        return format_html(
            '<span style="background-color: #6c757d; color: white; padding: 5px 10px; border-radius: 3px;">Regular</span>'
        )
    offer_badge.short_description = 'Offer Status'

    actions = ['mark_as_offer', 'remove_from_offer']

    def mark_as_offer(self, request, queryset):
        """Mark selected destinations as on offer."""
        updated = queryset.update(offer=True)
        self.message_user(request, f'{updated} destination(s) marked as on offer.')
    mark_as_offer.short_description = 'Mark selected as on offer'

    def remove_from_offer(self, request, queryset):
        """Remove selected destinations from offer."""
        updated = queryset.update(offer=False)
        self.message_user(request, f'{updated} destination(s) removed from offer.')
    remove_from_offer.short_description = 'Remove selected from offer'


@admin.register(NewsPosts)
class NewsPostsAdmin(admin.ModelAdmin):
    """Admin interface for NewsPosts model."""
    list_display = ['title', 'category', 'publication_date', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['title', 'category', 'content']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Article Information', {
            'fields': ('title', 'category', 'content')
        }),
        ('Publication', {
            'fields': ('date', 'month', 'image')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def publication_date(self, obj):
        """Display formatted publication date."""
        return f"{obj.month} {obj.date}"
    publication_date.short_description = 'Publication Date'


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """Admin interface for Testimonial model."""
    list_display = ['author', 'position', 'created_at']
    list_filter = ['created_at']
    search_fields = ['author', 'position', 'content']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Testimonial Information', {
            'fields': ('author', 'position', 'content')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    """Admin interface for HomeSlider model."""
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Slider Information', {
            'fields': ('title', 'image')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
