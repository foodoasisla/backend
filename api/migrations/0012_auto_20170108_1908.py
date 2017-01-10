# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-08 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_add_geo_extensions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hour',
            name='day',
            field=models.CharField(choices=[(b'AllMo', b'Monday'), (b'AllTu', b'Tuesday'), (b'AllWe', b'Wednesday'), (b'AllTh', b'Thursday'), (b'AllFr', b'Friday'), (b'AllSa', b'Saturday'), (b'AllSu', b'Sunday'), (b'1stMo', b'First Monday'), (b'1stTu', b'First Tuesday'), (b'1stWe', b'First Wednesday'), (b'1stTh', b'First Thursday'), (b'1stFr', b'First Friday'), (b'1stSa', b'First Saturday'), (b'1stSu', b'First Sunday'), (b'2ndMo', b'Second Monday'), (b'2ndTu', b'Second Tuesday'), (b'2ndWe', b'Second Wednesday'), (b'2ndTh', b'Second Thursday'), (b'2ndFr', b'Second Friday'), (b'2ndSa', b'Second Saturday'), (b'2ndSu', b'Second Sunday'), (b'3rdMo', b'Third Monday'), (b'3rdTu', b'Third Tuesday'), (b'3rdWe', b'Third Wednesday'), (b'3rdTh', b'Third Thursday'), (b'3rdFr', b'Third Friday'), (b'3rdSa', b'Third Saturday'), (b'3rdSu', b'Third Sunday'), (b'4thMo', b'Fourth Monday'), (b'4thTu', b'Fourth Tuesday'), (b'4thWe', b'Fourth Wednesday'), (b'4thTh', b'Fourth Thursday'), (b'4thFr', b'Fourth Friday'), (b'4thSa', b'Fourth Saturday'), (b'4thSu', b'Fourth Sunday'), (b'LstMo', b'Last Monday'), (b'LstTu', b'Last Tuesday'), (b'LstWe', b'Last Wednesday'), (b'LstTh', b'Last Thursday'), (b'LstFr', b'Last Friday'), (b'LstSa', b'Last Saturday'), (b'LstSu', b'Last Sunday')], max_length=100),
        ),
    ]
