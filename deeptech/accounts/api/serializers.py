# create model serializer
from accounts.models import Farmer, PlotDetail
from django.contrib.auth.models import User
from rest_framework import serializers


class PlotSerializer(serializers.ModelSerializer):
    class Meta:

        model = PlotDetail

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
            "first_name",
            "last_name",
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
