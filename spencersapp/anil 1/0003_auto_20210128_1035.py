# Generated by Django 3.1.2 on 2021-01-28 05:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spencersapp', '0002_auto_20210107_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='brand',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 10, 35, 34, 191701)),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 10, 35, 34, 191701)),
        ),
        migrations.AlterField(
            model_name='detailcategory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 10, 35, 34, 191701)),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 10, 35, 34, 191701)),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 10, 35, 34, 191701)),
        ),
    ]
