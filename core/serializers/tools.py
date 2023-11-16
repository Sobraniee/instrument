from rest_framework import serializers
from core.models import Tools


class ToolsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tools
        fields = '__all__'