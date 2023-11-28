from rest_framework import generics
from core.models import Tools
from core.serializers import ToolsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


class ToolsListCreateView(generics.ListCreateAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'brand', 'subcategory']
    pagination_class = PageNumberPagination


class ToolsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer
    pagination_class = PageNumberPagination