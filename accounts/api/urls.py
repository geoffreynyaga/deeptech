from django.urls import path

from .views import (
    FarmerDetailAPIView,
    FarmerListAPIView,
    FarmerListTestAPIView,
    SafaricomFarmerListAPIView,
    MappedSafaricomFarmersListByCountyAPIView,
    SafaricomFarmersErrorsListAPIView,
)

urlpatterns = [
    path("list/", FarmerListAPIView.as_view(), name="farmers_list"),
    path("list/<int:pk>/", FarmerDetailAPIView.as_view(), name="farmer_detail"),
    path(
        "safaricom/list/",
        SafaricomFarmerListAPIView.as_view(),
        name="safcom_farmer_detail",
    ),
    path(
        "safaricom/list/has-errors/",
        SafaricomFarmersErrorsListAPIView.as_view(),
        name="safcom_farmer_errors_list",
    ),
    path("test/", FarmerListTestAPIView.as_view(), name="test_celery"),
    path(
        "safaricom/mapped/",
        MappedSafaricomFarmersListByCountyAPIView.as_view(),
        name="mapped_safcom_farmer_by_county",
    ),
]
