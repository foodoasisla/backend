from django.db import models


class Location(models.Model):
    LOCATION_TYPES = ('Community Garden', "Farmer's Market",
                      'Food Bank', 'Grocery Store')

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=80, blank=False)
    address_1 = models.CharField(max_length=60, blank=False)
    address_2 = models.CharField(max_length=40, blank=True, default='')
    city = models.CharField(max_length=30, blank=False)
    state = models.CharField(max_length=2, blank=True, default='CA')
    zip = models.CharField(max_length=5, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    type = models.CharField(choices=LOCATION_TYPES, blank=False)

    class Meta:
        ordering = ('created', )
