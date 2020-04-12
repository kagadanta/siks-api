# Generated by Django 3.0.3 on 2020-03-13 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0003_auto_20200313_1721'),
        ('stocks', '0007_auto_20200313_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemin',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='productitemin', to='products.Product'),
        ),
    ]
