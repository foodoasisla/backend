from django.core.management.base import BaseCommand
import csv

from api.models import Location, Hour

import os


class Command(BaseCommand):
    help = 'in-process command for ingesting csv data with hours.'

    def handle(self, *args, **options):
        for filename in os.listdir('hours_csv_TEST'):
            print('importing CSV file {0}'.format(filename))
            with open(os.path.join('hours_csv_TEST', filename), 'r') as f:
                reader = csv.reader(f)
                next(f)
                for r in reader:
                    print('populating row: {0}'.format(r))
                    loc = Location(name=r[0], address_1=r[1], address_2=r[2], city=r[3], state=r[
                                   4], zipcode=r[5], phone=r[6], latitude=r[7], longitude=r[8], category=r[9], website=r[10], active=True)
                    loc.save()
                    for i in [r[11:i + 3] for i in range(11, len(r), 3)]:
                        h = Hour(day=i[0], open_time=i[1],
                                 close_time=i[2], location=loc)
                        print(h)
                        h.save()


# in progress ingest script
# sample_data = ['Arleta Community Garden','8800 Canterbury Avenue',' ','San Fernando Valley','CA','91331',' ',34.22961903400005, -118.42451217799999,'Community Garden','Y','1stMo', '08:00', '12:00','2ndTu', '08:00', '12:00']
#
# create the location
# loc = Location(name=sample_data[0],address_1=sample_data[1],address_2=sample_data[2],city=sample_data[3], state=sample_data[4], zipcode=sample_data[5], phone=sample_data[6], latitude=sample_data[7], longitude=sample_data[7],category='CG',active=True)
# loc.save()
# create the hour for the given location
# for i in [sample_data[11:][i:i+3] for i in range(0, len(sample_data[11:-1]),3)]:
    # h = Hour(day=i[0], open_time=i[1], close_time=i[2], location = loc)
