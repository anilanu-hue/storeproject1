# Generated by Django 3.1.2 on 2021-02-08 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spencersapp', '0003_auto_20210208_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_id', models.CharField(max_length=30)),
                ('is_order', models.BooleanField(default=False, max_length=10)),
                ('total', models.FloatField(default=0.0)),
                ('order_status', models.CharField(default='Pending', max_length=20)),
                ('ordered_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('shipping_to', models.TextField(blank=True, default='hyderabad', null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('corier_name', models.CharField(blank=True, max_length=50, null=True)),
                ('payment_type', models.CharField(blank=True, max_length=50, null=True)),
                ('isdeleted', models.BooleanField(default=False, max_length=10)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.IntegerField()),
                ('order_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='spencerscart.orders')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spencersapp.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
