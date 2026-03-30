from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('destinations/', views.DestinationListView.as_view(), name='destinations'),
]