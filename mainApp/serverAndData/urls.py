from django.urls import path
from . import views

urlpatterns = [
    
    path('cloud/', views.cloud, name='cloud'),
    path('database-maintenance/', views.databaseMaintenance, name='databaseMaintenance'),
]
    