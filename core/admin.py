from django.contrib import admin
from core.models import *

admin.site.register(Category)
admin.site.register(Brand)


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