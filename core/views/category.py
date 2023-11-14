from django.shortcuts import render
from django.views import View
from core.models import Category


class CategoryView(View):
    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        return render(request, {'category': category})