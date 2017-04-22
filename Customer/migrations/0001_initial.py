# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-01 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service_Request',
            fields=[
                ('requestID', models.IntegerField(primary_key=True, serialize=False)),
                ('requestType', models.CharField(max_length=500)),
                ('subscriptionDate', models.CharField(max_length=100)),
                ('fufillmentDate', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
