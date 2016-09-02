from django.db import models


class Location(models.Model):
    LOCATION_CATEGORIES = (('CG','Community Garden'), ('FM',"Farmer's Market"),('FB','Food Bank'),('GS','Grocery Store'),('SM','Super Market'), ('CV','Convenience Store'))

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=80, blank=False)
    address_1 = models.CharField(max_length=60, blank=False)
    address_2 = models.CharField(max_length=40, blank=True, default='')
    city = models.CharField(max_length=30, blank=False)
    state = models.CharField(max_length=2, blank=True, default='CA')
    zipcode = models.CharField(max_length=5, blank=False)
    phone = models.CharField(max_length=20, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    category = models.CharField(choices=LOCATION_CATEGORIES, blank=False, max_length=50)
    website = models.CharField(max_length=60, blank=True, default=''  )
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created', )
