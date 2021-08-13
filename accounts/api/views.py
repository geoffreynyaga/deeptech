from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Farmer

from .serializers import FarmerListSerializer


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
