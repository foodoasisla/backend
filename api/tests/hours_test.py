from django.test import TestCase
from api.models import Hour, Location


class HourTest(TestCase):

    def test_creating_hour(self):
        location = {'name': 'Youth Green',
                    'category': 'Community Garden',
                                'address_1': '12467 W. Osborne Street',
                                'city': 'Los Angeles',
                                'state': 'CA',
                                'zipcode': '91331',
                                'latitude': 34.25777331,
                                'longitude': -118.4046685}
        loc = Location(**location)
        loc.save()

        hour = Hour(day='AllMo', open_time='08:00',
                    close_time='14:00', location_id=loc.id)
        hour.save()

        query = Hour.objects.filter(day='AllMo')
        hour = query[0]

        self.assertEqual(1, len(query))
        self.assertEqual('AllMo', hour.day)
        self.assertEqual('08:00:00', str(hour.open_time))
        self.assertEqual('14:00:00', str(hour.close_time))
        self.assertEqual(loc.id, hour.location_id)
