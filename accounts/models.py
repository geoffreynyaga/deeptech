from django.contrib.auth import get_user_model
from django.contrib.gis.db import models as gis_models
from django.db import models
from django.db.models.signals import post_save

from phonenumber_field.modelfields import PhoneNumberField

# import django get_user_model() model

User = get_user_model()
# Create your models here.


class Farmer(models.Model):
    class Meta:
        verbose_name = "Farmer"
        verbose_name_plural = "Farmers"

    created_by = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True
    )
    farm_name = models.CharField(max_length=100, blank=True, null=True)
    id_number = models.IntegerField(null=True, blank=True)
    phone_number = PhoneNumberField(blank=True)
    address = models.TextField(blank=True, null=True)

    location_pin = gis_models.PointField(blank=True, null=True)
    boundary = gis_models.MultiPolygonField(blank=True)

    acreage = models.FloatField(default=0)
    pin_number = models.CharField(blank=True, null=True, max_length=20)
    county = models.CharField(max_length=30)
    sub_county = models.CharField(max_length=30)
    ward = models.CharField(max_length=30, blank=True, null=True)
    total_acreage_sprayed = models.FloatField(default=0)
    total_acreage_mapped = models.FloatField(default=0)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.farm_name


class SeedCompany(models.Model):
    class Meta:
        verbose_name = "Seed Company"
        verbose_name_plural = "Seed Companies"

    company_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True)
    address = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    location_pin = gis_models.PointField(blank=True, null=True)

    pin_number = models.CharField(blank=True, null=True, max_length=20)
    county = models.CharField(max_length=30)
    sub_county = models.CharField(max_length=30, blank=True, null=True)
    ward = models.CharField(max_length=30, blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


class ChemicalCompany(models.Model):
    class Meta:
        verbose_name = "Chemical Company"
        verbose_name_plural = "Chemical Companies"

    company_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True)
    address = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    location_pin = gis_models.PointField(blank=True, null=True)

    pin_number = models.CharField(blank=True, null=True, max_length=20)
    county = models.CharField(max_length=30)
    sub_county = models.CharField(max_length=30, blank=True, null=True)
    ward = models.CharField(max_length=30, blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
