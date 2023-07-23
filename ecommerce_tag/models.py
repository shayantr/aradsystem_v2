from django.db import models
from django.db.models.signals import pre_save, post_save

from ecommerce_products.models import Product

from ecommerce_tag.utils import *
# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, related_name='tags', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'


def tag_pre_save_reciver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = uniqe_slug_gen(instance)


pre_save.connect(tag_pre_save_reciver, sender=Tag)

