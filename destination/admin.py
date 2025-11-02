from django.contrib import admin
from .models import Destination, Testimonial, NewsPosts, HomeSlider


# Register your models here.
class DestinationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "description", "offer")


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "position", "content")


class NewsPostsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date", "month", "category", "content")

class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image")

admin.site.register(Destination, DestinationAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(NewsPosts, NewsPostsAdmin)
admin.site.register(HomeSlider, HomeSliderAdmin)
