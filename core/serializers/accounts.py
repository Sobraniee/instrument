from rest_framework import serializers
from core.models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', 'is_active', 'is_staff', 'is_employee')

