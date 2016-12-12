from django.core.management.base import BaseCommand
import csv
from api.models import Location
import os

class Command(BaseCommand):
    help = 'Imports CSV file to populate local DB'

    def handle(self, *args, **options):
        for filename in os.listdir('csv_files'):
            print 'importing CSV file %s' % filename
            with open(os.path.join('csv_files', filename), 'r') as f:
                reader = csv.reader(f)
                next(f)  # skips first line so we don't import headers
                for r in reader:
                    print 'populating row: %s' % r
                    loc = Location(name=r[1], category=r[2], address_1=r[3],
                                   city=r[4], state=r[5], zipcode=r[6],
                                   latitude=float(r[7]), longitude=float(r[8]))
                    loc.save()
