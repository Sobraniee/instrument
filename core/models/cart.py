from django.db import models
from core.models import Tools


class Cart(models.Model):
    tool = models.ForeignKey(Tools, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    buyer_name = models.CharField(max_length=250)
    buyer_phone = models.CharField(max_length=250)
    delivery = models.BooleanField(default=False)
    delivery_adress = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Корзина покупок"
        verbose_name_plural = "Корзины покупок"
