# Generated by Django 3.0.3 on 2020-03-08 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200307_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(default='Ex: Jl. Kartika'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.TextField(default='Ex: Jl. Kartika'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(default='Ex: Sintia', max_length=100),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone',
            field=models.CharField(default='Ex: +62xxxxxxxxxx', max_length=20),
        ),
    ]