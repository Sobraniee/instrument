from rest_framework import serializers
from core.models import OrderProduct, Order


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ['tool', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['number_order', 'buyer_name', 'buyer_phone', 'delivery', 'delivery_address', 'products']
