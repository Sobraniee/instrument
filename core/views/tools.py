from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from core.models import Tools
from core.serializers import ToolsSerializer, PhotoSerializer

class ToolsListCreateView(generics.ListCreateAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'brand', 'subcategory']
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        data = request.data
        photos_data = data.pop('photos', [])  # Получаем данные о фотографиях

        # Создаем инструмент без фотографий
        tools_serializer = self.get_serializer(data=data)
        tools_serializer.is_valid(raise_exception=True)
        tools_instance = tools_serializer.save()

        # Затем добавляем фотографии к созданному инструменту
        for photo_data in photos_data:
            photo_data['tool'] = tools_instance.id
            photo_serializer = PhotoSerializer(data=photo_data)
            if photo_serializer.is_valid():
                photo_serializer.save()
            else:
                # Обработка ошибок, если фотография не сохранена
                pass

        headers = self.get_success_headers(tools_serializer.data)
        return Response(tools_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ToolsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer
    pagination_class = PageNumberPagination
