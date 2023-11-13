from django.shortcuts import render
from django.views import View
from core.models import Tools


class ToolsView(View):
    def get(self, request, *args, **kwargs):
        tools = Tools.objects.all()
        return render(request, {'tools': tools})
