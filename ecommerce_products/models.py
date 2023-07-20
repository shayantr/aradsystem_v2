from django.db import models
from django.utils.html import mark_safe

from ecommerce_products.utils import *

# Create your models here.
class ProductManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='عکس محصول')
    active = models.BooleanField(default=False, verbose_name='فعال')

    objects = ProductManager()

    class Meta:
        verbose_name_plural = 'محصول'
        verbose_name = 'محصولات'

    def img_preview(self): #new
        return mark_safe(f'<img src = "{self.image.url}" width = "50"/>')

    def __str__(self):
        return self.title


