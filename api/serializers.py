from rest_framework import serializers
from api.models import Location, Hour
import time


class HourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hour
        fields = ('day', 'open_time', 'close_time', 'location_id')

    def create(self, validated_data):
        return Hour.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.day = validated_data.get('day', instance.day)
        instance.open_time = validated_data.get(
            'open_time', instance.open_time)
        instance.close_time = validated_data.get(
            'close_time', instance.close_time)
        instance.location_id = validated_data.get(
            'location_id', instance.location_id)
        instance.save()
        return instance

# Note. This must come before reference in LocationSerializer


class HourListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hour
        fields = ('day', 'open_time', 'close_time', )


class LocationSerializer(serializers.ModelSerializer):
    hours = HourListSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ('id', 'name', 'address_1', 'address_2', 'city',
                  'state', 'zipcode', 'phone', 'latitude', 'longitude', 'category', 'hours', 'website')

    def create(self, validated_data):
        return Location.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address_1 = validated_data.get(
            'address_1', instance.address_1)
        instance.address_2 = validated_data.get(
            'address_2', instance.address_2)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.zip = validated_data.get('zipcode', instance.zip)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get(
            'longitude', instance.longitude)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
