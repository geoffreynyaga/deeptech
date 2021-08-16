# Generated by Django 3.2.6 on 2021-08-14 19:42

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_plotmap"),
    ]

    operations = [
        migrations.AddField(
            model_name="plotmap",
            name="uploaded_tif",
            field=models.FileField(blank=True, null=True, upload_to="uploads/"),
        ),
        migrations.AlterField(
            model_name="plotmap",
            name="raster",
            field=django.contrib.gis.db.models.fields.RasterField(
                blank=True, null=True, srid=4326
            ),
        ),
    ]