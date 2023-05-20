from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="trainer_index"),
    path("<int:cnp>/", views.trainer_details, name="detail"),
    path("<int:cnp>/remove/", views.trainer_remove, name="remove"),
    path("create/", views.TrainerCreateView.as_view(), name='create-trainer')
]