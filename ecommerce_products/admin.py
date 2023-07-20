from django.contrib import admin
from ecommerce_products.models import *
# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'img_preview', 'title', 'description', 'price', 'active']
    list_display_links = ['id', 'title']

    class Meta:
        model = Product


admin.site.register(Product, ProductsAdmin)
