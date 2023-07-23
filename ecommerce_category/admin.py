from django.contrib import admin

from ecommerce_category.models import ProductCategory

# Register your models here.
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'name']
    list_display_links = ['id', 'title']

    class Meta:
        model = ProductCategory

admin.site.register(ProductCategory, ProductCategoryAdmin)