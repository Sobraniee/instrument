from django.urls import path
from .views import ToolsView

urlpatterns = [
    path('tools/', ToolsView.as_view(), name='tools_list'),
]
