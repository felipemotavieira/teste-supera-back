from rest_framework import serializers
from .models import Order
from .models import OrdersRelation
from products.serializers import ProductSerializer
from products.models import Product
from users.serializers import UserSerializer
import ipdb

class OrderSerializer(serializers.Serializer):
    order_products = ProductSerializer(many=True)
    buyer = UserSerializer(read_only=True)
    id = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        products = validated_data.pop('order_products')

        order = Order.objects.create(**validated_data)

        unique_prods = []
        for prod in products:
            if prod not in unique_prods:
                unique_prods.append(prod)

            prod_obj = Product.objects.get(**prod)

            order.order_products.add(prod_obj)

        for unique_prod in unique_prods:
            counter = 0
            for prod in products:

                if unique_prod == prod:
                    counter += 1

            unique_prod['counter'] = counter       

        order_relation = OrdersRelation.objects.filter(order=order.id)

        for prod_per_order in order_relation:
            for unique_prod in unique_prods:
                if prod_per_order.product.name == unique_prod['name']:
                    prod_per_order.quantity = unique_prod['counter']

            prod_per_order.save()

        ipdb.set_trace()

        return order
