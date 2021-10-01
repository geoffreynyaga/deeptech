# create model serializer
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point

from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from accounts.models import PlotDetail


class PlotSerializer(GeoFeatureModelSerializer):
    class Meta:

        model = PlotDetail
        geo_field = "boundary"

        fields = (
            "name",
            "acreage",
            "boundary",
            "crop",
        )
