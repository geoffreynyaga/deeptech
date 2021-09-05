from django.contrib import admin

from leaflet.admin import LeafletGeoAdmin

from farm.models import (
    Chemical,
    FarmCrop,
    FarmDisease,
    FarmPest,
    PlotDetail,
    PlotMap,
    SprayDetail,
)

# Register your models here.

# admin.site.register(PlotDetail)
admin.site.register(PlotDetail, LeafletGeoAdmin)

admin.site.register(PlotMap, LeafletGeoAdmin)
admin.site.register(FarmCrop)

admin.site.register(Chemical)
admin.site.register(SprayDetail)
admin.site.register(FarmDisease)
admin.site.register(FarmPest)
