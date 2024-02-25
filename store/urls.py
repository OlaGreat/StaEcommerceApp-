from django.urls import path
from . import views

urlpatterns = [
    path('',  views.home, name='homePage'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
]