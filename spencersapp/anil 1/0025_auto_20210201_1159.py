# Generated by Django 3.1.2 on 2021-02-01 06:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spencersapp', '0024_auto_20210201_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 11, 59, 0, 231185)),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 11, 59, 0, 231185)),
        ),
        migrations.AlterField(
            model_name='detailcategory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 11, 59, 0, 231185)),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 11, 59, 0, 231185)),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 11, 59, 0, 231185)),
        ),
    ]
