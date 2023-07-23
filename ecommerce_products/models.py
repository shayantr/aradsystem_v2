from django.db.models import Q
from django.db import models
from django.utils.html import mark_safe
from django.db.models.signals import pre_save

from ecommerce_products.utils import *

# Create your models here.
class ProductManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def search(self, query):
        lookup = Q(title__icontains=query) | Q(description__icontains=query)
        return self.get_queryset().filter(lookup, active=True).distinct()


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    slug = models.SlugField(blank=True, unique=True)
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



def pre_save_reciver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = uniqe_slug_gen(instance)


pre_save.connect(pre_save_reciver, sender=Product)