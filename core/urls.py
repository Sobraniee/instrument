from django.urls import path
from .views import *

urlpatterns = [
    path('tools/', ToolsView.as_view(), name='tools_list'),
    path('category/', CategoryView.as_view(), name='category_list'),
    path('brands/', BrandListCreateView.as_view(), name='brand-list-create'),
    path('brands/<int:pk>/', BrandRetrieveUpdateDestroyView.as_view(), name='brand-retrieve-update-destroy'),

]
