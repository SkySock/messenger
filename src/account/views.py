from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import generics

from .models import AuthUser
from .serializers import UserSerializer
from .services import PaginationUsers


class UserListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = AuthUser.objects.all()
    serializer_class = UserSerializer
    pagination_class = PaginationUsers
    

class UserDetailView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, username):
        users = AuthUser.objects.get(username=username)
        serializer = UserSerializer(users)
        return Response(serializer.data)
