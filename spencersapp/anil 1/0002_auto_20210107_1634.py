# Generated by Django 3.1.2 on 2021-01-07 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spencersapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 7, 16, 34, 41, 523620)),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 7, 16, 34, 41, 523620)),
        ),
        migrations.AlterField(
            model_name='detailcategory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 7, 16, 34, 41, 523620)),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 7, 16, 34, 41, 523620)),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 7, 16, 34, 41, 523620)),
        ),
    ]
