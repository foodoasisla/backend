from django.test import TestCase
from api.models import Hour

# will need to mock out a location


class HourTest(TestCase):
    sample_hour_data = {'day': 'AllMo',
                        'open_time': '08:00',
                        'close_time': '14:00',
                        'location_id': '1'}

    def test_creating_hour(self):
        hour = Hour(**self.sample_hour_data)
        hour.save()
        query = Hour.objects.filter(day='AllMo')
        self.assertEqual(1, len(query))
