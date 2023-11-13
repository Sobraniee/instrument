from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

    def __str__(self):
        return self.image