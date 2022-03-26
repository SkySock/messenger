from rest_framework import serializers
from src.account.serializers import UserBaseSerializer
from .models import UserFollowing


class UserFollowingSerializer(serializers.ModelSerializer):
    following_user = UserBaseSerializer(read_only=True)
    
    class Meta:
        model = UserFollowing
        fields = ('id', 'following_user', 'created')


class UserFollowersSerializer(serializers.ModelSerializer):
    user = UserBaseSerializer(read_only=True)
    
    class Meta:
        model = UserFollowing
        fields = ('id', 'user', 'created')
