from django.urls import path
from .views import *

urlpatterns = [
    path('category/', CategoryView.as_view(), name='category_list'),

    path('brands/', BrandListCreateView.as_view(), name='brand-list-create'),
    path('brands/<int:pk>/', BrandRetrieveUpdateDestroyView.as_view(), name='brand-retrieve-update-destroy'),

    path('tools/', ToolsdListCreateView.as_view(), name='tools-list-create'),
    path('tools/<int:pk>/', ToolsRetrieveUpdateDestroyView.as_view(), name='tools-retrieve-update-destroy'),
]
