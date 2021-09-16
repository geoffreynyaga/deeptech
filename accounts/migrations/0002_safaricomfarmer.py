# Generated by Django 3.2.6 on 2021-09-06 17:16

import django.contrib.gis.db.models.fields
from django.db import migrations, models

import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SafaricomFarmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_name', models.CharField(blank=True, max_length=100, null=True)),
                ('id_number', models.IntegerField(blank=True, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('address', models.TextField(blank=True, null=True)),
                ('location_pin', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('boundary', django.contrib.gis.db.models.fields.PolygonField(blank=True, srid=4326)),
                ('acreage', models.FloatField(default=0)),
                ('county', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('total_acreage_sprayed', models.FloatField(default=0)),
                ('total_acreage_mapped', models.FloatField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Safaricom Farmer',
                'verbose_name_plural': 'Safaricom Farmers',
            },
        ),
    ]
