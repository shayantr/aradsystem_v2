from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from ecommerce_products.models import Product


class OrderClass(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(blank=True, null=True)
    is_payed = models.BooleanField(default=False)

class OrderDetailClass(models.Model):
    order_id = models.ForeignKey(OrderClass, on_delete=models.CASCADE, related_name='orderid')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    count = models.IntegerField()


