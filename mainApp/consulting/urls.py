from django.urls import path
from . import views 

urlpatterns = [
    path('digiTransf/', views.digiTransf, name='digiTransf'),
    path('requirementsAnalysis/', views.requirementsAnalysis, name='requirementsAnalysis'),
    path('swTraining/', views.swTraining, name='swTraining'),
    path('workflowConsulting/', views.workflowConsulting, name='workflowConsulting'),
]