from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-retrieve-update-destroy'),

    path('brands/', BrandListCreateView.as_view(), name='brand-list-create'),
    path('brands/<int:pk>/', BrandRetrieveUpdateDestroyView.as_view(), name='brand-retrieve-update-destroy'),

    path('tools/', ToolsListCreateView.as_view(), name='tools-list-create'),
    path('tools/<int:pk>/', ToolsRetrieveUpdateDestroyView.as_view(), name='tools-retrieve-update-destroy'),

    path('subcategories/', SubcategoryListCreateView.as_view(), name='subcategories-list-create'),
    path('subcategories/<int:pk>/', SubcategoryRetrieveUpdateDestroyView.as_view(), name='subcategories-retrieve-update-destroy'),

    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
    path('order-products/<int:pk>/', OrderProductRetrieveUpdateDestroyView.as_view(), name='order-product-detail'),

    path('api/photos/', PhotoListCreateView.as_view(), name='photos-list'),
    path('api/photos/<int:pk>/', PhotoRetrieveUpdateDestroyView.as_view(), name='photos-retrieve-update-destroy'),
]
