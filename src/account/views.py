from django.http import Http404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from src.base.permissions import IsCurrentUserOrReadOnly
from rest_framework import generics, viewsets

from .models import AuthUser
from .serializers import UserBaseSerializer, UserDetailSerializer, UserProfileImageSerializer
from .services import PaginationUsers


class UserListView(generics.ListAPIView):
    """
    A list of users
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = UserBaseSerializer
    pagination_class = PaginationUsers
    queryset = AuthUser.objects.all()


class UserDetailView(viewsets.ModelViewSet):
    """
    User detail by id
    """
    permission_classes = (IsCurrentUserOrReadOnly,)
    serializer_class = UserDetailSerializer

    def get_queryset(self):
        return AuthUser.objects.all()


class UserDetailViewByUsername(viewsets.ModelViewSet):
    """
    User detail by username
    """
    permission_classes = (IsCurrentUserOrReadOnly,)
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

    def get_queryset(self):
        return AuthUser.objects.all()


class CurrentUserDetailView(generics.RetrieveAPIView):
    """
    Current authorized user detail
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = UserDetailSerializer

    def get_object(self):
        obj = self.request.user
        self.check_object_permissions(self.request, obj)
        return obj


class UpdateUserPhotoView(generics.UpdateAPIView):
    """
    Update profile image
    """
    permission_classes = (IsCurrentUserOrReadOnly,)
    serializer_class = UserProfileImageSerializer

    def get_object(self):
        obj = self.request.user
        self.check_object_permissions(self.request, obj)
        return obj
