from rest_framework import status
from rest_framework import generics

from rest_framework.response import Response
from api.models import Location
from api.models import Hour
from api.serializers import LocationSerializer
from api.serializers import HourSerializer

class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        queryset = Location.objects.all()
        return queryset

class NearbyLocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        # Radius in meters
        radius = self.request.query_params.get('radius', 10000)
        lat = self.request.query_params.get('latitude')
        lon = self.request.query_params.get('longitude')

        if not (lat and lon):
            return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        queryset = Location.objects.in_distance(int(radius), fields=['latitude', 'longitude'],
                                         points=[float(lat), float(lon)])

        return queryset


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class HourList(generics.ListCreateAPIView):
    queryset = Hour.objects.all()
    serializer_class = HourSerializer

class HourDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hour.objects.all()
    serializer_class = HourSerializer

