# Generated by Django 3.1.2 on 2021-02-01 06:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spencersapp', '0018_auto_20210201_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 11, 49, 12, 852773)),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 11, 49, 12, 852773)),
        ),
        migrations.AlterField(
            model_name='detailcategory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 11, 49, 12, 852773)),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 11, 49, 12, 852773)),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 11, 49, 12, 852773)),
        ),
    ]
