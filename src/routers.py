from django.urls import path, include


urlpatterns = [
    path('follow/', include('src.followers.urls')),
    path('', include('src.account.urls')),
]