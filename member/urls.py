from django.urls import path

from .import views

urlpatterns = [
    path("", views.index, name="member_index"),
    path("<int:cnp>/", views.member_details, name="detail"),
    path("<int:cnp>/remove/", views.member_remove, name="remove"),
    path("create/", views.MemberCreateView.as_view(), name='create-class')
]