from django.http import Http404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from src.base.permissions import IsCurrentUserOrReadOnly
from rest_framework import generics, viewsets

from .models import AuthUser
from .serializers import UserBaseSerializer, UserDetailSerializer
from .services import PaginationUsers


class UserListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = AuthUser.objects.all()
    serializer_class = UserBaseSerializer
    pagination_class = PaginationUsers
    

class UserDetailView(viewsets.ModelViewSet):
    serializer_class = UserDetailSerializer
    permission_classes = (IsCurrentUserOrReadOnly,)

    def get_queryset(self):
        return AuthUser.objects.all()


class UserDetailViewOfUsername(viewsets.ModelViewSet):
    serializer_class = UserDetailSerializer
    permission_classes = (IsCurrentUserOrReadOnly,)
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
