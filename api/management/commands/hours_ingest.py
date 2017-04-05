from django.core.management.base import BaseCommand
import csv

from api.models import Location, Hour

import os


class Command(BaseCommand):
    help = 'in-process command for ingesting csv data with hours.'

    def handle(self, *args, **options):
        csv_files = ['farmers-market.csv']
        for file in csv_files:
            with open('csv_hours_test_data/{}'.format(file), 'r') as f:
                reader = csv.reader(f)
                print(reader)
                next(f)
                for r in reader:
                    loc = Location(name=r[0], address_1=r[1], address_2=r[2], city=r[3], state=r[
                                   4], zipcode=r[5], phone=r[6], latitude=r[7], longitude=r[8], category=r[9], website=r[10], active=True)
                    loc.save()
                    print(loc.name)
                    hours = list(filter(None, r[11:]))
                    for i in [hours[i:i + 3] for i in range(0, len(hours), 3)]:
                        open_time = list(i[1])
                        open_time.insert(-2, ':')
                        open_time = ''.join(open_time)
                        close_time = list(i[2])
                        close_time.insert(-2, ':')
                        close_time = ''.join(close_time)
                        h = Hour(day=i[0], open_time=open_time,
                                 close_time=close_time, location=loc)
                        h.save()
