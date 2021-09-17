from django.urls import path

from .views import (
    FarmerDetailAPIView,
    FarmerListAPIView,
    FarmerListTestAPIView,
    SafaricomFarmerListAPIView,
)

urlpatterns = [
    path("list/", FarmerListAPIView.as_view(), name="farmers_list"),
    path("list/<pk>/", FarmerDetailAPIView.as_view(), name="farmer_detail"),
    path(
        "safaricom/list/",
        SafaricomFarmerListAPIView.as_view(),
        name="safcom_farmer_detail",
    ),
    path("test/", FarmerListTestAPIView.as_view(), name="test_celery"),
]
