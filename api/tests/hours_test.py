from django.test import TestCase
from api.models import Hour, Location


class HourTest(TestCase):
    sample_location_data = {'name': 'Youth Green',
                            'category': 'Community Garden',
                            'address_1': '12467 W. Osborne Street',
                            'city': 'Los Angeles',
                            'state': 'CA',
                            'zipcode': '91331',
                            'latitude': 34.25777331,
                            'longitude': -118.4046685}
    sample_hour_data = {'day': 'AllMo',
                        'open_time': '08:00',
                        'close_time': '14:00',
                        }

    def test_creating_hour(self):
        loc = Location(**self.sample_location_data)
        loc.save()
        self.sample_hour_data['location_id'] = loc.id
        hour = Hour(**self.sample_hour_data)
        hour.save()
        query = Hour.objects.filter(day='AllMo')
        hour = query[0]
        self.assertEqual(1, len(query))
        self.assertEqual('AllMo', hour.day)
        self.assertEqual('08:00:00', str(hour.open_time))
        self.assertEqual('14:00:00', str(hour.close_time))
