from django.db import models
from .category import Category


class Subcategory(models.Model):
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.JSONField(blank=True, null=True)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name