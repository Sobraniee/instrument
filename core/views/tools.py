from rest_framework import generics
from core.models import Tools
from core.serializers import ToolsSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ToolsListCreateView(generics.ListCreateAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'brand']


class ToolsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer