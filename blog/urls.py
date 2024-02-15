from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexPage.as_view, name="index"),
    path("fise-de-lucru/", views.WorksheetPage.as_view, name="fise-de-lucru"),
    path("exercitii/", views.ExercisesPage.as_view, name="exercitii"),
]