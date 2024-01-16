from rest_framework import generics
from core.models import Tools
from core.serializers import ToolsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from cloudinary.uploader import upload
from rest_framework import status
from rest_framework.response import Response


class ToolsListCreateView(generics.ListCreateAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'brand', 'subcategory']
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        photos = self.request.data.getlist('photos')
        photos_dict = {}

        for i, photo in enumerate(photos):
            try:
                response = upload(photo)
                photos_dict[f"photo_{i+1}"] = response['secure_url']
            except Exception as e:
                error_message = f"Ошибка при загрузке изображения: {str(e)}"
                return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(photos=photos_dict)

    def get_object(self, pk):
        obj = super().get_object(pk)
        photos_dict = {f"photo_{i+1}": photo_url for i, photo_url in enumerate(obj.photos)}
        obj.photos = photos_dict
        return obj


class ToolsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer
    pagination_class = PageNumberPagination

