from django.db import models
from core.models.tools import Tools


class Photo(models.Model):
    image = models.ImageField(upload_to='your')
    tool = models.ForeignKey(Tools, on_delete=models.CASCADE, related_name='photos')

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return str(self.tool)