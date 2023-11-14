from django.shortcuts import render
from django.views import View
from core.models import Brand


class BrandView(View):
    def get(self, request, *args, **kwargs):
        brand = Brand.objects.all()
        return render(request, {'brand': brand})