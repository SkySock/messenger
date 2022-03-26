from django.urls import path

from . import views


urlpatterns = [
    path("users/", views.UserListView.as_view()),
    path("profile/", views.CurrentUserDetailView.as_view()),
    path("profile/id<int:pk>/", views.UserDetailView.as_view({
        'get': 'retrieve',
        'put': 'partial_update',
        'delete': 'destroy',
    })),
    path("profile/<str:username>/", views.UserDetailViewOfUsername.as_view({
        'get': 'retrieve',
        'put': 'partial_update',
        'delete': 'destroy',
    })),
]