from django.urls import path
from . import views

urlpatterns = [
    path('desktop-development/', views.desktopAppDev, name='desktopAppDev'),
    path('web-development/', views.webAppDev, name='webAppDev'),
    path('mobile-development/', views.mobileAppDev, name='mobileAppDev'),
    path('api-development/', views.apiDevelopment, name='apiDevelopment'),
]
