from django.urls import path
from . import views


urlpatterns = [
    path("", views.IndexPage.as_view, name="index"),
    path("<int:blog_id>/", views.DetailsPage.as_view, name="details"),
    path("fise-de-lucru/", views.WorksheetPage.as_view, name="fise-de-lucru"),
    path("exercitii/", views.ExercisesPage.as_view, name="exercitii"),
    path("download-attachment/<int:post_id>", views.download_attachment, name="download-attachment"),
]