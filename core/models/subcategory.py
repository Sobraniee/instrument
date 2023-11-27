from django.db import models


class Subcategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name