from django.db import models

class Tools(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Категории', on_delete=models.CASCADE)
    brand = models.ForeignKey('Бренд', on_delete=models.CASCADE)
    photos = models.ManyToManyField('Фото')

class Meta:
    verbose_name = "Инструмент"
    verbose_name_plural = "Инструмент"
