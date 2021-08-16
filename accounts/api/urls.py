from django.urls import path

from .views import FarmerDetailAPIView, FarmerListAPIView

urlpatterns = [
    path("list/", FarmerListAPIView.as_view(), name="farmers_list"),
    path("list/<pk>/", FarmerDetailAPIView.as_view(), name="farmer_detail"),
]
