from django.db import models
from django_earthdistance.models import EarthDistanceQuerySet


class Location(models.Model):
    objects = EarthDistanceQuerySet.as_manager()

    LOCATION_CATEGORIES = (('CG', 'Community Garden'), ('FM', "Farmer's Market"),
                           ('FB', 'Food Bank'), ('GS', 'Grocery Store'),
                           ('SM', 'Super Market'), ('OS', 'Other Stores'))

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
    category = models.CharField(
        choices=LOCATION_CATEGORIES, blank=False, max_length=50)
    website = models.CharField(max_length=60, blank=True, default='')
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created', )


class Hour(models.Model):
    DAYS = (('AllMo', 'Monday'), ('AllTu', 'Tuesday'), ('AllWe', 'Wednesday'), ('AllTh', 'Thursday'), ('AllFr', 'Friday'),
            ('AllSa', 'Saturday'), ('AllSu', 'Sunday'),
            ('1stMo','First Monday'), ('1stTu', 'First Tuesday'),
            ('1stWe', 'First Wednesday'), ('1stTh','First Thursday'), ('1stFr', 'First Friday'),
            ('1stSa', 'First Saturday'), ('1stSu','First Sunday'), ('2ndMo', 'Second Monday'),
            ('2ndTu', 'Second Tuesday'), ('2ndWe','Second Wednesday'), ('2ndTh', 'Second Thursday'),
            ('2ndFr', 'Second Friday'), ('2ndSa','Second Saturday'), ('2ndSu', 'Second Sunday'),
            ('3rdMo', 'Third Monday'), ('3rdTu','Third Tuesday'), ('3rdWe', 'Third Wednesday'),
            ('3rdTh', 'Third Thursday'), ('3rdFr','Third Friday'), ('3rdSa', 'Third Saturday'),
            ('3rdSu', 'Third Sunday'), ('4thMo','Fourth Monday'), ('4thTu', 'Fourth Tuesday'),
            ('4thWe', 'Fourth Wednesday'), ('4thTh', 'Fourth Thursday'),
            ('4thFr','Fourth Friday'), ('4thSa', 'Fourth Saturday'),('4thSu', 'Fourth Sunday'),
            ('LstMo', 'Last Monday'), ('LstTu', 'Last Tuesday'), ('LstWe', 'Last Wednesday'), ('LstTh', 'Last Thursday'),
            ('LstFr', 'Last Friday'), ('LstSa', 'Last Saturday'), ('LstSu', 'Last Sunday'))

    day = models.CharField(choices=DAYS, blank=False, max_length=100)
    open_time = models.TimeField(blank=False)
    close_time = models.TimeField(blank=False)
