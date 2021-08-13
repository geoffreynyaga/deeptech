from django.urls import path

from .views import FarmerListAPIView

urlpatterns = [
    path("list/", FarmerListAPIView.as_view(), name="farmers_list"),
]
