# Generated by Django 3.2.6 on 2021-09-07 07:56

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_safaricomfarmercsv'),
    ]

    operations = [
        migrations.AddField(
            model_name='safaricomfarmer',
            name='has_errors',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='safaricomfarmer',
            name='boundary',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, null=True, srid=4326),
        ),
    ]
