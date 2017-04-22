# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-08 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0007_auto_20170408_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='preferredContact',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='secondaryEmailID',
        ),
        migrations.AddField(
            model_name='customer',
            name='preferEmail',
            field=models.BooleanField(default=True),
        ),
    ]
