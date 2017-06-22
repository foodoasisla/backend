from rest_framework import generics

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
        radius = self.request.query_params.get('radius', 1000)
        lat = self.request.query_params.get('latitude')
        lon = self.request.query_params.get('longitude')

        # set default map center if no params are passed in
        if not (lat and lon):
            lat = 34.046561
            lon = -118.2499777

        queryset = Location.objects.in_distance(int(radius), fields=['latitude', 'longitude'],
                                                points=[float(lat), float(lon)])

        return queryset


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CommunityGardenLocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.filter(category='Community Garden')


class GroceryStoreLocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.filter(category='Grocery Store')


class FoodPantryLocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.filter(category='Food Pantry')


class HourList(generics.ListCreateAPIView):
    queryset = Hour.objects.all()
    serializer_class = HourSerializer


class HourDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hour.objects.all()
    serializer_class = HourSerializer
