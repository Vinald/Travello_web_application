"""
Views for the contact app.
Handles contact form submissions.
"""

import logging
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.http import JsonResponse
from .forms import ContactForm
from .models import Contact
from core.decorators import get_client_ip

logger = logging.getLogger(__name__)


class ContactView(View):
    """
    Contact form view.
    Handles both GET (display form) and POST (process submission) requests.
    """
    template_name = 'contact.html'
    form_class = ContactForm

    def get(self, request):
        """Display contact form."""
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """Process contact form submission."""
        form = self.form_class(request.POST)

        if form.is_valid():
            try:
                contact = form.save(commit=False)
                contact.ip_address = get_client_ip(request)
                contact.save()

                logger.info(f"New contact submission from {contact.email}")
                messages.success(
                    request,
                    'Thank you for contacting us! We will get back to you soon.'
                )

                # Return JSON response for AJAX requests
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': True, 'message': 'Message sent successfully!'})

                return redirect('contact')
            except Exception as e:
                logger.error(f"Error saving contact submission: {str(e)}")
                messages.error(request, 'An error occurred. Please try again later.')
        else:
            # Add form errors to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

        # Return JSON response for AJAX requests
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'errors': form.errors
            }, status=400)

        return render(request, self.template_name, {'form': form})


# Functional view for backward compatibility
def contact(request):
    """Functional view for contact (delegates to ContactView)."""
    view = ContactView.as_view()
    return view(request)
