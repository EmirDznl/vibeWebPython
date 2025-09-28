from django.urls import path
from . import views

urlpatterns = [
    path('hrManagement/', views.hr_view, name='hrManagement'),
    path('payroll/', views.payroll_view, name='payroll'),
]
