import django.db
from rest_framework import views, generics, permissions, response
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
            AuthUser.objects.get(id=pk)
        except AuthUser.DoesNotExist:
            return response.Response({'error': 'User does not exist'}, status=404)

        try:
            UserFollowing.objects.get(user=request.user, following_user=pk)
        except UserFollowing.DoesNotExist:
            return response.Response(False)
        return response.Response(True)

    def post(self, request, pk):
        try:
            user = AuthUser.objects.get(id=pk)
            UserFollowing.objects.create(user=request.user, following_user=user)
        except AuthUser.DoesNotExist:
            return response.Response(status=404)
        except django.db.IntegrityError:
            return response.Response(True, status=200)

        return response.Response(True, status=201)

    def delete(self, request, pk):
        try:
            follow = UserFollowing.objects.get(
                user=request.user,
                following_user=pk
            )
        except UserFollowing.DoesNotExist:
            return response.Response(status=404)
        follow.delete()
        return response.Response(False, status=204)
