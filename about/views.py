"""
Views for the about app.
"""

from django.shortcuts import render
from django.views import View


class AboutView(View):
    """
    About page view.
    Displays company information and team details.
    """
    template_name = 'about/about.html'

    def get(self, request):
        """Display about page."""
        context = {
            'page_title': 'About Us',
            'page_description': 'Learn more about our company and mission'
        }
        return render(request, self.template_name, context)


def about(request):
    """Functional view for about page (delegates to AboutView)."""
    view = AboutView.as_view()
    return view(request)
