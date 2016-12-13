from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Location
from api.serializers import LocationSerializer


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def location_list(request):
    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def nearby_locations(request):
    if not request.method == 'GET':
        return HttpResponse(status=404)

    # Radius in meters
    radius = request.GET.get('radius', 1000)
    lat = request.GET.get('latitude')
    lon = request.GET.get('longitude')

    if not (lat and lon):
        return HttpResponse(status=422)

    query = Location.objects.in_distance(int(radius), fields=['latitude', 'longitude'],
                                         points=[float(lat), float(lon)])
    return JSONResponse(LocationSerializer(query.all(), many=True).data)

@csrf_exempt
def location_detail(request, pk):
    try:
        location = Location.objects.get(pk=pk)
    except Location.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LocationSerializer(location)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LocationSerializer(location, data=data)
        if serializer.is_valid():
            serializer.save()
            return  JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        location.delete()
        return HttpResponse(status=204)
