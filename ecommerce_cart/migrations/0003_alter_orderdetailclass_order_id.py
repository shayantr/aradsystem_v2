# Generated by Django 4.2.3 on 2023-07-28 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_cart', '0002_alter_orderdetailclass_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetailclass',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce_cart.orderclass'),
        ),
    ]