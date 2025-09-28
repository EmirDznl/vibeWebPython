from django.urls import path
from . import views

urlpatterns = [
    path("", views.approved_surveys_view, name="approved_surveys"),
    path("survey/", views.survey_view, name="surveys"),
    path("success/", views.survey_success_view, name="survey_success"),
]
