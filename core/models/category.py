from django.db import models
from .subcategory import Subcategory


class Category(models.Model):
    name = models.CharField(max_length=255)
    sub_name = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name