from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from accounts.models import Farmer

from .serializers import FarmerDetailSerializer, FarmerListSerializer


# generics.ListAPIView
class FarmerListAPIView(generics.ListCreateAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerListSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        print(queryset, "queryset")
        # qs = queryset.filter(acreage__gte=100).filter(farm_name="Kotut")
        # print(qs,"qs")

        serializer = FarmerListSerializer(queryset, many=True)

        return Response(serializer.data)


# Retrieve a specific Farmer using RetrieveAPIView
class FarmerDetailAPIView(generics.RetrieveAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = "pk"

    # def get_object(self):
    #     obj = self.get_queryset().filter(id=self.kwargs["pk"])
    #     print(obj, "obj")
    #     return obj.first()

    # def get(self, request):
    #     # Note the use of `get_object()` instead of `self.object`
    #     obj = self.get_object()
    #     print(obj, "obj")
    #     serializer = FarmerDetailSerializer(obj)
    #     return Response(serializer.data)
