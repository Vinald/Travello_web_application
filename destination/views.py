from django.shortcuts import render
from  .models import Destination
# Create your views here.
def index(request):
    destination = Destination.objects.all()
    
    return render(request, 'index.html', {'destination': destination})