from django.db import models


class Subcategory(models.Model):
    name = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name