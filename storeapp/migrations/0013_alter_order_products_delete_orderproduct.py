# Generated by Django 4.2.7 on 2023-11-29 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0012_remove_order_total_price_orderproduct_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='storeapp.product'),
        ),
        migrations.DeleteModel(
            name='OrderProduct',
        ),
    ]
