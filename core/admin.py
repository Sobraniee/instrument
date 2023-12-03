from django.contrib import admin
from core.models import *

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Photo)


@admin.register(Tools)
class ToolsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'description',
        'price',
        'subcategory',
        'category',
        'brand',
    ]


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = [
        'category_id',
        'name',


    ]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [
        'tool',
        'quantity', 
        'buyer_name', 
        'buyer_phone', 
        'created_at',


    ]