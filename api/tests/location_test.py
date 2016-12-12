from django.test import TestCase
from api.models import Location

class LocationTest(TestCase):
    def test_creating_location(self):
        loc_data = {'name': 'Youth Green',
                    'category': 'Community Garden',
                    'address_1': '12467 W. Osborne Street',
                    'city': 'Los Angeles',
                    'state': 'CA',
                    'zipcode': '91331',
                    'latitude': 34.25777331,
                    'longitude': -118.4046685}
        loc = Location(**loc_data)
        loc.save()
        query = Location.objects.filter(name='Youth Green')
        self.assertEqual(1, len(query))
        loc = query[0]
        self.assertEqual('Los Angeles', loc.city)
        self.assertEqual('91331', loc.zipcode)
        self.assertEqual(34.257773, float(loc.latitude))
