from rest_framework import serializers
from api.models import Location


class LocationSerializer(serializers.Serializer):

    class Meta:
        model = Location
        fields = ('id', 'name', 'address_1', 'address_2', 'city',
                  'state', 'zip', 'phone', 'latitude', 'longitude', 'category')

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
        instance.zip = validated_data.get('zip', instance.zip)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance