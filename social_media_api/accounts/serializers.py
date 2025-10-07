from rest_framework import serializers 
from .models import CustomUser

class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser 
        fields = ['id','bio','profile_picture','followers','created_at']
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']     
