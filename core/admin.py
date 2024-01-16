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


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'number_order',
        'buyer_name', 
        'buyer_phone', 
        'delivery',
        'delivery_address',
        

    ]

@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = [
        'order', 
        'tool',
        'quantity', 
        

    ]    