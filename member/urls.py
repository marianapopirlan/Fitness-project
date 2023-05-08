from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:cnp>/", views.member_details, name="detail"),
    path("<int:cnp>/remove/", views.member_remove, name="remove"),
]