from django.shortcuts import render
from django.views import View
from core.models import Tools

class ToolsView(View):
    template_name = 'tools_list.html'

    def get(self, request, *args, **kwargs):
        tools = Tools.objects.all()
        return render(request, self.template_name, {'tools': tools})
