from django.urls import path
from . import views

urlpatterns = [
    path('',  views.home, name='homePage'),
    path('about', views.about, name='about'),
]