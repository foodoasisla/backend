from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO


class CSVingestTest(TestCase):
    # testing the final output of the CSV Ingest command

    def test_command_output(self):
        out = StringIO()
        call_command('csv_ingest', stdout=out)
        self.assertEqual(
            '1220 locations have been added to the database.\n', out.getvalue())
