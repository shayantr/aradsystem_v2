# Generated by Django 4.2.3 on 2023-07-20 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_products', '0005_alter_product_options_alter_product_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
