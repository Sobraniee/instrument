from rest_framework import serializers
from core.models import Tools, Photo


class ToolsSerializer(serializers.ModelSerializer):
    photos = serializers.ListField(child=serializers.URLField(), required=False)

    class Meta:
        model = Tools
        fields = '__all__'

    def create(self, validated_data):
        photos_data = validated_data.pop('photos', [])
        tool = Tools.objects.create(**validated_data)

        for photo_url in photos_data:
            Photo.objects.create(tool=tool, url=photo_url)

        return tool