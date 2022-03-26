from django.urls import path

from . import views


urlpatterns = [
    path("<int:pk>/", views.FollowView.as_view()),
    path("following/", views.UserFollowingViewSet.as_view()),
    path("followers/", views.UserFollowersViewSet.as_view()),
]
