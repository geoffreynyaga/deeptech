from django.contrib import admin
from django.contrib.gis.db import models as gis_models

from leaflet.admin import LeafletGeoAdmin
from mapwidgets.widgets import GooglePointFieldWidget

from accounts.models import (
    ChemicalCompany,
    Farmer,
    SafaricomFarmer,
    SafaricomFarmerCSV,
    SeedCompany,
)
from mapwidgets.widgets import GooglePointFieldWidget


# Register your models here.
# add an admin view for Farmer model
class FarmerAdmin(LeafletGeoAdmin):
    fields = (
        "farm_name",
        "created_by",
        "location_pin",
        "boundary",
        "id_number",
        "phone_number",
        "address",
        "acreage",
        "pin_number",
        "county",
        "sub_county",
        "ward",
    )

    list_display = ("farm_name", "county", "phone_number")
    search_fields = ("farm_name",)
    # read_only_fields = ("pin_number",)


class SafaricomFarmerAdmin(LeafletGeoAdmin):
    # formfield_overrides = {
    #     gis_models.PointField: {"widget": GooglePointFieldWidget}
    # }

    fields = (
        "farmer_name",
        "has_errors",
        "error_comments",
        "county",
        "location",
        "location_pin",
        "boundary",
        "id_number",
        "phone_number",
        "address",
        "acreage",
        "total_acreage_sprayed",
        "total_acreage_mapped",
    )

    list_display = (
        "farmer_name",
        "is_mapped",
        "has_errors",
        "county",
        "acreage",
        "location_pin",
        "boundary",
    )
    search_fields = ("farmer_name",)
    list_filter = ("is_mapped", "has_errors", "county")
    # read_only_fields = ("pin_number",)


admin.site.register(Farmer, FarmerAdmin)
admin.site.register(SafaricomFarmer, SafaricomFarmerAdmin)

admin.site.register(ChemicalCompany)
admin.site.register(SeedCompany, LeafletGeoAdmin)
admin.site.register(SafaricomFarmerCSV)
