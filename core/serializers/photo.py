from rest_framework import serializers
from core.models import Photo


class PhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'