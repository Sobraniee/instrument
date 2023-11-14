from django.urls import path
from .views import ToolsView, CategoryView, BrandView

urlpatterns = [
    path('tools/', ToolsView.as_view(), name='tools_list'),
    path('category/', CategoryView.as_view(), name='category_list'),
    path('brands/', BrandView.as_view(), name='brand_list'),

]
