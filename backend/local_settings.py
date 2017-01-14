# local development settings

import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'la_food_oasis',
        'USER': 'la_food_oasis_user',
        # 'PASSWORD': os.environ['DB_PASSWORD'],
        'PASSWORD': '',
        'PORT': '',
        'HOST': 'localhost',
        'TEST': {
            'NAME': 'la_food_oasis_test',
            'USER': 'la_food_oasis_user'
        }
    }
}
