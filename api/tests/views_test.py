from django.test import TestCase
from api.models import Location


class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_location = Location.objects.create(
            name='Spring Street Community Garden',
            latitude=34.0444447, longitude=-118.2965976,
            category='Community Garden')

    def test_fetches_index(self):
        response = self.client.get('/locations/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(4, len(response.json()))
        self.assertEqual(None, response.json()['previous'])
        self.assertEqual(None, response.json()['next'])
        self.assertEqual(1, response.json()['count'])
        self.assertEqual('Spring Street Community Garden',
                         response.json()['results'][0]['name'])

    def test_fetches_by_location_within_radius(self):
        response = self.client.get('/nearby_locations/', {'latitude': 34.0444447,
                                                          'longitude': -118.296597})
        self.assertEqual(200, response.status_code)
        self.assertEqual('Spring Street Community Garden',
                         response.json()['results'][0]['name'])

    def test_fetches_by_location_outside_of_radius(self):
        # Santa Monica State Beach
        response = self.client.get('/nearby_locations/', {'latitude': 34.0051628,
                                                          'longitude': -118.5145828})
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.json()['results'])

    def test_fetches_by_location_with_large_radius_override(self):
        # Baldwin Hills Scenic Overlook
        response = self.client.get('/nearby_locations/', {'radius': 15000,
                                                          'latitude': 34.0139142,
                                                          'longitude': -118.3800862})
        self.assertEqual(200, response.status_code)
        self.assertEqual('Spring Street Community Garden',
                         response.json()['results'][0]['name'])

    def test_fetches_by_location_with_small_radius_override(self):
        # Staples Center
        response = self.client.get('/nearby_locations/', {'radius': 1,
                                                          'latitude': 34.0371399,
                                                          'longitude': -118.2682917})
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.json()['results'])

    def test_fetches_by_location_with_no_lat_long(self):
        response = self.client.get('/nearby_locations/')
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.json()['results'])

    def test_fetches_by_correct_category(self):
        response = self.client.get('/locations/community_gardens/')
        self.assertEqual(200, response.status_code)
        self.assertEqual('Spring Street Community Garden',
                         response.json()['results'][0]['name'])

    def test_ignores_incorrect_category(self):
        response = self.client.get('/locations/grocery_stores/')
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.json()['results'])
