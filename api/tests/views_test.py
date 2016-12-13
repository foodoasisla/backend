from django.test import TestCase
from api.models import Location

class TestViews(TestCase):
    def test_fetches_index(self):
        Location(name='Test Community Garden',
                 latitude=0,
                 longitude=0).save()

        response = self.client.get('/locations')
        # import IPython; IPython.embed()
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(response.json()))
        self.assertEqual('Test Community Garden',
                         response.json()[0]['name'])

    def test_fetches_by_location(self):
        Location(name='Test Community Garden',
                 latitude=12.345678,
                 longitude=12.345678).save()

        # query within radius
        response = self.client.get('/nearby_locations', {'latitude': 12.345678,
                                                         'longitude': 12.345678})
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(response.json()))
        self.assertEqual('Test Community Garden',
                         response.json()[0]['name'])

        # query outside of radius
        response = self.client.get('/nearby_locations', {'latitude': 12.30,
                                                         'longitude': 12.345678})
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, len(response.json()))

        # query with radius override
        response = self.client.get('/nearby_locations', {'radius': 15000,
                                                         'latitude': 12.30,
                                                         'longitude': 12.345678})
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(response.json()))
