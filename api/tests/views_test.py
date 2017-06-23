from django.test import TestCase
from api.models import Location


class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.spring_street = Location.objects.create(
            name='Spring Street Community Garden',
            latitude=34.0444447, longitude=-118.2965976,
            category='Community Garden')

        cls.trader_joes = Location.objects.create(
            name="Trader Joe's",
            latitude=34.0086873, longitude=-118.4033927,
            category='Grocery Store')

        cls.bread_of_life = Location.objects.create(
            name="Bread of Life Community Outreach",
            latitude=33.858486,
            longitude=-118.092907,
            category='Food Pantry')

        cls.stator_bros = Location.objects.create(
            name="Stater Bros. Markets",
            latitude=34.098075,
            longitude=-117.872853,
            category='Super Market')

    def test_index(self):
        response = self.client.get('/locations/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(4, len(response.json()))
        self.assertEqual(None, response.json()['previous'])
        self.assertEqual(None, response.json()['next'])
        self.assertEqual(4, response.json()['count'])
        self.assertEqual('Spring Street Community Garden',
                         response.json()['results'][0]['name'])

    def test_location_within_radius(self):
        response = self.client.get('/nearby_locations/', {'latitude': 34.0444447,
                                                          'longitude': -118.296597})
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json()['count'])
        self.assertEqual('Spring Street Community Garden',
                         response.json()['results'][0]['name'])

    def test_location_outside_of_radius(self):
        # Santa Monica State Beach
        response = self.client.get('/nearby_locations/', {'latitude': 34.0051628,
                                                          'longitude': -118.5145828})
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.json()['results'])

    def test_location_with_large_radius_override(self):
        # Baldwin Hills Scenic Overlook
        response = self.client.get('/nearby_locations/', {'radius': 15000,
                                                          'latitude': 34.0139142,
                                                          'longitude': -118.3800862})
        self.assertEqual(200, response.status_code)
        self.assertEqual(2, response.json()['count'])
        self.assertEqual('Spring Street Community Garden',
                         response.json()['results'][0]['name'])

    def test_location_with_small_radius_override(self):
        # Staples Center
        response = self.client.get('/nearby_locations/', {'radius': 1,
                                                          'latitude': 34.0371399,
                                                          'longitude': -118.2682917})
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.json()['results'])

    def test_location_with_no_lat_long(self):
        response = self.client.get('/nearby_locations/')
        self.assertEqual(200, response.status_code)
        self.assertEqual([], response.json()['results'])

    def test_location_detail(self):
        locations = self.client.get('/locations/')
        id = locations.json()['results'][0]['id']
        response = self.client.get('/locations/{}/'.format(id))
        self.assertEqual(200, response.status_code)
        self.assertEqual('Spring Street Community Garden',
                         response.json()['name'])

    def test_location_detail_no_id_found(self):
        response = self.client.get('/locations/10000000000')
        self.assertEqual(301, response.status_code)

    def test_community_gardens(self):
        response = self.client.get('/locations/community_gardens/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json()['count'])
        self.assertEqual('Spring Street Community Garden',
                         response.json()['results'][0]['name'])

    def test_grocery_stores(self):
        response = self.client.get('/locations/grocery_stores/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json()['count'])
        self.assertEqual("Trader Joe's", response.json()['results'][0]['name'])

    def test_food_pantries(self):
        response = self.client.get('/locations/food_pantries/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json()['count'])
        self.assertEqual("Bread of Life Community Outreach",
                         response.json()['results'][0]['name'])

    def test_food_super_markets(self):
        response = self.client.get('/locations/super_markets/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json()['count'])
        self.assertEqual("Stater Bros. Markets",
                         response.json()['results'][0]['name'])

    def test_analytics_summary(self):
        response = self.client.get('/analytics/locations/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(4, response.json()['total locations'])
