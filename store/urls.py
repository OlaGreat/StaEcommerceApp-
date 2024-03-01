from django.urls import path
from . import views

urlpatterns = [
    path('',  views.home, name='homePage'),
    path('about/', views.about, name='about'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('category/<str:queryCategory>', views.category, name='category'),
    path('product/<int:productPk>', views.viewProduct, name='viewProduct'),
    path('cart/',views.cart, name='cart'),
]