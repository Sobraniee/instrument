from django.db import models
import json

class Category(models.Model):
    name = models.CharField(max_length=255)
    sub_name = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_sub_name_as_dict(self):
        return json.loads(self.sub_name) if self.sub_name else {}

    def set_sub_name_from_dict(self, sub_name_dict):
        self.sub_name = json.dumps(sub_name_dict)
    
    def __str__(self):
        return self.name