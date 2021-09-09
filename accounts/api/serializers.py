# create model serializer
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point

from rest_framework import serializers
from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer,
    GeometrySerializerMethodField,
)

from accounts.models import Farmer, SafaricomFarmer
from farm.models import PlotDetail


class PlotSerializer(GeoFeatureModelSerializer):
    class Meta:

        model = PlotDetail
        geo_field = "boundary"

        fields = (
            "name",
            "acreage",
            "boundary",
            "crop",
            "date_planted",
        )


class FarmerListSerializer(serializers.ModelSerializer):
    # serfor list of farmers
    plots = serializers.SerializerMethodField()

    def get_plots(self, obj):
        qs = PlotDetail.objects.filter(farm__pk=obj.pk).order_by("-id")
        print(qs, "qs")
        qs_final = PlotSerializer(qs, many=True).data

        return qs_final

    class Meta:

        model = Farmer

        fields = (
            "id",
            "farm_name",
            "location_pin",
            "boundary",
            "plots",
            "id_number",
            "phone_number",
            "address",
            "acreage",
            "pin_number",
            "county",
            "sub_county",
            "ward",
        )


class FarmerDetailSerializer(GeoFeatureModelSerializer):
    # serfor list of farmers
    plots = serializers.SerializerMethodField()

    def get_plots(self, obj):
        qs = PlotDetail.objects.filter(farm__pk=obj.pk).order_by("-id")

        qs_final = PlotSerializer(qs, many=True).data
        return qs_final

    class Meta:

        model = Farmer
        geo_field = "location_pin"

        fields = (
            "id",
            "farm_name",
            "location_pin",
            "id_number",
            "phone_number",
            "address",
            "acreage",
            "pin_number",
            "county",
            "sub_county",
            "ward",
            "boundary",
            "plots",
        )


class SafaricomFarmerListSerializer(serializers.ModelSerializer):
    class Meta:

        model = SafaricomFarmer

        fields = (
            "farmer_name",
            "id_number",
            "phone_number",
            "address",
            "location_pin",
            "boundary",
            "has_errors",
            "acreage",
            "county",
            "location",
            "total_acreage_sprayed",
            "total_acreage_mapped",
            "date_created",
            "date_modified",
        )
