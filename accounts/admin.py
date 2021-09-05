from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from accounts.models import ChemicalCompany, Farmer, SeedCompany


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


admin.site.register(Farmer, FarmerAdmin)
admin.site.register(ChemicalCompany)
admin.site.register(SeedCompany)


# OSMGeoAdmin import
