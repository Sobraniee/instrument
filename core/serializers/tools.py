from rest_framework import serializers
from core.models import Tools
from .photo import PhotoSerializer
# from core.models import Tools
# from core.serializers import PhotoSerializer


class ToolsSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Tools
        fields = '__all__'
