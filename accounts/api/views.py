import logging

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Farmer, SafaricomFarmer
from accounts.tasks import add_two_numbers

from .serializers import (
    FarmerDetailSerializer,
    FarmerListSerializer,
    SafaricomFarmerListSerializer,
)

logger = logging.getLogger(__name__)

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


class SafaricomFarmerListAPIView(generics.ListCreateAPIView):
    queryset = SafaricomFarmer.objects.all()
    serializer_class = SafaricomFarmerListSerializer
    permission_classes = [IsAuthenticated]

    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     print(queryset, "queryset")
    #     # qs = queryset.filter(acreage__gte=100).filter(farm_name="Kotut")
    #     # print(qs,"qs")

    #     serializer = SafaricomFarmerListSerializer(queryset, many=True)

    #     return Response(serializer.data)


class FarmerListTestAPIView(APIView):
    serializer_class = FarmerListSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        print(data, "data")
        logger.info(data, "data")
        x = data["x"]
        y = data["y"]

        try:
            result = add_two_numbers.delay(x, y)
            print(result, "result")
            
            # return Response({"result": result.get()})

            add_two_numbers.delay(x, y)
            add_two_numbers.apply_async(args=[x, y])
            return Response({"message": "Task has been submitted"})
        except Exception as e:
            print(e, "e")
            logger.error(e, "e")
            return Response({"message": "Error Submitting Task"})


