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
        'type',
        'price',
        'category',
        'brand',
    ]

