from django.urls import path
from . import views



urlpatterns = [ 
    path("small-business/", views.small, name="small"),
    path("mid-market/", views.middle, name="middle"),
    path("enterprise/", views.enterprise, name="enterprise"),
]

