from django.urls import path
from . import views

urlpatterns = [
    path('crm', views.crm, name='crm'),
    path('eAgreement/', views.eAgreement, name='eAgreement'),
    path('eBill/', views.eBill, name='eBill'),
    path('eBook/', views.eBook, name='eBook'),
]
