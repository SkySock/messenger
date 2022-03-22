from django.shortcuts import render
from rest_framework import views, generics, permissions, response
from src import followers
from src.account.models import AuthUser
from .models import UserFollowing
from .serializers import UserFollowingSerializer, UserFollowersSerializer


class UserFollowingViewSet(generics.ListAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserFollowingSerializer
    def get_queryset(self):
        return UserFollowing.objects.filter(user=self.request.user)
    
    
class UserFollowersViewSet(generics.ListAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserFollowersSerializer
    def get_queryset(self):
        return UserFollowing.objects.filter(following_user=self.request.user)
    

class FollowView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, pk):
        try:
            UserFollowing.objects.get(user=request.user, following_user=pk)
        except UserFollowing.DoesNotExist:
            return response.Response(False)
        return response.Response(True)

    def post(self, request, pk):
        try:
            user = AuthUser.objects.get(id=pk)
        except UserFollowing.DoesNotExist:
            return response.Response(status=404)
        UserFollowing.objects.create(user=request.user, following_user=user)
        return response.Response(status=201)

    def delete(self, request, pk):
        try:
            follow = UserFollowing.objects.get(user=request.user, following_user=pk)
        except UserFollowing.DoesNotExist:
            return response.Response(status=404)
        follow.delete()
        return response.Response(status=204)
