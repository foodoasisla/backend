from django.core.management.base import BaseCommand
import csv

from api.models import Location, Hour

import os


class Command(BaseCommand):
    help = 'in-process command for ingesting csv data with hours.'

    def handle(self, *args, **options):
        for filename in os.listdir('csv_hours_test_data'):
            print('importing CSV file {0}'.format(filename))
            with open(os.path.join('csv_hours_test_data', filename), 'r') as f:
                reader = csv.reader(f)
                next(f)
                for r in reader:
                    print('populating row: {0}'.format(r))
                    loc = Location(name=r[0], address_1=r[1], address_2=r[2], city=r[3], state=r[
                                   4], zipcode=r[5], phone=r[6], latitude=r[7], longitude=r[8], category=r[9], website=r[10], active=True)
                    loc.save()
                    hours = list(filter(None, r[11:]))
                    for i in [hours[i:i + 3] for i in range(0, len(hours), 3)]:
                        h = Hour(day=i[0], open_time=i[1],
                                 close_time=i[2], location=loc)
                        h.save()
