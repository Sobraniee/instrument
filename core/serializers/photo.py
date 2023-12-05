from rest_framework import serializers
from ..models import Tools, Photo
from core.models import Tools, Photo
# from core.models import Photo
# from core.models import Tools

class PhotoSerializer(serializers.ModelSerializer):
    tool = serializers.PrimaryKeyRelatedField(queryset=Tools.objects.all())

    class Meta:
        model = Photo
        fields = ('id', 'image', 'tool')