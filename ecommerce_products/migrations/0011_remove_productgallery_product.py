# Generated by Django 4.2.3 on 2023-07-25 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_products', '0010_productgallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productgallery',
            name='product',
        ),
    ]