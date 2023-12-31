# Generated by Django 4.2.3 on 2023-07-19 18:12

from django.db import migrations, models
import ecommerce_products.utils


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='static_cdn/static_root/admin/images/home/product.jpg', null=True, upload_to=ecommerce_products.utils.upload_image_path),
        ),
    ]
