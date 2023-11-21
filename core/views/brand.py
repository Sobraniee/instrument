from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.views import View
from core.models import Brand


class BrandView(View):
    def get(self, request, *args, **kwargs):
        brand = Brand.objects.all()
        return render(request, {"brand": brand})


class BrandListAPIView(APIView):
    def get(self, request):
        brands = Brand.objects.all()
        serializer = Brand(brands, many=True)
        return Response(serializer.data)


class BrandDetailAPIView(APIView):
    def get(self, request, pk):
        brand = Brand.objects.get(pk=pk)
        serializer = Brand(brand)
        return Response(serializer.data)
