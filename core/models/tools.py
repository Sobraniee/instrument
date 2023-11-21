from django.db import models
from .brand import Brand
from .category import Category
from .photo import Photo


class Tools(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    photos = models.ManyToManyField('Photo')
    favorites = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Инструмент"
        verbose_name_plural = "Инструменты"
