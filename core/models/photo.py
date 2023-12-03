from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to='photos')
    tool = models.ForeignKey('Tools', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return str(self.tool)