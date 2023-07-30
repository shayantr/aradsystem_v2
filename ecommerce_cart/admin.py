from django.contrib import admin

# Register your models here.
from ecommerce_cart.models import OrderClass, OrderDetailClass

admin.site.register(OrderClass)
admin.site.register(OrderDetailClass)
