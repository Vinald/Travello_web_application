from django.shortcuts import render
from  .models import Destination, NewsPosts, Testimonial, HomeSlider

# Create your views here.
def index(request):
    destination = Destination.objects.all()
    news_posts = NewsPosts.objects.all()
    testimonials = Testimonial.objects.all()
    sliders = HomeSlider.objects.all()

    return render(request, 'index.html', {'destination': destination, 'news_posts': news_posts, 'testimonials': testimonials, 'sliders': sliders})