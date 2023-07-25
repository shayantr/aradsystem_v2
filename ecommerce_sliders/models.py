from django.db import models
from django.utils.html import mark_safe
import os
import datetime

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    date = datetime.datetime.now()
    year = date.year
    month = date.month
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f'products/{year}/{month}/{instance.title}/{final_name}'

# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    link = models.URLField(max_length=100, verbose_name='آدرس')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='عکس محصول')

    class Meta:
        verbose_name_plural = 'اسلایدر ها'
        verbose_name = 'اسلایدر'

    def img_preview(self): #new
        return mark_safe(f'<img src = "{self.image.url}" width = "50"/>')

    def __str__(self):
        return self.title
