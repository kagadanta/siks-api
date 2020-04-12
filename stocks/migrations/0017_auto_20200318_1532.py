# Generated by Django 3.0.3 on 2020-03-18 08:32

import datetime

import django.utils.timezone
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('stocks', '0016_stockin_is_calculate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockout',
            old_name='is_publish',
            new_name='is_init',
        ),
        migrations.AddField(
            model_name='itemin',
            name='created_date',
            field=models.DateField(auto_now_add=True,
                                   default=datetime.datetime(2020, 3, 18, 8, 31, 57, 348165, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itemin',
            name='updated_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='itemout',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itemout',
            name='is_init',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='itemout',
            name='updated_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='stockcard',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockcard',
            name='updated_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='stockin',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockin',
            name='updated_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='stockout',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockout',
            name='updated_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='stockin',
            name='date',
            field=models.DateField(blank=True, default=datetime.date(2020, 3, 18), null=True),
        ),
    ]
