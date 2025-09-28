from django.urls import path
from . import views

urlpatterns = [
    path('smallOrganisations/', views.smallWareHouse, name='smallWareHouse'),
    path('middleOrganisations/', views.middleWareHouse, name='middleWareHouse'),
]
    