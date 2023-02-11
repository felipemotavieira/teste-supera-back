from django.db import models
import uuid

# Create your models here.
class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    buyer = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="buyer",
    )

    order_products = models.ManyToManyField(
        "products.Product",
        related_name="order_products",
    )
