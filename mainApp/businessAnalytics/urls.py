from django.urls import path
from . import views

urlpatterns = [
    path('budgetManagement/', views.budget_management, name='budget_management'),
    path('dataReport/', views.data_report, name='data_report'),
    path('liveDashboard/', views.live_dashboard, name='live_dashboard'),
]