from rest_framework import serializers
from src.followers.models import UserFollowing
from .models import AuthUser


class UserDetailSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(read_only=True)

    class Meta:
        model = AuthUser
        fields = (
            'id',
            'username',
            'profile_image',
            'bio',
            'display_status',
        )

        
class UserBaseSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(read_only=True)
    is_followed = serializers.SerializerMethodField('get_is_followed')
    
    class Meta:
        model = AuthUser
        fields = ('id', 'username', 'display_status', 'profile_image', 'is_followed')

    def get_is_followed(self, obj):
        request = self.context.get('request')
        if not request:
            return None
        try:
            UserFollowing.objects.get(user=request.user, following_user=obj)
        except UserFollowing.DoesNotExist:
            return False
        return True
    