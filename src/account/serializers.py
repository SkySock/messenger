from attr import field
from rest_framework import serializers

from .models import AuthUser
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ("id", "username", "display_status", "profile_image",)
    