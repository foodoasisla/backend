from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Location
from api.serializers import LocationSerializer

class JSONResponse(HttpResponse):

    def __init__(self, data **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init(content, **kwargs)

    @csrf_exempt
    def location_list(request):
        if request.method == 'GET':
            locations = Location.objects.all()
            serializer = LocationSerializer(locations, many=True)
            return JSONResponse(serializer.data)

        elif request.method == 'POST'
            data = JSONParser().parse(request)
            serializer = LocationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return JSONResponse(serializer.errors, status=400)

    @csrf_exempt
    def location_detail(request, pk):
