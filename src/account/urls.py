from django.urls import path

from . import views


urlpatterns = [
    path("users/", views.UserListView.as_view()),
    path("user/<str:username>/", views.UserDetailView.as_view()),
]