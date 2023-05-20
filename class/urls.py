from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="class_index"),
    path("<int:id>/", views.class_details, name="detail"),
    path("<int:id>/remove/", views.class_remove, name="remove"),
    path("create/", views.ClassCreateView.as_view(), name='create-class')
]