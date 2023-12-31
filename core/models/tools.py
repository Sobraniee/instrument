from django.db import models
from .brand import Brand
from .category import Category
from cloudinary.models import CloudinaryField


class Tools(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    photo = CloudinaryField('photo', null=True, blank=True)
    favorites = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Инструмент"
        verbose_name_plural = "Инструменты"

    def __str__(self):
        return self.name