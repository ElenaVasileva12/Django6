# Generated by Django 4.2.7 on 2023-11-29 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0013_alter_order_products_delete_orderproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=2, max_digits=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateField(auto_now_add=True),
        ),
    ]