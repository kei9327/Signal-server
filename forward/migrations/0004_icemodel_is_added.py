# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forward', '0003_auto_20170412_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='icemodel',
            name='is_added',
            field=models.BooleanField(default=False),
        ),
    ]
