from django.db import models


class Order(models.Model):
    number_order = models.PositiveIntegerField(unique=True)
    buyer_name = models.CharField(max_length=255)
    buyer_phone = models.CharField(max_length=15)
    delivery = models.BooleanField()
    delivery_address = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products')
    tool = models.ForeignKey('Tools', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Продукт заказа"
        verbose_name_plural = "Продукты заказа"

