# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-01 19:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_auto_20170401_1918'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Service_Request',
        ),
    ]
