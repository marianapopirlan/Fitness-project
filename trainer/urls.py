from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<int:cnp>/", views.trainer_details, name="detail"),
    path("<int:cnp>/remove/", views.trainer_remove, name="remove"),
]