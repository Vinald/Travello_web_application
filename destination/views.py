"""
Views for the destination app.
"""

import logging
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Destination, NewsPosts, Testimonial, HomeSlider

logger = logging.getLogger(__name__)


class IndexView(View):
    """
    Home page view displaying destinations, news, testimonials, and sliders.
    """
    template_name = 'index.html'
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        """
        GET request handler for home page.
        Retrieves and displays all content with optimized queries.
        """
        try:
            # Use select_related and prefetch_related for query optimization
            destinations = Destination.objects.all().order_by('-created_at')
            news_posts = NewsPosts.objects.all().order_by('-created_at')[:6]
            testimonials = Testimonial.objects.all().order_by('-created_at')
            sliders = HomeSlider.objects.all().order_by('-created_at')

            # Paginate destinations
            paginator = Paginator(destinations, self.paginate_by)
            page = request.GET.get('page')

            try:
                destinations_page = paginator.page(page)
            except PageNotAnInteger:
                destinations_page = paginator.page(1)
            except EmptyPage:
                destinations_page = paginator.page(paginator.num_pages)

            context = {
                'destination': destinations_page,
                'news_posts': news_posts,
                'testimonials': testimonials,
                'sliders': sliders,
            }

            return render(request, self.template_name, context)

        except Exception as e:
            logger.error(f"Error rendering index page: {str(e)}")
            context = {
                'error': 'Unable to load content. Please try again later.'
            }
            return render(request, self.template_name, context, status=500)


class DestinationListView(ListView):
    """
    List view for all destinations.
    """
    model = Destination
    template_name = 'destination_list.html'
    context_object_name = 'destinations'
    paginate_by = 12

    def get_queryset(self):
        """
        Get optimized queryset with filtering by offer status.
        """
        queryset = Destination.objects.all().order_by('-created_at')

        # Filter by offer if provided
        offer_filter = self.request.GET.get('offer')
        if offer_filter == 'true':
            queryset = queryset.filter(offer=True)

        return queryset

    def get_context_data(self, **kwargs):
        """Add additional context data."""
        context = super().get_context_data(**kwargs)
        context['total_count'] = self.get_queryset().count()
        return context


class DestinationDetailView(DetailView):
    """
    Detail view for a single destination.
    """
    model = Destination
    template_name = 'destination_detail.html'
    context_object_name = 'destination'
    slug_field = 'id'
    slug_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        """Add related destinations to context."""
        context = super().get_context_data(**kwargs)
        # Get related destinations (same price range)
        current_obj = self.get_object()
        context['related'] = Destination.objects.filter(
            price__range=[current_obj.price * 0.8, current_obj.price * 1.2]
        ).exclude(pk=current_obj.pk)[:4]
        return context


def index(request):
    """
    Functional view for home page (kept for backward compatibility).
    Delegates to IndexView.
    """
    view = IndexView.as_view()
    return view(request)
