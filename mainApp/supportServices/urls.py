from django.urls import path
from . import views 

urlpatterns = [
    path('on-site-support/', views.onSiteSupport, name='onSiteSupport'),
    path('remote-support/', views.remoteSupport, name='remoteSupport'),
]
