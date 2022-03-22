from rest_framework import serializers
from src.account.serializers import UserSerializer
from .models import UserFollowing


class UserFollowingSerializer(serializers.ModelSerializer):
    following_user = UserSerializer(read_only=True)
    
    class Meta:
        model = UserFollowing
        fields = ('id', 'following_user', 'created')


class UserFollowersSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = UserFollowing
        fields = ('id', 'user', 'created')
