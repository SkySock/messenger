from django.http import Http404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from src.base.permissions import IsCurrentUserOrReadOnly
from rest_framework import generics, viewsets

from .models import AuthUser
from .serializers import UserBaseSerializer, UserDetailSerializer, UserProfileImageSerializer
from .services import PaginationUsers


class UserListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserBaseSerializer
    pagination_class = PaginationUsers
    queryset = AuthUser.objects.all()


class UserDetailView(viewsets.ModelViewSet):
    permission_classes = (IsCurrentUserOrReadOnly,)
    serializer_class = UserDetailSerializer

    def get_queryset(self):
        return AuthUser.objects.all()


class UserDetailViewOfUsername(viewsets.ModelViewSet):
    permission_classes = (IsCurrentUserOrReadOnly,)
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

    def get_queryset(self):
        return AuthUser.objects.all()


class CurrentUserDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserDetailSerializer

    def get_object(self):
        try:
            obj = AuthUser.objects.get(id=self.request.user.id)
        except AuthUser.DoesNotExist:
            raise Http404()
        self.check_object_permissions(self.request, obj)
        return obj


class UpdateUserPhotoView(generics.UpdateAPIView):
    permission_classes = (IsCurrentUserOrReadOnly,)
    serializer_class = UserProfileImageSerializer

    def get_object(self):
        try:
            obj = AuthUser.objects.get(id=self.request.user.id)
        except AuthUser.DoesNotExist:
            raise Http404()
        self.check_object_permissions(self.request, obj)
        return obj
