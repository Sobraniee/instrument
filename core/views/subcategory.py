from rest_framework import generics
from core.models import Subcategory
from core.serializers import SubcategorySerializer


class SubcategoryListCreateView(generics.ListCreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class SubcategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer