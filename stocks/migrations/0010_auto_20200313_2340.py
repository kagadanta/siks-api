# Generated by Django 3.0.3 on 2020-03-13 16:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('stocks', '0009_auto_20200313_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemin',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
