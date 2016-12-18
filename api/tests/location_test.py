from django.test import TestCase
from api.models import Location

class LocationTest(TestCase):
    sample_location_data = {'name': 'Youth Green',
                            'category': 'Community Garden',
                            'address_1': '12467 W. Osborne Street',
                            'city': 'Los Angeles',
                            'state': 'CA',
                            'zipcode': '91331',
                            'latitude': 34.25777331,
                            'longitude': -118.4046685}

    def test_creating_location(self):
        loc = Location(**self.sample_location_data)
        loc.save()
        query = Location.objects.filter(name='Youth Green')
        self.assertEqual(1, len(query))
        loc = query[0]
        self.assertEqual('Los Angeles', loc.city)
        self.assertEqual('91331', loc.zipcode)
        self.assertEqual(34.257773, float(loc.latitude))

    def test_querying_by_location(self):
        Location(**self.sample_location_data).save()
        query = Location.objects.in_distance(1, fields=['latitude', 'longitude'],
                                             points=[34.257773, -118.404669])
        self.assertEqual(1, len(query))

        query = Location.objects.in_distance(1, fields=['latitude', 'longitude'],
                                             points=[0, 0])
        self.assertEqual(0, len(query))
