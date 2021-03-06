# Generated by Django 3.0.3 on 2020-03-27 09:41

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0010_remove_supplier_is_publish'),
        ('products', '0006_remove_product_is_publish'),
        ('stocks', '0023_auto_20200325_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemin',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='productitemin', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='itemin',
            name='stockin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='stockinitemin', to='stocks.StockIn'),
        ),
        migrations.AlterField(
            model_name='stockin',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2020, 3, 27), null=True),
        ),
        migrations.AlterField(
            model_name='stockin',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='supplierstockin', to='users.Supplier'),
        ),
        migrations.AlterField(
            model_name='stockout',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2020, 3, 27), null=True),
        ),
    ]
