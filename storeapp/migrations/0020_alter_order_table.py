# Generated by Django 4.2.7 on 2023-12-01 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0019_alter_order_date_ordered'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='order',
            table='storapp_orderprofuct',
        ),
    ]
