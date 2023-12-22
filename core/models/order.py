from django.db import models
from .tools import Tools


class Order(models.Model):
    number_order = models.PositiveIntegerField(unique=True)
    buyer_name = models.CharField(max_length=255)
    buyer_phone = models.CharField(max_length=15)
    delivery = models.BooleanField()
    delivery_address = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def save(self, *args, **kwargs):
        if not self.number_order:
            max_number_order = Order.objects.aggregate(models.Max('number_order'))['number_order__max'] or 0
            self.number_order = max_number_order + 1
            self.number_order = f"{self.number_order:06d}"
        super().save(*args, **kwargs)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products')
    tool = models.ForeignKey(Tools, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Продукт заказа"
        verbose_name_plural = "Продукты заказа"

