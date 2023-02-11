from rest_framework import serializers
from .models import Order
from products.serializers import ProductSerializer
from products.models import Product
import ipdb

class OrderSerializer(serializers.Serializer):
    order_products = ProductSerializer(many=True)

    def create(self, validated_data):
        products = validated_data.pop('order_products')

        order = Order.objects.create(**validated_data)

        for prod in products:
            prod_obj = Product.objects.get(**prod)
            
            order.order_products.add(prod_obj)
            
        return order
