# Generated by Django 3.0.3 on 2020-03-14 09:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0003_auto_20200313_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_init',
            field=models.BooleanField(default=True),
        ),
    ]