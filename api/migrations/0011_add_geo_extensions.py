from django.db import migrations
from django.contrib.postgres.operations import CreateExtension

class Migration(migrations.Migration):
    dependencies = [('api', '0010_auto_20161019_0312')]

    operations = [CreateExtension('cube'),
                  CreateExtension('earthdistance')]
