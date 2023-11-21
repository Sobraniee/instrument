from rest_framework import generics
from core.models import Tools
from core.serializers import ToolsSerializer


class ToolsdListCreateView(generics.ListCreateAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer


class ToolsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tools.objects.all()
    serializer_class = ToolsSerializer