from django.urls import path
from . import views 

urlpatterns = [
    path('erp-management/', views.erp_management, name='erpManagement'),
    path('integration-management/', views.integration_management, name='integrationManagement'),
    path('sw-management/', views.sw_management, name='swManagement'),
]
