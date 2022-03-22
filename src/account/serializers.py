from attr import field
from rest_framework import serializers

from .models import AuthUser
        
        
class UserSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(read_only=True)
    
    class Meta:
        model = AuthUser
        fields = ("id", "username", "display_status", "profile_image",)
    