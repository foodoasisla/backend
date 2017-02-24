from django.core.management.base import BaseCommand
import csv

from api.models import Location, Hour

import os


class Command(BaseCommand):
    help = 'is this thing on?'

    def handle(self, *args, **options):
        print('is this thing on???')
