"""
Views for the services app.
"""

from django.shortcuts import render
from django.views import View


class ServicesView(View):
    """
    Services page view.
    Displays available travel services.
    """
    template_name = 'news.html'

    def get(self, request):
        """Display services page."""
        context = {
            'services_title': 'Our Services',
            'services_description': 'Explore the wide range of services we offer'
        }
        return render(request, self.template_name, context)


def services(request):
    """Functional view for services (delegates to ServicesView)."""
    view = ServicesView.as_view()
    return view(request)
